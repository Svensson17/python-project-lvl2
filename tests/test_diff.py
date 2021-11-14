import json

from gendiff.generate_diff import generate_diff


def test_gendiff_stylish():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file2.json'
    assert generate_diff(path_file1, path_file2) == open('./tests/fixtures/result_stylish', 'r').read()


def test_gendiff_plain():
    path_file1 = './tests/fixtures/file1.yml'
    path_file2 = './tests/fixtures/file2.yml'
    output_format = 'plain'
    assert generate_diff(
        path_file1,
        path_file2,
        output_format
    ) == open(
        './tests/fixtures/'
        'result_plain',
        'r'
    ).read()


def test_diff_json():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file2.json'
    data = generate_diff(path_file1, path_file2)
    try:
        json.load(data)
    except Exception as e:
        print('Invalid json')
