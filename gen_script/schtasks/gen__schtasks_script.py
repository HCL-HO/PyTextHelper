from common import *

# Basic config
DELIMINATOR = "\n"
COMPUTERS_FILE = "computers.txt"
TEMPLATE = "schtasks_template.txt"
REPLACE = "COMPUTER_NAME_HERE"

# Sensitive
ADMIN = ""
PASSWORD = ""
ADMIN_REPLACE = "ADMIN_USER"
PASSWORD_REPLACE = "PASSWORD"

computers_list = load_array_from_file(COMPUTERS_FILE, DELIMINATOR)
template = get_text_from_file_in_str(TEMPLATE)
print(computers_list)
result = ''
for computer in computers_list:
    command = template.replace(REPLACE, computer).replace(ADMIN_REPLACE, ADMIN).replace(PASSWORD_REPLACE, PASSWORD)
    result += command + "\n"

write_output_to_file(result, "script.bat")
