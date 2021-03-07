"""Parsing and open files."""

import argparse


def parser_arg():
    """Parsing arguments."""
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    path_file1 = args.first_file
    path_file2 = args.second_file
    format_name = args.format
    return path_file1, path_file2, format_name
