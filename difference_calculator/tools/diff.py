"""Create a difference between two dictionaries."""


def diff(dict1, dict2):
    """Create a difference between two dictionaries. Return list."""
    result = []
    common_keys = sorted(dict1.keys() & dict2.keys())
    added_keys = sorted(dict2.keys() - dict1.keys())
    deleted_keys = sorted(dict1.keys() - dict2.keys())
    for key in common_keys:
        node_list = process_common_keys(dict1, dict2, key)
        result.extend(node_list)
    for key in added_keys:
        node = process_added_keys(dict2, key)
        result.append(node)
    for key in deleted_keys:
        node = process_deleted_keys(dict1, key)
        result.append(node)
    return result


def process_common_keys(dict1, dict2, key):
    """Processes common elements of dictionaries. Returns a list of nodes."""
    result = []
    if dict1[key] == dict2[key]:
        if value_is_dict(dict1[key]):
            children = diff(dict1[key], dict2[key])
            node = create_internal_node(key, 'not changed', children)
            result.append(node)
        else:
            node = create_leaf_node(key, 'not changed', dict1[key])
            result.append(node)
    else:
        if value_is_dict(dict1[key]) and value_is_dict(dict2[key]):
            children = diff(dict1[key], dict2[key])
            node = create_internal_node(key, 'not changed', children)
            result.append(node)
        else:
            if value_is_dict(dict1[key]):
                children = transform_dict(dict1[key])
                node = create_internal_node(key, 'before update', children)
                result.append(node)
            else:
                node = create_leaf_node(key, 'before update', dict1[key])
                result.append(node)
            if value_is_dict(dict2[key]):
                children = transform_dict(dict2[key])
                node = create_internal_node(key, 'after update', children)
                result.append(node)
            else:
                node = create_leaf_node(key, 'after update', dict2[key])
                result.append(node)
    return result


def process_added_keys(dict2, key):
    """Processes unique elements of the second dictionary. Returns a node."""
    if value_is_dict(dict2[key]):
        children = transform_dict(dict2[key])
        node = create_internal_node(key, 'added', children)
        return node
    else:
        node = create_leaf_node(key, 'added', dict2[key])
        return node


def process_deleted_keys(dict1, key):
    """Processes unique elements of the first dictionary. Returns a node."""
    if value_is_dict(dict1[key]):
        children = transform_dict(dict1[key])
        node = create_internal_node(key, 'deleted', children)
        return node
    else:
        node = create_leaf_node(key, 'deleted', dict1[key])
        return node


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


def value_is_dict(value):
    '''Checks if a dictionary value is a dictionary.'''
    if type(value) is dict:
        return True
    return False


def transform_dict(dictionary):
    """Transformation dictionaries to node_list. Returns a list of node_list."""
    result = []
    for key in dictionary.keys():
        if value_is_dict(dictionary[key]):
            children = transform_dict(dictionary[key])
            node = create_internal_node(key, 'not changed', children)
            result.append(node)
        else:
            node = create_leaf_node(key, 'not changed', dictionary[key])
            result.append(node)
    return result
