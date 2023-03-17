def convert_enum(kotlin_enum):
    # Split the Kotlin enum into its values
    values = kotlin_enum.split(", ")

    # Convert each value to a Flutter enum value
    flutter_enum_values = []
    for value in values:
        name = value.split("(")[0].strip()  # Remove any arguments
        flutter_enum_value = "  " + name.lower() + ",\n"  # Convert name to lowercase
        flutter_enum_values.append(flutter_enum_value)

    # Combine the Flutter enum values into a single string
    flutter_enum = "enum " + kotlin_enum.split(".")[0] + " {\n"
    for value in flutter_enum_values:
        flutter_enum += value
    flutter_enum += "}\n"

    return flutter_enum

# Example usage
kotlin_enum = """
    enum class Color(val rgb: Int) {
        RED(0xFF0000),
        GREEN(0x00FF00),
        BLUE(0x0000FF)
    }
"""
flutter_enum = convert_enum(kotlin_enum)
print(flutter_enum)
