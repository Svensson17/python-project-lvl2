def render_plain(diff, depth=0):
    diff_type = diff["type"]
    key = diff.get("key")
    children = diff.get("children")
    print(key)
    if diff_type == "origin":
        rows = [render_plain(child) for child in children]
        return "\n".join(to_list(rows))
    if diff_type == "nested":
        rows = []
        for child in children:
            child["key"] = "{0}.{1}".format(key, child["key"])
            rows.append(render_plain(child))
        return rows
    if diff_type == "added":
        value = to_string(diff[value])
        return "Property '{0}' was added with value: {1}".format(key, value)
    if diff_type == "removed":
        return "Property '{0}' was removed".format(key)
    if diff_type == "updated":
        value = to_string(diff[old_value])
        new_value = to_string(diff[new_value])
        return "Property '{0}' was updated. From {1} to {2}".format(
            key,
            value,
            new_value,
        )
    if diff_type == "unchanged":
        return[]

def to_list(items):
    items_list = []
    if not isinstance(items, list):
        return [items]
    for item in items:
        items_list.extend(to_list(item))
    return items_list

def to_string(value_to_string):
    if isinstance(value_to_string, dict):
        return '[complex value]'
    if isinstance(value_to_string, string):
        return "'{0}'".format(value_to_str)
    if value_to_string is None:
        return "null"
    return str(value-to_string.lower())
