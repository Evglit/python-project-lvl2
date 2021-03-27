"""Create a difference between two dictionaries."""


def diff(dict1, dict2):
    """Create a difference between two dictionaries. Return list."""
    result = []
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        node = {'name': key}
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                node['status'] = 'not changed'
                if type(dict1[key]) is dict:
                    node['status'] = 'nested'
                    node['children'] = diff(dict1[key], dict2[key])
                else:
                    node['data'] = dict1[key]
            else:
                node['status'] = 'changed'
                if type(dict1[key]) is dict and type(dict2[key]) is dict:
                    node['status'] = 'nested'
                    node['children'] = diff(dict1[key], dict2[key])
                else:
                    node['data before'] = dict1[key]
                    node['data after'] = dict2[key]
        elif key in dict1:
            node['status'] = 'deleted'
            node['data'] = dict1[key]
        elif key in dict2:
            node['status'] = 'added'
            node['data'] = dict2[key]
        result.append(node)
    return result
