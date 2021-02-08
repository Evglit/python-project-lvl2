"""Test comprsion file.json"""

from difference_calculator.tools.comparison import generate_diff
from pathlib import Path
import json
import yaml


def test_generate_diff_json():
    path_dict1 = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'file1.json')
    path_dict2 = path_dict1.with_name('file2.json')
    dict1 = json.load(open('{}'.format(path_dict1)))
    dict2 = json.load(open('{}'.format(path_dict2)))
    path_right_answer = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'right_answer.txt')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2) == right_answer.read()


def test_generate_diff_yml():
    path_dict3 = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'file1.yml')
    path_dict4 = path_dict3.with_name('file2.yml')
    with open(path_dict3) as f:
        dict3 = yaml.safe_load(f)
    with open(path_dict4) as f:
        dict4 = yaml.safe_load(f)
    path_right_answer = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'right_answer.txt')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict3, dict4) == right_answer.read()
