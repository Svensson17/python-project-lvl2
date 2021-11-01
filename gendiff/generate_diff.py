import json

import os

import yaml

from gendiff.diff import build_diff
from gendiff.formator.formator import formator


def generate_diff(filename1, filename2, format_name= 'stylish'):
    _, extension = os.path.splitext(filename1)
    if extension == ".json":
        data1 = json.load(open(filename1))
        data2 = json.load(open(filename2))
    else:
        data1 = yaml.safe_load(open(filename1))
        data2 = yaml.safe_load(open(filename2))
    #
    # print(data1, data2)
    # keys = set(list(data1.keys()) + list(data2.keys()))
    # result = "{\n"
    # for key in sorted(keys):
    #     if key not in data2:
    #         result += "  - {}: {}\n".format(key, data1[key])
    #     elif key not in data1:
    #         result += "  + {}: {}\n".format(key, data2[key])
    #     elif data1[key] != data2[key]:
    #         result += "  - {}: {}\n".format(key, data1[key])
    #         result += "  + {}: {}\n".format(key, data2[key])
    #     else:
    #         result += "    {}: {}\n".format(key, data1[key])
    # result += "}"
    diff = build_diff(data1, data2)
    return formator(diff, format_name)



    