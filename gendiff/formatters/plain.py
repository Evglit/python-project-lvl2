'''Flat format formater.'''


def plain(diff_list, path=''):
    """Converts a list of differences to flat format. Returns string."""
    result = ''
    diff_list.sort(key=lambda x: x['name'])
    for node in diff_list:
        difference = process_node(node, path)
        result += difference
    return result


def process_node(node, path):
    """Analysis of the node. Returns a string with changes
    if the node was changed."""
    if node['status'] == 'not changed' and node['type node'] == 'internal':
        path_to_change = path + node['name'] + '.'
        difference = plain(node['children'], path_to_change)
        return difference
    if node['status'] == 'added':
        path_to_change = path + node['name']
        change = create_change(node)
        return (
            f"Property '{path_to_change}' was added "
            f"with value: {change}\n"
        )
    if node['status'] == 'deleted':
        path_to_change = path + node['name']
        change = create_change(node)
        return "Property '{}' was removed\n".format(path_to_change)
    if node['status'] == 'before update':
        path_to_change = path + node['name']
        change = create_change(node)
        return (
            f"Property '{path_to_change}' was updated. "
            f"From {change} to "
        )
    if node['status'] == 'after update':
        change = create_change(node)
        return "{}\n".format(change)
    return ''


def create_change(dictionary):
    """Parses the node data. Returns it in the correct format as a string."""
    if dictionary['type node'] == 'internal':
        return '[complex value]'
    if dictionary['data'] is False:
        return 'false'
    elif dictionary['data'] is True:
        return 'true'
    elif dictionary['data'] is None:
        return 'null'
    else:
        return "'{}'".format(dictionary['data'])
