#!/usr/bin/env python3

"""my_program

Usage:
    my_program [--debug]
    my_program -h | --help
    my_program --version

Options:
    --debug         print debugging information
    -h --help       show this help
    --version       show version

"""

# Imports
import os
import inspect
import logging

from docopt import docopt


# Global variables
ROOT_DIR = os.path.dirname(os.path.realpath(
    inspect.getfile(inspect.currentframe())))

logger = logging.getLogger(__name__)


# Class declarations


# Function declarations


def main(args):
    logger.debug(args)
    pass


# Main body
if __name__ == "__main__":
    args = docopt(__doc__, version='my_program 0.0.1')
    if args.get('--debug'):
        logging.basicConfig(level=logging.DEBUG)
    main(args)
