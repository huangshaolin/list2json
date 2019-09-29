#!/usr/bin/env python3

"""my_program

Usage:
    my_program [--debug] <md_path> [<json_path>] [--indent=<indent_str>]
    my_program -h | --help
    my_program --version

Options:
    --indent=<indent>        markdown indent string (tab by default)
    --debug         print debugging information
    -h --help       show this help
    --version       show version

"""

# Imports
import os
import json
import inspect
import logging

from docopt import docopt

from indented_lines_to_dict import indented_lines_to_dict


# Global variables
ROOT_DIR = os.path.dirname(os.path.realpath(
    inspect.getfile(inspect.currentframe())))

logger = logging.getLogger(__name__)


# Class declarations


# Function declarations


def main(args):
    logger.debug(args)
    md_path = args.get("<md_path>")
    json_path = args.get("<json_path>")
    indent_str = args.get("--indent")

    if not json_path:
        json_path = md_path + ".json"
    if not indent_str:
        indent_str = '\t'

    with open(md_path, 'r') as f:
        lines = f.readlines()
    d = indented_lines_to_dict(lines, indent_str)
    with open(json_path, 'w') as f:
        json.dump(d, f)
    print("Done!")


# Main body
if __name__ == "__main__":
    args = docopt(__doc__, version='my_program 0.0.1')
    if args.get('--debug'):
        logging.basicConfig(level=logging.DEBUG)
    main(args)
