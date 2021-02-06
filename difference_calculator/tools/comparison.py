"""Comparing flat files."""


def generate_diff(dict1, dict2):
    """Comparing two dictionary. Return difference in string."""
    result = []
    for key_dict1, value_dict1 in dict1.items():
        if key_dict1 in dict2:
            if dict2[key_dict1] == value_dict1:
                result.append('  {}: {}'.format(key_dict1, value_dict1))
            else:
                result.append('- {}: {}'.format(key_dict1, value_dict1))
                result.append('+ {}: {}'.format(key_dict1, dict2[key_dict1]))
        else:
            result.append('- {}: {}'.format(key_dict1, value_dict1))
    for key_dict2, value_dict2 in dict2.items():
        if key_dict2 not in dict1:
            result.append('+ {}: {}'.format(key_dict2, value_dict2))
    result = '{\n  ' + '\n  '.join(result) + '\n}\n'
    print(result)
    return result
