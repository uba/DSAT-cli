# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

from datetime import datetime
from dsat.config import Config
from dsat.product import Catalog
from dsat.request import getImages

for name in Catalog.products:
    images = getImages([datetime.strptime('202111161200', '%Y%m%d%H%M')], name, 2, [0,1,2], [0,1,2])
    images[0].crop([0,0,678,678]).save(name + '.png')