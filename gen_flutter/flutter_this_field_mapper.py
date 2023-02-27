import common as Common

lines = Common.load_array_from_file('source.txt', '\n')

results = []
for line in lines:
    fields = line.split(" ")
    field_name = fields[0]

print("\n".join(results))