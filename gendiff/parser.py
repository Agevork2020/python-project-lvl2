import argparse
from gendiff.generate_diff import render_diff

def parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', dest="format", type=str,
                        help='set format of output', default='stylish')
    args = parser.parse_args()
    answer = render_diff(args.first_file, args.second_file, args.format)
    return answer
