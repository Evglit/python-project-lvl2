"""Generating the difference between two files."""

from difference_calculator.formaters.stylish import stylish
from difference_calculator.formaters.plain import plain
from difference_calculator.formaters.json import format_json


def generate_diff(dict1, dict2, format_name):
    """Create a difference between two files in a selected format.
    Return string."""
    if format_name == 'stylish':
        result = diff(dict1, dict2)
        return stylish(result)
    elif format_name == 'plain':
        result = diff(dict1, dict2)
        return plain(result)
    elif format_name == 'json':
        result = diff(dict1, dict2)
        return format_json(result)
    return 'Format {} not found!'.format(format_name)


def diff(dict1, dict2):
    """Create a difference between two files. Return list."""
    result = []
    common_keys = sorted(list(dict1.keys() & dict2.keys()))
    added_keys = sorted(list(dict2.keys() - dict1.keys()))
    deleted_keys = sorted(list(dict1.keys() - dict2.keys()))
    for key in common_keys:
        process_common_keys(dict1, dict2, key, result)
    for key in added_keys:
        process_added_keys(dict2, key, result)
    for key in deleted_keys:
        process_deleted_keys(dict1, key, result)
    return result


def process_common_keys(dict1, dict2, key, result):
    if dict1[key] == dict2[key]:
        if has_children(dict1[key]):
            children = diff(dict1[key], dict2[key])
            node = create_internal_node(key, 'not changed', children)
            result.append(node)
        else:
            node = create_leaf_node(key, 'not changed', dict1[key])
            result.append(node)
    else:
        if has_children(dict1[key]) and has_children(dict2[key]):
            children = diff(dict1[key], dict2[key])
            node = create_internal_node(key, 'not changed', children)
            result.append(node)
        else:
            if has_children(dict1[key]):
                children = transform_dict(dict1[key])
                node = create_internal_node(key, 'before update', children)
                result.append(node)
            else:
                node = create_leaf_node(key, 'before update', dict1[key])
                result.append(node)
            if has_children(dict2[key]):
                children = transform_dict(dict2[key])
                node = create_internal_node(key, 'after update', children)
                result.append(node)
            else:
                node = create_leaf_node(key, 'after update', dict2[key])
                result.append(node)


def process_added_keys(dict2, key, result):
    if has_children(dict2[key]):
        children = transform_dict(dict2[key])
        node = create_internal_node(key, 'added', children)
        result.append(node)
    else:
        node = create_leaf_node(key, 'added', dict2[key])
        result.append(node)


def process_deleted_keys(dict1, key, result):
    if has_children(dict1[key]):
        children = transform_dict(dict1[key])
        node = create_internal_node(key, 'deleted', children)
        result.append(node)
    else:
        node = create_leaf_node(key, 'deleted', dict1[key])
        result.append(node)


def create_internal_node(name, status, children):
    '''Return internal node.'''
    return {
        'name': name,
        'status': status,
        'type node': 'internal',
        'children': children
    }


def create_leaf_node(name, status, data):
    '''Return leaf node.'''
    return {
        'name': name,
        'status': status,
        'type node': 'leaf',
        'data': data
    }


def has_children(value):
    '''Checks if there are children in the dictionary.'''
    if type(value) is dict:
        return True
    return False


def transform_dict(dictionary):
    """Transformation dictionaries to nodes. Returns a list of nodes."""
    result = []
    for key in dictionary.keys():
        if has_children(dictionary[key]):
            children = transform_dict(dictionary[key])
            node = create_internal_node(key, 'not changed', children)
            result.append(node)
        else:
            node = create_leaf_node(key, 'not changed', dictionary[key])
            result.append(node)
    return result
