"""Dictionary format formater."""


def stylish(diff_list, level=0):
    """Converts a list of differences to dictionary format. Returns string."""
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    diff_list.sort(key=lambda x: x['name'])
    for node in diff_list:
        status = format_status(node)
        if has_children(node):
            result += indent + status + node['name'] + ': ' \
                + stylish(node['children'], level + 1) + '\n'
        else:
            data = format_data(node)
            result += indent + status + node['name'] + ': ' + data + '\n'
    result += indent[:-2] + '}\n' if level == 0 else indent[:-2] + '}'
    return result


def format_data(node):
    """Parses the node data. Returns it in the correct format as a string."""
    if node['data'] is False:
        return 'false'
    elif node['data'] is True:
        return 'true'
    elif node['data'] is None:
        return 'null'
    else:
        return str(node['data'])


def format_status(node):
    """Parses the node status. Returns it in the correct format as a string."""
    if node['status'] == 'not changed':
        return '  '
    elif node['status'] == 'deleted' or node['status'] == 'before update':
        return '- '
    elif node['status'] == 'added' or node['status'] == 'after update':
        return '+ '


def has_children(node):
    '''Checks if there are children in the node.'''
    if node['type node'] == 'internal':
        return True
    return False
