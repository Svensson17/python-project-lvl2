def build_diff(data1, data2):
    return {
        "type": "origin",
        "children": create(data1, data2)
    }

def create(data1, data2=None):
    if not isinstance(data1, dict):
        return data1
    if data2 is None:
        data2 = data1
    keys = create_list_keys(data1, data2)
    result = []
    for key in sorted(keys):
        if key not in data1:
            result.append({
                "type": "added",
                "key": key,
                "value": data2[key]
            })
        elif key not in data2:
            result.append({
                "type": "removed",
                "key": key,
                "value": data1[key]
            })
        elif isinstance(data1[key], dict):
            if isinstance(data2[key], dict):
                result.append({
                    "type": "nested",
                    "key": key,
                    "children": create(data1[key], data2[key])
                })
        elif data1[key] != data2[key]:
            result.append({
                "type": "updated",
                "key": key,
                "old_value": data1[key],
                "new_value": data2[key]
            })
        else:
            result.append({
                "type": "unchanged",
                "key": key,
                "value": data1[key]
            })
    return result



def create_list_keys(data1, data2):
    keys1 = list(data1.keys())
    keys2 = list(data2.keys())
    return keys1 if (data1 == data2) else set(keys1 + keys2)
