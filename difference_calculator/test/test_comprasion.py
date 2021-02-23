"""Test generate_diff"""

from difference_calculator.gendiff import generate_diff
from pathlib import Path
import json
import yaml


def test_diff_stylish_json():
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
        'right_answer_stylish.txt')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2, 'stylish') == right_answer.read()


def test_diff_stylish_yml():
    path_dict1 = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'file1.yml')
    path_dict2 = path_dict1.with_name('file2.yml')
    with open(path_dict1) as f:
        dict1 = yaml.safe_load(f)
    with open(path_dict2) as f:
        dict2 = yaml.safe_load(f)
    path_right_answer = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'right_answer_stylish.txt')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2, 'stylish') == right_answer.read()


def test_diff_plain_json():
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
        'right_answer_plain.txt')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2, 'plain') == right_answer.read()


def test_diff_plain_yml():
    path_dict1 = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'file1.yml')
    path_dict2 = path_dict1.with_name('file2.yml')
    with open(path_dict1) as f:
        dict1 = yaml.safe_load(f)
    with open(path_dict2) as f:
        dict2 = yaml.safe_load(f)
    path_right_answer = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'right_answer_plain.txt')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2, 'plain') == right_answer.read()


def test_diff_foramtjson_json():
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
        'right_answer.json')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2, 'json') == right_answer.read()


def test_diff_foramtjson_yml():
    path_dict1 = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'file1.yml')
    path_dict2 = path_dict1.with_name('file2.yml')
    with open(path_dict1) as f:
        dict1 = yaml.safe_load(f)
    with open(path_dict2) as f:
        dict2 = yaml.safe_load(f)
    path_right_answer = Path(
        Path(__file__).parent.absolute(),
        'fixtures',
        'right_answer.json')
    right_answer = open('{}'.format(path_right_answer))
    assert generate_diff(dict1, dict2, 'json') == right_answer.read()
