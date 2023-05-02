from common import *
import os
import shutil
import regex

source = get_text_from_file_in_str('source.txt')

pattern = r'<string name="(.*?)">'  # Pattern to match text between curly brackets
pattern2 = r'android:src="@drawable/(.*?)"'  # Pattern to match text between curly brackets
pattern3 = r'android:text="@string/(.*?)"'  # Pattern to match text between curly brackets
matches = regex.findall(pattern3, source, flags=regex.DOTALL)  # Find all matches in the text

path = "/Users/ericho/Documents/project/CCeP-JM-Mobile/android/app/src/main/res/drawable"
new_path = "/Users/ericho/Documents/icons"

for m in matches:
    # print(m)
    print(
        f'JobActionButtonData(key: Key("{m}"), imgPath: "{m}.svg", buttonLabel: S.current.{underscore_to_camelcase(m)}, hasActionPermission: ()=>true, onPressed: ()=> null),')
    # try:
    #     shutil.copy2(f'{path}/{m}.png', f'{new_path}/{m}.png')
    # except:
    #     pass
    # finally:
    #     pass
    # try:
    #     shutil.copy2(f'{path}/{m}.xml', f'{new_path}/{m}.xml')
    # except:
    #     pass
    # finally:
    #     pass
