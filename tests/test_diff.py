from gendiff.generate_diff import generate_diff


def test_gendiff_stylish():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file2.json'
    assert generate_diff(path_file1, path_file2) == open('./tests/fixtures/result_stylish', 'r').read()
