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
            change = '[complex value]' if item['type node'] == 'internal' else transform_change(item['data'])
            result += "Property '{}' was added with value: {}\n".format(path_to_change, change)
        if item['status'] == 'deleted':
            path_to_change = path + item['name']
            change = '[complex value]' if item['type node'] == 'internal' else transform_change(item['data'])
            result += "Property '{}' was removed\n".format(path_to_change)
        if item['status'] == 'before update':
            path_to_change = path + item['name']
            change = '[complex value]' if item['type node'] == 'internal' else transform_change(item['data'])
            result += "Property '{}' was updated. From {} to ".format(path_to_change, change)
        if item['status'] == 'after update':
            change = '[complex value]' if item['type node'] == 'internal' else transform_change(item['data'])
            result += "{}\n".format(change)
    return result


def transform_change(change):
    if change is False:
        return 'false'
    elif change is True:
        return 'true'
    elif change is None:
        return 'null'
    else:
        return "'{}'".format(change)
