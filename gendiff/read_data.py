import json

import yaml


def parse(data, format_type):
    if format_type == ".json":
        return json.load(data)
    elif format_type in {'.yml', '.yaml'}:
        return yaml.safe_load(data)
