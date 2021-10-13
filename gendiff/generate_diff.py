import json


def generate_diff(filename1, filename2):
    data1 = json.load(open(filename1))
    data2 = json.load(open(filename2))
    print(data1, data2)
    keys = set(list(data1.keys()) + list(data2.keys()))
    result = "{\n"
    for key in sorted(keys):
        if key not in data2:
            result += "  - {}: {}\n".format(key, data1[key])
        elif key not in data1:
            result += "  + {}: {}\n".format(key, data2[key])
        elif data1[key] != data2[key]:
            result += "  - {}: {}\n".format(key, data1[key])
            result += "  + {}: {}\n".format(key, data2[key])
        else:
            result += "    {}: {}\n".format(key, data1[key])
    result += "}"
    return result


    