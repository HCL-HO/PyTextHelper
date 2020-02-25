from _ctypes import Array

from common import *


def replace_with_multiple(keyword: str, replacements: Array, source: str):
    for replacement in replacements:
        replacement = replacement.rstrip().lstrip()
        source = source.replace(keyword, replacement, 1)
    return source


def replace_multiple_with(keywords: Array, replacement: str, source: str):
    for keyword in keywords:
        keyword = keyword.rstrip('\n')
        source = source.replace(keyword, replacement)
    return source


def read_and_replace(path: str, keyword, replacement):
    text = get_text_from_file_in_str(path)
    result = text.replace(keyword, replacement)
    return result


# print(read_and_replace('../source.txt', '\n', ' '))
