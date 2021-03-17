"""Test generate_diff"""

import pytest
from gendiff.generate_diff import generate_diff
from pathlib import Path


@pytest.mark.parametrize(
    "file1,file2,right_answer,format_name",
    [
        ('file1.json', 'file2.json', 'right_answer_stylish.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'right_answer_stylish.txt', 'stylish'),
        ('file1.json', 'file2.json', 'right_answer_plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'right_answer_plain.txt', 'plain'),
        ('file1.json', 'file2.json', 'right_answer.json', 'json'),
        ('file1.yml', 'file2.yml', 'right_answer.json', 'json')
    ]
)
def test_diff_stylish_json(file1, file2, right_answer, format_name):
    path_dict1 = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        file1)
    path_dict2 = path_dict1.with_name(file2)
    path_right_answer = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        right_answer)
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(path_dict1, path_dict2, format_name) \
        == right_answer.read()[:-1]
