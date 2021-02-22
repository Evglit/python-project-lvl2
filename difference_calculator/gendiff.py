"""Generating the difference between two files."""

from difference_calculator.formaters.stylish import stylish
from difference_calculator.formaters.plain import plain


def generate_diff(dict1, dict2, format_name):
    """Create a difference between two files in a selected format. Return string."""
    result = diff(dict1, dict2)
    if format_name == 'stylish':
        return stylish(result)
    elif 'plain':
        return plain(result)
    else:
        return 'Format not found!'


def diff(dict1, dict2):
    """Create a difference between two files. Return list."""
    result = []
    common_keys = sorted(list(dict1.keys() & dict2.keys()))
    added_keys = sorted(list(dict2.keys() - dict1.keys()))
    deleted_keys = sorted(list(dict1.keys() - dict2.keys()))
    for key in common_keys:
        if dict1[key] == dict2[key]:
            if type(dict1[key]) is dict:
                result.append({
                    'name': key,
                    'status': 'not changed',
                    'type node': 'internal',
                    'children': diff(dict1[key], dict2[key]),
                })
            else:
                result.append({
                    'name': key,
                    'status': 'not changed',
                    'type node': 'leaf',
                    'data': dict1[key],
                })
        else:
            if type(dict1[key]) is dict and type(dict2[key]) is dict:
                result.append({
                    'name': key,
                    'status': 'not changed',
                    'type node': 'internal',
                    'children': diff(dict1[key], dict2[key]),
                })
            else:
                if type(dict1[key]) is dict:
                    result.append({
                        'name': key,
                        'status': 'before update',
                        'type node': 'internal',
                        'children': transform_dict(dict1[key]),
                    })
                else:
                    result.append({
                        'name': key,
                        'status': 'before update',
                        'type node': 'leaf',
                        'data': dict1[key],
                    })
                if type(dict2[key]) is dict:
                    result.append({
                        'name': key,
                        'status': 'after update',
                        'type node': 'internal',
                        'children': transform_dict(dict2[key]),
                    })
                else:
                    result.append({
                        'name': key,
                        'status': 'after update',
                        'type node': 'leaf',
                        'data': dict2[key],
                    })
    for key in added_keys:
        if type(dict2[key]) is dict:
            result.append({
                'name': key,
                'status': 'added',
                'type node': 'internal',
                'children': transform_dict(dict2[key]),
            })
        else:
            result.append({
                'name': key,
                'status': 'added',
                'type node': 'leaf',
                'data': dict2[key],
            })
    for key in deleted_keys:
        if type(dict1[key]) is dict:
            result.append({
                'name': key,
                'status': 'deleted',
                'type node': 'internal',
                'children': transform_dict(dict1[key]),
            })
        else:
            result.append({
                'name': key,
                'status': 'deleted',
                'type node': 'leaf',
                'data': dict1[key],
            })
    return result


def transform_dict(dictionary):
    """Transformation of the source dictionary. Return dictionary."""
    result = []
    for key in dictionary.keys():
        if type(dictionary[key]) is dict:
            result.append({
                'name': key,
                'status': 'not changed',
                'type node': 'internal',
                'children': transform_dict(dictionary[key]),
            })
        else:
            result.append({
                'name': key,
                'status': 'not changed',
                'type node': 'leaf',
                'data': dictionary[key],
            })
    return result
