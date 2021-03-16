"""Create a difference between two dictionaries."""


def diff(dict1, dict2={}):
    """Create a difference between two dictionaries. Return list."""
    result = []
    if dict2 == {}:
        for key in dict1.keys():
            node = create_node(key, 'not changed', dict1)
            result.append(node)
        return result
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                node = create_node(key, 'not changed', dict1)
                result.append(node)
            else:
                if type(dict1[key]) is dict and type(dict2[key]) is dict:
                    node = create_node(key, 'not changed', dict1, dict2)
                    result.append(node)
                else:
                    node = create_node(key, 'before update', dict1)
                    result.append(node)
                    node = create_node(key, 'after update', dict2)
                    result.append(node)
        elif key in dict1:
            node = create_node(key, 'deleted', dict1)
            result.append(node)
        elif key in dict2:
            node = create_node(key, 'added', dict2)
            result.append(node)
    return result


def create_node(key, status, dict1, dict2={}):
    """Create a node. Return dict."""
    node = {'name': key, 'status': status}
    if dict2 == {}:
        if type(dict1[key]) is dict:
            node['type node'] = 'internal'
            node['children'] = diff(dict1[key])
        else:
            node['type node'] = 'leaf'
            node['data'] = dict1[key]
        return node
    node['type node'] = 'internal'
    node['children'] = diff(dict1[key], dict2[key])
    return node
