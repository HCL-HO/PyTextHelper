import common as Common

lines = Common.load_array_from_file('source.txt', '\n')


def replace_android_res_string(arr):
    output = []
    for line in arr:
        res = line.rstrip().lstrip()
        res = res.replace("<string name=\"", "\"")
        res = res.replace("\">", "\":\"")
        res = res.replace("</string>", "\",")
        output.append(res)
    return output


def under_score_to_camel(input_lines):
    new_output = ''
    for line in input_lines:
        print(Common.underscore_to_camelcase(line))
        # new_line = ""
        # parts = line.split(":")
        # field_name = parts[0].replace("\"", "")
        # field_name_parts = field_name.split("_")
        # value = parts[1]
        # for i in range(len(field_name_parts)):
        #     if i > 0:
        #         new_line += field_name_parts[i][0].capitalize() + field_name_parts[i][0:]
        # new_output += f"\"${new_line}\":${value}"
        # print(new_line)
    return new_output


replaced_string_arr = replace_android_res_string(lines)
print(under_score_to_camel(replaced_string_arr))
