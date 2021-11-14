from gendiff.formator.plain import render_plain

from gendiff.formator.json import render_json

from gendiff.formator.stylish import render_stylish


def formator(diff, format_name):
    if format_name == "stylish":
        return render_stylish(diff)
    if format_name == "plain":
        return render_plain(diff)
    if format_name == 'json':
        return render_json(diff)



