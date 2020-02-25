from typing import List

import common as Common

indent = '    '
indent_increment = '  '


def get_params(keys):
    result = ''
    for key in keys:
        result += key + ': str, '
    return result[:-2]


def get_content(keys):
    result = ''
    for key in keys:
        result += indent + indent_increment + 'self.' + key + ' = ' + key + '\n'
    return result


def get_class_str(class_name: str):
    keys = Common.load_array_from_file('keys.txt', '\n')
    result = ''
    result += 'class '
    result += class_name + ' :' + '\n'
    result += indent + 'def __init__(self, params):\n' + get_content(keys)
    result = result.replace('params', get_params(keys))
    result += get_static_create_method(class_name, keys)
    Common.write_output(result)
    return result


def get_static_create_method(class_name: str, keys: List):
    result = '\n\n'
    result += 'def get_' + class_name.lower() + '(params) -> ' + class_name + ':\n'
    result += indent
    result += 'return ' + class_name + '('
    for key in keys:
        result += 'params[\'' + key + '\'], '
    result = result[:-2]
    result += ')'
    return result


get_class_str('Feed')
