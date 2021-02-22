"""Parsing and open files."""

import argparse
from difference_calculator.tools.open_file import open_file


def parser_arg():
    """Parsing arguments."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    arg1 = open_file(args.first_file)
    arg2 = open_file(args.second_file)
    format_name = (args.format)
    return arg1, arg2, format_name
