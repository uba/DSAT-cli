# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from dsat.config import Config
import hashlib
import os
from PIL import Image

def encode(url):
    # Note: url[11:] => Remove 'https://s{}.' part
    key = hashlib.md5(url[11:].encode('utf-8')).hexdigest()
    return '{}{}.png'.format(Config.cacheDir, key)

def exists(url):
    key = encode(url)
    return os.path.exists(key)

def load(url):
    key = encode(url)
    return Image.open(key)

def save(url, image):
    os.makedirs(Config.cacheDir, exist_ok=True)
    image.save(encode(url))
