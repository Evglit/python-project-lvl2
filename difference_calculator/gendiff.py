"""Generating the difference between two files."""


from difference_calculator.tools.parsing_file import parsing_file
from difference_calculator.tools.diff import diff
from difference_calculator.formatters.formatting import formatting


def generate_diff(path_file1, path_file2, format_name='stylish'):
    """Create a difference between two files in a selected format.
    Return string."""
    dict1 = parsing_file(path_file1)
    dict2 = parsing_file(path_file2)
    result = diff(dict1, dict2)
    return formatting(result, format_name)
