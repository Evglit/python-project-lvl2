#!/usr/bin/env python3

import argparse
from difference_calculator.tools.gendiff import generate_diff
from difference_calculator.tools.to_parse import to_parse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    arg1 = to_parse(args.first_file)
    arg2 = to_parse(args.second_file)
    print(generate_diff(arg1, arg2))


if __name__ == '__main__':
    main()
