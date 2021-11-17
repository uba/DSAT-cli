# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from dsat import cache
from dsat.config import Config
from dsat.utils import computeImageSize, createImage, pickServer
import logging as log
import multiprocessing as mp
from PIL import Image
import requests
from tqdm import tqdm

lock = mp.Lock()

def requestImage(url):
    log.info('Request ' + url[11:])
    # First, look cache...
    with lock:
        if Config.useCache and cache.exists(url):
            log.info('--> Loaded from cache')
            return cache.load(url) # Done!
    try:
        # else, try request...
        response = requests.get(url, stream=True)
        log.info('* Response code:' + str(response.status_code))
        if not response.ok:
            log.info('** Tile not found **')
            return Config.missingTileImage.copy()
        image = Image.open(response.raw).convert('RGBA')
        if Config.useCache:
            log.info('<-- Saving to cache')
            cache.save(url, image)
        return image
    except requests.exceptions.RequestException:
        log.info('** Tile not found **')
        return Config.missingTileImage.copy()

def getReference(ref, level, x, y):
    url = '{}://{}.{}/references/{}/{}/{}/{}.png'.format(Config.protocol, pickServer(),
        Config.baseURL, ref, level, x, y)
    return requestImage(url)

def addReference(name, level, x, y, tile):
    ref = getReference(name, level, x, y)
    tile.paste(ref, (0,0), mask=ref)

def getTile(date, product, time, level, x, y):
    url = '{}://{}.{}/{}/{}/{}/{}/{}/{}.png'.format(Config.protocol, 
        pickServer(), Config.baseURL, date, product, time, level, x, y)
    tile = requestImage(url)
    if Config.addReferences:
        for name in Config.references:
            addReference(name, level, x, y, tile)
    return tile

def getTiles(date, product, time, level, tilesx, tilesy):
    tiles = {}
    for x, i in zip(tilesx, range(len(tilesx))):
        for y, j in zip(tilesy, range(len(tilesy))):
            tiles[(i,j)] = getTile(date, product, time, level, x, y)
    return tiles

def getAllTiles(date, product, time, level):
    return getTiles(date, product, time, level,
        Config.tilesLocation[level], Config.tilesLocation[level])

def getImage(date, product, time, level, tilesx, tilesy, queue=None):
    tiles = getTiles(date, product, time, level, tilesx, tilesy)
    ncols, nlines = computeImageSize(len(tilesx), len(tilesy))
    image = createImage(tiles, nlines, ncols)
    if queue:
        queue.put((mp.current_process().name, image))
    return image

# Note: Multi-thread version
def getImages(dates, product, level, tilesx, tilesy, nProcess=Config.nProcesses):
    queue, processes, images = mp.Queue(), [], []
    for date in tqdm(dates, desc='Processing images', ascii=True, unit='image'):
        log.info('Processing date ' + date.strftime('%Y/%m/%d %H:%M'))
        p = mp.Process(target=getImage, name=date.strftime('%Y%m%d%H%M'),
            args=(date.strftime('%Y%m%d'), product, date.strftime('%H%M'), level, tilesx, tilesy, queue))
        processes.append(p)
        p.start()
        if len(processes) == nProcess: # Consume, wait and go ahead...
            log.info('Waiting...')
            _consume(queue, processes, images)
            queue, processes = mp.Queue(), []

    # The last one...
    _consume(queue, processes, images)

    # Note: images -> list([pid, image])
    # Order images by process name = date order
    images.sort(key=lambda tup: tup[0])
    return [img[1] for img in images]

def _consume(queue, processes, images):
    for p in processes:
        img = queue.get() # block
        images.append(img)
    for p in processes:
        p.join() # "Come together, yeah! \o"

# Note: Single-thread version
'''
def getImages(dates, product, level, tilesx, tilesy):
    images = []
    for date in tqdm(dates, desc='Processing images', ascii=True, unit='image'):
        images.append(getImage(date.strftime('%Y%m%d'), product,
            date.strftime('%H%M'), level, tilesx, tilesy))
    return images
'''
