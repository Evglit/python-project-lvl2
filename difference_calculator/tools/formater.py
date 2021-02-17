"""Formaters for diff"""


def stylish(dictionary, level=0):
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    keys = list(dictionary.keys())
    if keys[0][0] != '+' and keys[0][0] != '-' and keys[0][0] != ' ':
        keys.sort()
    else:
        keys.sort(key=lambda x: x[2:])
    for key in keys:
        if type(dictionary[key]) is dict:
            if key[:2] != '+ ' and key[:2] != '- ' and key[:2] != '  ':
                prefix = indent + '  ' + key + ': '
                result += prefix + stylish(dictionary[key], level + 1) + '\n'
            else:
                prefix = indent + key + ': '
                result += prefix + stylish(dictionary[key], level + 1) + '\n'
        else:
            if key[:2] != '+ ' and key[:2] != '- ' and key[:2] != '  ':
                prefix = indent + '  ' + key + ': '
                result += prefix + str(dictionary[key]) + '\n'
            else:
                prefix = indent + key + ': '
                result += prefix + str(dictionary[key]) + '\n'
    result += indent[:-2] + '}\n' if level == 0 else indent[:-2] + '}'
    return result
