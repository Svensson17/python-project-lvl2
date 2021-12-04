from gendiff.diff import build
from gendiff.formator.formator import format_data
from gendiff.read_data import parse
import os


def read_data(path):
    _, extension = os.path.splitext(path)
    extension = extension.lower()
    return parse(open(path), extension)


def generate_diff(filename1, filename2, format_name='stylish'):
    data1 = read_data(filename1)
    data2 = read_data(filename2)
    diff = build(data1, data2)
    return format_data(diff, format_name)
