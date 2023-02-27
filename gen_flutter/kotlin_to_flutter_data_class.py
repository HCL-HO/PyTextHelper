import common as C


def get_kotlin_data_class_name(source):
    return C.find_between(source, "class", "(").lstrip().rstrip()


def replace_with_dart_type(data_type):
    return {
        "Int": "int",
        'Boolean': 'bool',
    }.get(data_type, data_type)


def get_kotlin_data_class_dict(source):
    fields = C.find_between(source, "(", ")").lstrip().rstrip().split("\n")
    fields = [a.lstrip().rstrip() for a in fields]
    result = {}
    for field in fields:
        field_name = C.find_between(field, " ", ":")
        data_type = C.find_between(field, ": ", ",")
        data_type = replace_with_dart_type(data_type)
        result[field_name] = data_type
    return result


def gen_dto_w_keys(name: str, fields_dict: dict):
    temp = "@freezed\nclass $name with _$$name {  const factory $name({ $temp }) = _$name; \n" \
           "factory $name.fromJson(Map<String, Object?> json) => _$$nameFromJson(json);}"
    content = ''
    for k in fields_dict.keys():
        content += fields_dict[k] + "? " + k + ",\n"

    temp = temp.replace('$name', name)
    temp = temp.replace("$temp", content)
    return temp


data = C.get_text_from_file_in_str('source.txt')
class_name = get_kotlin_data_class_name(data)
kotlin_dict = get_kotlin_data_class_dict(data)

print(gen_dto_w_keys(class_name, kotlin_dict))
