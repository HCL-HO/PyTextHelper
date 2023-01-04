import common as Common

lines = Common.load_array_from_file('source.txt', '\n')
output = ''
for line in lines:
    res = line.rstrip().lstrip()
    res = res.replace("<string name=\"", "\"")
    res = res.replace("\">", "\":\"")
    res = res.replace("</string>", "\",")
    output += res + "\n"

print(output)

