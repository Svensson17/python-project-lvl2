import json

import os

import yaml

from gendiff.diff import build_diff
from gendiff.formator.formator import formator
from gendiff.read_data import read_data


def generate_diff(filename1, filename2, format_name='stylish'):
    data1 = read_data(filename1)
    data2 = read_data(filename2)
    diff = build_diff(data1, data2)
    return formator(diff, format_name)
