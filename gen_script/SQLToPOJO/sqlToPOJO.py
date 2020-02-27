from common import *

source = get_text_from_file_in_str('source.txt')
paramsStr = source.split('select ')[1].split('from')[0]
params = paramsStr.split(',')


def getFieldFromSQL(params):
    for param in params:
        # print(param)
        if param.lower().find('to_char(') >= 0:
            params.remove(param)

    for index in range(len(params)):
        if params[index].find(' as ') >= 0:
            params[index] = params[index].split(' as ')[1]
        params[index] = params[index].lower().replace('\n', '').lstrip().rstrip()
        removedtable = params[index].split('.')
        if len(removedtable) > 1:
            params[index] = removedtable[1]
    return params


def getVOClassFields(params):
    result = ''
    outParams = []
    for field in params:
        output = ''
        field_split = field.split('_')
        if len(field_split) > 1:
            for i in range(len(field_split)):
                if i == 0:
                    output += field_split[0]
                else:
                    output += field_split[i][:1].upper() + field_split[i][1:]
        else:
            output = field
        outParams.append(output)
        result += 'public String ' + output + ';\n'

    print('Public String')
    print(result)
    return outParams


def printMapperCode(classFields, tableFields):
    result = ''
    for i in range(len(classFields)):
        field = classFields[i]
        tableField = tableFields[i]
        result += 'vo.set' + field[:1].upper() + field[1:] + '(rs.getString("' + tableField.upper() + '"));\n'
    result += 'return vo;';
    print(result)


fields = getFieldFromSQL(params)
classFields = getVOClassFields(fields)
printMapperCode(classFields, fields)
print('\n Mapper')

# result = ''
# for field in params:
#     result += vo.set
# print()
