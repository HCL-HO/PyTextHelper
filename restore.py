import os
from common import *


def restore_sql(sql):
    restore_sql_result = ''
    for x in sql:
        line = x.rstrip()
        line = line.rstrip().rstrip('+').rstrip().rstrip('"')
        line = line.lstrip().lstrip('+').lstrip().lstrip('"')
        restore_sql_result += line + '\n'
    pyperclip.copy(restore_sql_result)
    return restore_sql_result
    # print(line)


write_output(restore_sql(get_text_from_file('source.txt')))
