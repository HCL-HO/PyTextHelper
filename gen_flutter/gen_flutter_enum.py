import common as C


def replace_first_space_w_collen(txt: str):
    return txt.replace(' ', ';', 1)


source = C.get_text_from_file_in_str('source.txt')


def get_mtr_line_dict(txt: str):
    mtr_line_trunks = txt.split('-\n')

    mtr_lin_dict = {}

    for mtr_line_trunk in mtr_line_trunks:
        lines = mtr_line_trunk.split('\n')
        lines = [a for a in lines if a != '']
        mtr_lin_dict[replace_first_space_w_collen(lines[0])] = list(
            map(lambda x: replace_first_space_w_collen(x), lines[1:]))
    return mtr_lin_dict


def gen_enum_from_mtr_dict(dict: dict):
    enums = ''
    temp = "enum MTRLines { $temp final String name; final String code;final List<MTRStations> stations;const MTRLines(this.code, this.name, this.stations);"
    for k in dict.keys():
        station_list = [C.to_quoted_str(station.split(';')[0]) for station in dict[k]]
        station_list_str = "[" + ",".join(station_list) + "]"
        enums += k.split(';')[0].lower() + "(" + C.to_quoted_str(k.split(';')[0]) + ", " \
                 + C.to_quoted_str(k.split(';')[1]) \
                 + ", " + station_list_str + ")"
        enums += ",\n"

    temp = temp.replace('$temp', enums)
    return temp


def gen_station_enum_from_mtr_dict(dict: dict):
    enums = ''
    temp = "enum MTRStation {$temp final String name;final String code;const MTRStation(this.code, this.name);}"
    for stations in dict.values():
        for station in stations:
            station_name = C.to_quoted_str(station.split(';')[1])
            station_code = station.split(';')[0]

            enums += station_code.lower() + "(" + C.to_quoted_str(station_code) + ", " \
                     + station_name + ")"
            enums += ",\n"

    temp = temp.replace('$temp', enums)
    return temp


print(gen_enum_from_mtr_dict(get_mtr_line_dict(source)))
print(gen_station_enum_from_mtr_dict(get_mtr_line_dict(source)))
