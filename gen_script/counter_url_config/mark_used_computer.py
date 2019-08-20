from common import *

USED_COMPUTER_FILE = 'computers.txt'


def replace_multiple(path: str, replace_with: str):
    result = ''
    text = get_text_from_file(path)
    keywords_array = get_text_from_file(USED_COMPUTER_FILE)
    for line in text:
        for keyword in keywords_array:
            keyword = keyword.rstrip('\n')
            line = line.replace(keyword, replace_with)
        result += line
    write_output(result)


replace_multiple('C:\\Users\\eric_cl_ho\\Desktop\\URL to PRD counter.bat', 'USED_BO')
