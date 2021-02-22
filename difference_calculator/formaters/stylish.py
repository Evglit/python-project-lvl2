"""Dictionary format formater."""


def stylish(diff_list, level=0):
    """Converts a list of differences to dictionary format. Returns string."""
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    diff_list.sort(key=lambda x: x['name'])
    for item in diff_list:
        if item['status'] == 'not changed':
            status = '  '
        elif item['status'] == 'deleted' or item['status'] == 'before update':
            status = '- '
        elif item['status'] == 'added' or item['status'] == 'after update':
            status = '+ '
        if item['type node'] == 'internal':
            result += indent + status + item['name'] + ': ' \
                + stylish(item['children'], level + 1) + '\n'
        else:
            if item['data'] is False:
                data = 'false'
            elif item['data'] is True:
                data = 'true'
            elif item['data'] is None:
                data = 'null'
            else:
                data = str(item['data'])
            result += indent + status + item['name'] + ': ' + data + '\n'
    result += indent[:-2] + '}\n' if level == 0 else indent[:-2] + '}'
    return result
