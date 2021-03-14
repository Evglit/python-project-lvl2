from difference_calculator.formatters.stylish import stylish
from difference_calculator.formatters.plain import plain
from difference_calculator.formatters.json import format_json


def format_diff(list_diff, format_name):
    """Formats a list of differences to the specified format. Return string."""
    if format_name == 'stylish':
        return stylish(list_diff)
    elif format_name == 'plain':
        return plain(list_diff)
    elif format_name == 'json':
        return format_json(list_diff)
    return 'Format {} not found!'.format(format_name)
