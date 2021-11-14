INDENT_TYPE = ' '
INDENT_SIZE = 4


def render_stylish(diff, depth=0):
    diff_type = diff["type"]
    key = diff.get("key")
    indent = make_indent(depth)
    children = diff.get("children")
    if diff_type == "origin":
        rows = ["{0}{1}\n".format(
            indent,
            render_stylish(child, depth)
        ) for child in children]
        return "{{\n{0}}}".format("".join(rows))
    if diff_type == "nested":
        rows = ["{0}\n". format(render_stylish(child, depth + 1)) for child in children]
        return "{0}    {1}: {{\n{2}{3}}}".format(indent, key, "".join(rows), make_indent(depth + 1))

    if diff_type == "added":
        return "{0}  + {1}: {2}".format(indent, key, to_string(diff["value"], depth))

    if diff_type == "removed":
        return "{0}  - {1}: {2}".format(indent, key, to_string(diff["value"], depth))

    if diff_type == "updated":
        str1 = "{0}  - {1}: {2}".format(indent, key, to_string(diff["old_value"], depth))
        str2 = "{0}  + {1}: {2}".format(indent, key, to_string(diff["new_value"], depth))
        return "\n".join([str1, str2])

    if diff_type == "unchanged":
        return "{0}    {1}: {2}".format(indent, key, to_string(diff["value"], depth))


def to_string(value_to_string, depth):
    if value_to_string is None:
        return "null"
    if isinstance(value_to_string, bool):
        return str(value_to_string).lower()
    if isinstance(value_to_string, dict):
        result = []
        indent = make_indent(depth + 1)
        for key, value_to_string in value_to_string.items():
            str_value = to_string(value_to_string, depth + 1)
            result.append("{0}    {1}: {2}\n".format(indent, key, str_value))
        return "{{\n{0}{1}}}".format("".join(result), indent)
    return value_to_string


def make_indent(depth):
    return INDENT_TYPE * INDENT_SIZE * depth