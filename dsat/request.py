# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from dsat import cache
from dsat.config import Config
from dsat.utils import computeImageSize, createImage, pickServer
import logging as log
from PIL import Image
import requests
from tqdm import tqdm

def requestImage(url):
    log.info('Request ' + url[11:])
    if Config.useCache and cache.exists(url):
        log.info('--> Loaded from cache')
        return cache.load(url)
    else:
        response = requests.get(url, stream=True)
        log.info('* Response code:' + str(response.status_code))
        image = Image.open(response.raw).convert('RGBA')
        if Config.useCache:
            log.info('<-- Saving to cache')
            cache.save(url, image)
        return image

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
        for ref in Config.references:
            addReference(ref, level, x, y, tile)
    return tile

def getTiles(date, product, time, level, tilesx, tilesy):
    tiles = {}
    for x, i in zip(tilesx, range(0, len(tilesx))):
        for y, j in zip(tilesy, range(0, len(tilesy))):
            tiles[(i,j)] = getTile(date, product, time, level, x, y)
    return tiles

def getAllTiles(date, product, time, level):
    return getTiles(date, product, time, level, Config.tilesLocation[level], Config.tilesLocation[level])

def getImage(date, product, time, level, tilesx, tilesy):
    tiles = getTiles(date, product, time, level, tilesx, tilesy)
    ncols, nlines = computeImageSize(len(tilesx), len(tilesy))
    return createImage(tiles, nlines, ncols)

def getImages(dates, product, level, tilesx, tilesy):
    images = []
    for date in tqdm(dates, desc='Processing images', ascii=True, unit='image'):
        images.append(getImage(date.strftime('%Y%m%d'), product,
            date.strftime('%H%M'), level, tilesx, tilesy))
    return images
