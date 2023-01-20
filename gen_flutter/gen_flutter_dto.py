import common as C
import json

source = C.get_text_from_file_in_str('mtr_response.txt')


def gen_dto(name: str, source: str):
    source_json = json.loads(source)
    return gen_dto_w_keys(name, dict(source_json).keys())


def gen_dto_w_keys(name: str, keys: []):
    temp = "@freezed\nclass $name with _$$name {  const factory $name({ $temp }) = _$name; \n" \
           "factory $name.fromJson(Map<String, Object?> json) => _$$nameFromJson(json);}"
    content = ''
    for k in keys:
        content += "String? " + k + ",\n"

    temp = temp.replace('$name', name)
    temp = temp.replace("$temp", content)
    return temp


print(gen_dto("MTRScheduleResp", source))
