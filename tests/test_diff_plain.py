import pytest

from gendiff.generate_diff import generate_diff

def test_gendiff_plain():
    path_file1 = './tests/fixtures/file1.yml'
    path_file2 = './tests/fixtures/file2.yml'
    assert generate_diff(path_file1,path_file2) == open('./tests/fixtures/result_plain', 'r').read()