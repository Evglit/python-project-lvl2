"""Dictionary format formater."""


def stylish(diff_list, level=0):
    """Converts a list of differences to dictionary format. Returns string."""
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    diff_list.sort(key=lambda x: x['name'])
    for node in diff_list:
        if node['status'] == 'changed':
            data = format_data(node['data before'], indent)
            result += indent + '- ' + node['name'] + ': ' + data + '\n'
            data = format_data(node['data after'], indent)
            result += indent + '+ ' + node['name'] + ': ' + data + '\n'
        else:
            status = format_status(node['status'])
            if node['status'] == 'nested':
                data = stylish(node['children'], level + 1)
            else:
                data = format_data(node['data'], indent)
            result += indent + status + node['name'] + ': ' + data + '\n'
    result += indent[:-2] + '}'
    return result


def format_data(data, indent):
    """Parses the data. Returns it in the correct format as a string."""
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += indent + '  ' + key + ': ' + value + '\n'
        result += indent[:-2] + '}'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    else:
        result = str(data)
    return result


def format_status(status):
    """Parses the node status. Returns it in the correct format as a string."""
    if status == 'not changed' or status == 'nested':
        return '  '
    elif status == 'deleted':
        return '- '
    elif status == 'added':
        return '+ '
