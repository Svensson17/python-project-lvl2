import json
import pytest

from gendiff.generate_diff import generate_diff

test_input_cases = ['json', 'yml']


@pytest.mark.parametrize('test_format', test_input_cases)
def test_gendiff(test_format):
    path_file1 = './tests/fixtures/file1.{}'.format(test_format)
    path_file2 = './tests/fixtures/file2.{}'.format(test_format)
    assert generate_diff(path_file1, path_file2) == open('./tests/fixtures/result_stylish', 'r').read()
    assert generate_diff(
        path_file1,
        path_file2,
        'plain'
    ) == open(
        './tests/fixtures/'
        'result_plain',
        'r'
    ).read()
    data = generate_diff(path_file1, path_file2, 'json')
    try:
        json.loads(data)
    except Exception as e:
        pytest.fail('Invalid json: {}'.format(e))
