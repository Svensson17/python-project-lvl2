import json


def generate_diff(filename1, filename2):
    first_file = json.load(open(filename1))
    second_file = json.load(open(filename2))
    print(first_file, second_file)

    