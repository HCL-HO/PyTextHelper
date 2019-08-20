import common as Common

indent = '    '
indent_increment = '  '


def get_params(keys):
    result = ''
    for key in keys:
        result += key + ': str, '
    print(result)
    print(result[:-2])
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
    Common.write_output(result)
    return result


get_class_str('Feed')
