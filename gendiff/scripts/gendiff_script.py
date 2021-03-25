#!/usr/bin/env python3
"""A gendiff script."""
import argparse
from gendiff import generate_diff


def main():
    """Run a code."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', dest="format", type=str, help='set format of output')
    args = parser.parse_args()
    answer = generate_diff(args.first_file, args.second_file)
    print(answer)   


if __name__ == '__main__':
    main()

