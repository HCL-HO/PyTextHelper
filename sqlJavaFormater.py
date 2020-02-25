from common import *


def make_java_sql(sql):
    make_java_sql_result = ''
    for i in range(len(sql)):
        line = sql[i]
        if line.rstrip() is not '':
            line = line.rstrip().rstrip(';')
            # line = line.lstrip()
            line = '" ' + line + ' "'
            if i is not len(sql) - 1:
                line += ' + \n'
            else:
                line += ';'
            make_java_sql_result += line
    pyperclip.copy(make_java_sql_result)
    return make_java_sql_result


write_output(make_java_sql(get_text_from_file('source.txt')))
