"""Test comprsion"""

from difference_calculator.tools.comparison import generate_diff
from pathlib import Path
import json


def test_generate_diff():
    path_dict1 = Path(
        Path().absolute(),
        'fixtures',
        'file1.json')
    path_dict2 = path_dict1.with_name('file2.json')
    path_right_answer = path_dict1.with_name('right_answer.txt')
    dict1 = json.load(open('{}'.format(path_dict1)))
    dict2 = json.load(open('{}'.format(path_dict2)))
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2) == right_answer.read()
