kotlin_data_class = """
data class MyDataClass(val property1: String, val property2: Int)
"""

# Parse the Kotlin data class to extract its properties
kotlin_data_class = kotlin_data_class.strip().split("\n")[0].replace("data class ", "")
kotlin_properties = kotlin_data_class[kotlin_data_class.index("(")+1:kotlin_data_class.index(")")].split(", ")
kotlin_property_names = [prop.split(": ")[0] for prop in kotlin_properties]
kotlin_property_types = [prop.split(": ")[1] for prop in kotlin_properties]

# Create the Flutter data class
flutter_data_class = "import 'package:json_annotation/json_annotation.dart';\n\n"
flutter_data_class += "@JsonSerializable()\n"
flutter_data_class += "class {} {{\n".format(kotlin_data_class.split("(")[0])
for i, prop_name in enumerate(kotlin_property_names):
    prop_type = kotlin_property_types[i]
    if prop_type == "Int":
        prop_type = "int"
    flutter_data_class += f"  final {prop_type} {prop_name};\n"
flutter_data_class += "\n"
flutter_data_class += f"  {kotlin_data_class.split('(')[0]}({', '.join([f'required this.{prop_name}' for prop_name in kotlin_property_names])});\n\n"
flutter_data_class += "  factory {} .fromJson(Map<String, dynamic> json) => _${}.FromJson(json);\n\n".format(kotlin_data_class.split("(")[0], kotlin_data_class.split("(")[0])
flutter_data_class += "  Map<String, dynamic> toJson() => _${}.ToJson(this);\n".format(kotlin_data_class.split("(")[0])
flutter_data_class += "}"

# Print the Flutter data class
print(flutter_data_class)
