"""Test comprsion"""

from difference_calculator.tools.comparison import generate_diff


def test_generate_diff():
    dict1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    dict2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }
    right_answer = (
        '{\n    host: hexlet.io'
        '\n  - timeout: 50'
        '\n  + timeout: 20'
        '\n  - proxy: 123.234.53.22'
        '\n  - follow: False'
        '\n  + verbose: True'
        '\n}'
    )
    assert generate_diff(dict1, dict2) == right_answer
