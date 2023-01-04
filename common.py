from typing import List

# import pyperclip


def get_text_from_file(path) -> List[str]:
    f = open(path, "r")
    sql = f.readlines()
    return sql


def get_text_from_file_in_str(path) -> str:
    return "".join(str(x) for x in get_text_from_file(path))


def write_output(result):
    write_output_to_file(result, "output.txt")


def write_output_to_file(result, file):
    print(result + "\n")
    output = open(file, "w+")
    output.write(result)
    output.close()


def load_array_from_file(file, deliminator) -> List[str]:
    return get_text_from_file_in_str(file).split(deliminator)


def to_quoted_str(txt):
    return "\"" + txt + "\""
