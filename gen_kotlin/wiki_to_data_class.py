import common as Common

lines = Common.load_array_from_file('source.txt', '\n')

results = []
for line in lines:
    fields = line.split("	")
    try:
        field_name = fields[0].lstrip().rstrip()
        field_type = fields[1].lstrip().rstrip()
        mandatory = fields[2].lstrip().rstrip()
        nullable = '?' if mandatory != 'Y' else ''
        kotlin_field = f'val {field_name} : {field_type}{nullable},'
        results.append(kotlin_field)
    except:
        pass

print("\n".join(results))
