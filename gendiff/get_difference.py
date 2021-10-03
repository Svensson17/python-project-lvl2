import argparse


def get_difference():
    parser = argparse.ArgumentParser(description='Generate difference')
    parser.add_argument('first_argument')
    parser.add_argument('second_argument')
    args = parser.parse_args()
    print(args.first_file, args.second_file)
