'''Flat format formater.'''


def plain(diff_list, path=''):
    """Converts a list of differences to flat format. Returns string."""
    result = ''
    diff_list.sort(key=lambda x: x['name'])
    for item in diff_list:
        if item['status'] == 'not changed' and item['type node'] == 'internal':
            path_to_change = path + item['name'] + '.'
            result += plain(item['children'], path_to_change)
        if item['status'] == 'added':
            path_to_change = path + item['name']
            change = create_change(item)
            result += (
                f"Property '{path_to_change}' was added "
                f"with value: {change}\n"
            )
        if item['status'] == 'deleted':
            path_to_change = path + item['name']
            change = create_change(item)
            result += "Property '{}' was removed\n".format(path_to_change)
        if item['status'] == 'before update':
            path_to_change = path + item['name']
            change = create_change(item)
            result += (
                f"Property '{path_to_change}' was updated. "
                f"From {change} to "
            )
        if item['status'] == 'after update':
            change = create_change(item)
            result += "{}\n".format(change)
    return result


def create_change(dictionary):
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
