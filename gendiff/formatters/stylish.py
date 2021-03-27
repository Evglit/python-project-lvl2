"""Dictionary format formater."""


def stylish(diff_list, level=0):
    """Converts a list of differences to dictionary format. Returns string."""
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    diff_list.sort(key=lambda x: x['name'])
    for node in diff_list:
        status = format_status(node['status'])
        if node['status'] == 'nested':
            data = stylish(node['children'], level + 1)
            result += indent + status + node['name'] + ': ' + data + '\n'
        elif node['status'] == 'changed':
            data = format_data(node['data before'], indent)
            result += indent + '- ' + node['name'] + ': ' + data + '\n'
            data = format_data(node['data after'], indent)
            result += indent + '+ ' + node['name'] + ': ' + data + '\n'
        else:
            data = format_data(node['data'], indent)
            result += indent + status + node['name'] + ': ' + data + '\n'
    result += indent[:-2] + '}'
    return result


def format_data(data, indent=None):
    """Parses the data. Returns it in the correct format as a string."""
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            if type(data[key]) is dict:
                value = format_data(data[key], indent)
                result += indent + '  ' + key + ': ' + value + '\n'
            else:
                value = format_data(data[key])
                result += indent + '  ' + key + ': ' + value + '\n'
        result += indent[:-2] + '}'
        return result
    if data is False:
        return 'false'
    elif data is True:
        return 'true'
    elif data is None:
        return 'null'
    else:
        return str(data)


def format_status(status):
    """Parses the node status. Returns it in the correct format as a string."""
    if status == 'not changed' or status == 'nested':
        return '  '
    elif status == 'deleted':
        return '- '
    elif status == 'added':
        return '+ '
