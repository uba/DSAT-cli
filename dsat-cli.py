# Copyright (C) 2021-2022 INPE.
# DSAT-Cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import argparse
from datetime import datetime
from dsat.config import Config
from dsat.request import getImage, getImages
from dsat.utils import buildDates, exportAnimation, generateTileSequence
from dsat.version import __version__
import logging as log

def isValidDate(s):
    try:
        return datetime.strptime(s, '%Y%m%d%H%M')
    except ValueError:
        raise argparse.ArgumentTypeError("Not a valid date: '{0}'.".format(s))
        
if __name__ == '__main__':
    # Create command-line parser
    parser = argparse.ArgumentParser(description='DSAT-Cli. Copyright (C) 2021-2022 INPE.', prog='dsat-cli')
    #> Product
    # TODO: build product informations.
    parser.add_argument('--product', '-p', help='Product that will be retrieved',
        type=str, dest='product', required=True)
    #> Date
    parser.add_argument('--date', '-d', help='Desired image datetime. Format: YYYYMMDDhhmm',
        type=isValidDate, dest='date', required=True)
    #> Image count
    parser.add_argument('-i', help='Number of images that will be requested from the given date as start.',
        type=int, dest='i', default=6, required=False)
    #> Time-step
    parser.add_argument('--time-step', '-t', help='Interval of image capture times in minutes. (default 10)',
        type=int, dest='time', default=10, required=False)
    #> Level
    parser.add_argument('--level', '-l', help='Level (zoom)  that will be retrieved',
        type=int, dest='level', choices=Config.tilesLocation.keys(), required=True)
    #> Tiles-extent
    parser.add_argument('--tiles-extent', help='Optional tiles extent',
        nargs=4, metavar=('xmin', 'ymin', 'xmax', 'xmax'),
        type=int, dest='extent', default=None, required=False)
    #> Speed-animation
    parser.add_argument('--speed', help='Frame rate, i.e. time between two consecutive frames. Default: 0.5 (in seconds)',
        type=float, dest='speed', default=Config.frameRate, required=False)
    #> Output
    parser.add_argument('--output', '-o', help='Output filename to save resut',
        type=str, dest='output', required=True)
    #> Verbose
    parser.add_argument('--verbose', help='Increase output verbosity',
        action='store_true')
    #> Version
    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + __version__)

    # Parse input
    args = parser.parse_args()

    # Setup verbose
    if args.verbose:
        log.basicConfig(format='%(levelname)s: %(message)s', level=log.INFO)

    log.info('-- Parameters --')
    for arg in vars(args):
        log.info(arg + ': ' + str(getattr(args, arg)))

    # Verify tiles-extent
    extent = args.extent
    if not extent:
        tilesIndex = Config.tilesLocation[args.level]
        extent = [tilesIndex[0], tilesIndex[0], tilesIndex[-1], tilesIndex[-1]] 

    # Build tiles that will be requested
    xmin, ymin, xmax, ymax = extent[0], extent[1], extent[2], extent[3]
    tilesx, tilesy = generateTileSequence(xmin, xmax, ymin, ymax)
    
    log.info('-- Tiles --')
    log.info('x:' + str(tilesx))
    log.info('y:' + str(tilesy))

    # Compute dates
    dates = buildDates(args.date, args.i-1, args.time)

    log.info('-- Dates --')
    for d in dates: log.info(d)

    log.info('Using cache: ' + str(Config.useCache))

    # TODO: use tqdm for progress bar indicator
    # Let's go!
    images = getImages(dates, args.product, args.level, tilesx, tilesy)
    log.info('Saving result to file: ' + args.output)
    if len(images) == 1:
        images[0].save(args.output)
    else:
        exportAnimation(images, args.speed * 1000, args.output)

    print('Done. Bye! \o')
    print('Visit www.cptec.inpe.br/dsat')
