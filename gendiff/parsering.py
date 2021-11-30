import argparse


def parse_data():
    parser = argparse.ArgumentParser(description='Generate difference')
    parser.add_argument('first_argument')
    parser.add_argument('second_argument')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='stylish'
    )
    return parser.parse_args()
