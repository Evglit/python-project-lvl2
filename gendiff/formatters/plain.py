'''Flat format formater.'''


def plain(diff_list):
    """Converts a list of differences to flat format. Returns string."""
    result = ''
    diff_list.sort(key=lambda x: x['name'])
    result = get_diff_plain_list(diff_list)
    return '\n'.join(result)


def get_diff_plain_list(diff_list, path=''):
    """Analysis of the nodes. Returns a list with changes."""
    plain_list = []
    intermediate_result = ''
    for node in diff_list:
        if node['status'] == 'not changed' and node['type node'] == 'internal':
            path_to_change = path + node['name'] + '.'
            difference = get_diff_plain_list(node['children'], path_to_change)
            plain_list.extend(difference)
        if node['status'] == 'added':
            path_to_change = path + node['name']
            change = create_change(node)
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            plain_list.append(difference)
        if node['status'] == 'deleted':
            path_to_change = path + node['name']
            change = create_change(node)
            difference = "Property '{}' was removed".format(path_to_change)
            plain_list.append(difference)
        if node['status'] == 'before update':
            path_to_change = path + node['name']
            change = create_change(node)
            intermediate_result = (
                f"Property '{path_to_change}' was updated. "
                f"From {change} to "
            )
            continue
        if node['status'] == 'after update':
            change = create_change(node)
            difference = intermediate_result + "{}".format(change)
            plain_list.append(difference)
            intermediate_result = ''
    return plain_list


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
    if type(dictionary['data']) is str:
        return "'{}'".format(dictionary['data'])
    else:
        return '{}'.format(dictionary['data'])
