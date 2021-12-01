### Hexlet tests and linter status:
[![Actions Status](https://github.com/Svensson17/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Svensson17/python-project-lvl2/actions)
[![Actions Status](https://github.com/Svensson17/python-project-lvl2/workflows/CI/badge.svg)](https://github.com/Svensson17/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a666788d7de42b480694/maintainability)](https://codeclimate.com/github/Svensson17/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a666788d7de42b480694/test_coverage)](https://codeclimate.com/github/Svensson17/python-project-lvl2/test_coverage)

This is my second project on hexlet.io. Here I have implemented project which finds and shows the difference between files of different types. Descriptions of it you can find below.
Command 'poetry run gendiff -h' gives us project help. Command 'poetry run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json' shows us difference between two fixtures.
The diff is built based on how the files have changed relative to each other, the keys are displayed in alphabetical order.
The absence of a plus or minus signifies that the key is present in both files, and its values are the same. In all other situations, the value for the key is either different, or the key is only in one file.

[![asciicast](https://asciinema.org/a/P6cTR7YQEPX7oHPMfuNSmPbbK.svg)](https://asciinema.org/a/P6cTR7YQEPX7oHPMfuNSmPbbK)