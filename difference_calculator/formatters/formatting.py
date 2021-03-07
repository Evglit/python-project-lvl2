from difference_calculator.formatters.stylish import stylish
from difference_calculator.formatters.plain import plain
from difference_calculator.formatters.json import format_json


def formatting(dictionary, format_name):
    if format_name == 'stylish':
        return stylish(dictionary)
    elif format_name == 'plain':
        return plain(dictionary)
    elif format_name == 'json':
        return format_json(dictionary)
    return 'Format {} not found!'.format(format_name)
