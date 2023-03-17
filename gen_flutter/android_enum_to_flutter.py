from common import *

import regex


# String? get
# name
# {
#     switch(this)
# {
#     case
# EquipmentOwner.HA:
# return "HA";
# }
# }


def get_class_name(txt):
    return find_between(txt, 'class', '(').lstrip().rstrip()


def get_val_enums_pairs(txt):
    lines = find_between(txt, '{', '}').split("\n")
    enums = []
    strings = []
    output = {}
    for e in lines:
        t = find_between(e, "", "(").lstrip().rstrip().lower()
        if t != "":
            enums.append(t)
        s = find_between(e, "(", ",").lstrip().rstrip()
        if s != "":
            strings.append(underscore_to_camelcase(s))

    for index in range(len(enums)):
        output[enums[index]] = strings[index]
    return output


def get_general_enums_pairs(txt):
    lines = find_between(txt, '{', '}').split("\n")
    enums = []
    list_of_fields = []
    output = {}
    for e in lines:
        t = find_between(e, "", "(").lstrip().rstrip().lower()
        if t != "":
            enums.append(t)
            # getting list of values
            s = find_between(e, "(", ")").lstrip().rstrip()
            values = s.split(",")
            fields = []
            for idx, x in enumerate(values):
                # print(x)
                if x != "":
                    x = x.lstrip().rstrip()
                    fields.append(
                        underscore_to_camelcase(x).replace("R.string.", "S.current.") if idx == len(values) - 1 else x)
            list_of_fields.append(fields)
    for index in range(len(enums)):
        output[enums[index]] = list_of_fields[index]
    return output


def get_enum_fields_name(txt):
    pattern = r'\((.*?)\)'  # Pattern to match text between curly brackets
    pattern2 = r'val(.*?): '  # Pattern to match text between curly brackets
    matches = regex.findall(pattern, txt, flags=regex.DOTALL)  # Find all matches in the text
    result_fields = []
    if len(matches) > 0:
        result_fields = regex.findall(pattern2, matches[0], flags=regex.DOTALL)
        result_fields = [a.lstrip().rstrip() for a in result_fields]
    return result_fields


def get_res_enums_pairs(txt):
    lines = find_between(txt, '{', '}').split("\n")
    enums = []
    strings = []
    output = {}
    for e in lines:
        t = find_between(e, "", "(").lstrip().rstrip().lower()
        if t != "":
            enums.append(t)
    for e in lines:
        s = find_between(e, "R.string.", ")").lstrip().rstrip()
        if s != "":
            strings.append(underscore_to_camelcase(s))

    for index in range(len(enums)):
        output[enums[index]] = strings[index]
    return output


def gen_flutter_res_enum_extension(txt, className):
    output = "extension " + className + "Extension on " + className + "{\n" \
             + "  String? get name {\n" + "    switch (this) {\n"
    for e in txt:
        output += "case " + className + "." + e + ":\n"
        output += "return S.current." + txt[e] + ";\n"

    output += "}\n}\n}\n"
    return output


def gen_flutter_general_enum_extensions(map, fieldNames, className):
    output = "extension " + className + "Extension on " + className + "{\n"
    for idx, field_name in enumerate(fieldNames):
        output += "  String? get " + field_name + " {\n" + "    switch (this) {\n"
        for e in map:
            output += "case " + className + "." + e + ":\n"
            output += "return " + map[e][idx] + ";\n"

        output += "}\n}\n"
    return output + "}\n"


def gen_flutter_val_enum_extension(txt, className):
    output = "extension " + className + "Extension on " + className + "{\n" \
             + "  String? get rawValue {\n" + "    switch (this) {\n"
    for e in txt:
        output += "case " + className + "." + e + ":\n"
        output += "return " + txt[e] + ";\n"

    output += "}\n}\n}\n"
    return output


def gen_flutter_enum(resEnum, valEnum, className):
    output = "enum " + className + "{\n"
    for e in resEnum:
        output += f"@JsonValue({valEnum[e]})\n"
        output += e + ",\n"
    return output + "}"


def gen_simple_enum(source):
    className = get_class_name(source)
    resEnumMap = get_res_enums_pairs(source)
    valEnumMap = get_val_enums_pairs(source)
    print(gen_flutter_enum(resEnumMap, valEnumMap, className))
    print(gen_flutter_res_enum_extension(resEnumMap, className))


def gen_multifields_enum(source):
    className = get_class_name(source)
    genEnumMap = get_general_enums_pairs(source)
    fields = get_enum_fields_name(source)
    print(fields)
    print(genEnumMap)
    print(gen_flutter_general_enum_extensions(genEnumMap, fields, className))


source = get_text_from_file_in_str('source.txt')
gen_multifields_enum(source)
# def search_brackets(text):
#     pattern = r'\{(.*?)\}'  # Pattern to match text between curly brackets
#     matches = regex.findall(pattern, text, flags=regex.DOTALL)  # Find all matches in the text
#     fields = matches[0]
#     pattern2 = r'(.*?)\('  # Pattern to match text between curly brackets
#     matches = regex.findall(pattern2, fields, flags=regex.DOTALL)  # Find all matches in the text
#     return matches
#
#
# print(search_brackets(source))
