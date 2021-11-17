# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

import multiprocessing
from PIL import Image

"""DSAT-Cli Configuration."""

class Config:
    tileSize = 256
    baseURL = 'cptec.inpe.br/pesquisa/goes/goes16/web_tiles'
    protocol = 'https'
    servers = ['s0', 's1', 's2', 's3']
    tilesLocation = {
        2 : range(0, 3),
        3 : range(0, 6),
        4 : range(0, 11),
        5 : range(0, 22),
        6 : range(0, 43),
        7 : range(0, 84)
    }
    addReferences = True
    references = ['countries', 'labels']
    frameRate = 0.5 # seconds
    optimizeGif = True
    useCache = True
    cacheDir = '.cache/'
    defaultProduct = 'true_color_ch13_dsa'
    missingTileImage = Image.new('RGBA', (tileSize, tileSize), (0,0,0,0))
    nProcesses =  multiprocessing.cpu_count()

Config = Config()
