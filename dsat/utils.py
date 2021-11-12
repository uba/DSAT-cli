# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from datetime import timedelta
from dsat.config import Config
from PIL import Image
import random

def buildDates(startDate, count, delta):
    dates = [startDate]
    for t in range(0, count):
        dates.append(dates[t] + timedelta(minutes=delta))
    return dates

def computeFullImageSize(level):
    return len(Config.tilesLocation[level]) * Config.tileSize

def computeImageSize(nTilesX, nTilesY):
    return nTilesX * Config.tileSize, nTilesY * Config.tileSize

def pickServer():
    return random.choice(Config.servers)

def generateTileSequence(xmin, xmax, ymin, ymax): 
    return list(range(xmin, xmax+1)), list(range(ymin, ymax+1))

def createImage(tiles, nlines, ncols):
    result = Image.new('RGBA', (ncols, nlines), (0,0,0,0))
    for pos in tiles:
        result.paste(tiles[pos], (pos[0] * Config.tileSize, pos[1] * Config.tileSize))
    return result

def exportAnimation(images, duration, filename):
    images[0].save(filename, save_all=True, append_images=images[1:],
        optimize=Config.optimizeGif, duration=duration, loop=0)

