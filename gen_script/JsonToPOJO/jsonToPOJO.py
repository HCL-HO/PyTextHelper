import common
import json

source = common.get_text_from_file_in_str('source.txt')
sourceJson = json.loads(source)
output = ''

for key in sourceJson.keys():
    line = 'public ' + key + ': string = \"\", \n'
    output += line

print(output)