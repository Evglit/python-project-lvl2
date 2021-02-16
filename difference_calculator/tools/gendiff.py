"""Comparing flat files."""


def generate_diff(dict1, dict2):
    str_data(dict1)
    str_data(dict2)
    result = {}
    common_keys = list(dict1.keys() & dict2.keys())
    added_keys = list(dict2.keys() - dict1.keys())
    deleted_keys = list(dict1.keys() - dict2.keys())
    for key in common_keys:
        if dict1[key] == dict2[key]:
            result['  ' + key] = dict1[key]
        else:
            if type(dict1[key]) is dict and type(dict2[key]) is dict:
                result['  ' + key] = generate_diff(dict1[key], dict2[key])
            else:
                result['- ' + key] = dict1[key]
                result['+ ' + key] = dict2[key]
    for key in added_keys:
        result['+ ' + key] = dict2[key]
    for key in deleted_keys:
        result['- ' + key] = dict1[key]
    return result


def str_data(dictionary):
    for key in dictionary.keys():
        if type(dictionary[key]) is dict:
            str_data(dictionary[key])
        elif dictionary[key] is True:
            dictionary[key] = 'true'
        elif dictionary[key] is False:
            dictionary[key] = 'false'
        elif dictionary[key] is None:
            dictionary[key] = 'null'


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
