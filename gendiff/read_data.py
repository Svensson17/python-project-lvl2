import json

import os

import yaml


def read_data(path):
    _, extension = os.path.splitext(path)
    extension = extension.lower()
    return parse(open(path), extension)


def parse(data, format_type):
    if format_type == ".json":
        return json.load(data)
    elif format_type in {'.yml', '.yaml'}:
        return yaml.safe_load(data)
