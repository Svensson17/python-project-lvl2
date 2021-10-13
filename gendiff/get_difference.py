import argparse


def helper():
    parser = argparse.ArgumentParser(description='Generate difference')
    parser.add_argument('first_argument')
    parser.add_argument('second_argument')
    parser.add_argument('- f', '-- format', help='set format of output')
    args = parser.parse_args()
    return args
