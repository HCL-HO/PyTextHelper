from common import *


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


def get_enums_pairs(txt):
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


def gen_flutter_enum_extension(txt, className):
    output = "extension " + className + "Extension on " + className + "{\n" \
             + "  String? get name {\n" + "    switch (this) {\n"
    for e in txt:
        output += "case " + className + "." + e + ":\n"
        output += "return S.current." + txt[e] + ";\n"

    output += "}\n}\n}\n"
    return output


def gen_flutter_enum(txt, className):
    output = "enum " + className + "{\n"
    for e in txt:
        output += e + ",\n"
    return output + "}"


source = get_text_from_file_in_str('../tasks/source.txt')
className = get_class_name(source)
enumMap = get_enums_pairs(source)
print(gen_flutter_enum(enumMap, className))
print(gen_flutter_enum_extension(enumMap, className))
