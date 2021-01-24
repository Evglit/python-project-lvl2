#!/usr/bin/env python3

import argparse
import json
from difference_calculator.tools.comparison import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    arg1 = json.load(open(args.first_file))
    arg2 = json.load(open(args.second_file))
    print(generate_diff(arg1, arg2))


if __name__ == '__main__':
    main()
