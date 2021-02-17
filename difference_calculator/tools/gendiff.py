"""Comparing flat files."""

from difference_calculator.tools.formater import stylish


def generate_diff(dict1, dict2, format_name=stylish):
    str_data(dict1)
    str_data(dict2)
    result = diff(dict1, dict2)
    return format_name(result)


def diff(dict1, dict2):
    result = {}
    common_keys = list(dict1.keys() & dict2.keys())
    added_keys = list(dict2.keys() - dict1.keys())
    deleted_keys = list(dict1.keys() - dict2.keys())
    for key in common_keys:
        if dict1[key] == dict2[key]:
            result['  ' + key] = dict1[key]
        else:
            if type(dict1[key]) is dict and type(dict2[key]) is dict:
                result['  ' + key] = diff(dict1[key], dict2[key])
            else:
                result['- ' + key] = dict1[key]
                result['+ ' + key] = dict2[key]
    for key in added_keys:
        result['+ ' + key] = dict2[key]
    for key in deleted_keys:
        result['- ' + key] = dict1[key]
    return result


def str_data(dictionary):
    for key in dictionary.keys():
        if type(dictionary[key]) is dict:
            str_data(dictionary[key])
        elif dictionary[key] is True:
            dictionary[key] = 'true'
        elif dictionary[key] is False:
            dictionary[key] = 'false'
        elif dictionary[key] is None:
            dictionary[key] = 'null'
