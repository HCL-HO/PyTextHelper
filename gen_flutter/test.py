from common import *
import os
import shutil
import regex

source = get_text_from_file_in_str('source.txt')

pattern = r'job.add\((.*?)\)\)'  # Pattern to match text between curly brackets
pattern2 = r'\(listOf\((.*?)\),\)'  # Pattern to match text between curly brackets
pattern3 = r'android:text="@string/(.*?)"'  # Pattern to match text between curly brackets
matches = regex.findall(pattern, source, flags=regex.DOTALL)  # Find all matches in the text

path = "/Users/ericho/Documents/project/CCeP-JM-Mobile/android/app/src/main/res/drawable"
new_path = "/Users/ericho/Documents/icons"

objs = []
for m in matches:
    # print(m)
    # objs.append(m.replace(" ", "").split(","))
    new_line = m
    new_line = new_line.replace("JobEnum.", "")
    new_line = new_line.replace("CM_JOB", "cm_job")
    new_line = new_line.replace("PM_JOB", "pm_job")
    new_line = new_line.replace("area.", "Area.")
    new_line = new_line.replace("HandlingPartyEnum.", "HandlingParty.")
    new_line = new_line.replace("case.", "Case.")
    new_line = new_line.replace("NON_PMSMC", "nonPmsmc")
    new_line = new_line.replace("IN_HOUSE", "inhouse")
    new_line = new_line.replace("PMSMC", "pmsmc")
    print(new_line + "),")
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

# for o in objs:
    # new_line = f"MatObject(mat: {o[0]}, area: {o[1].lower()}, mCase: {o[2].replace('listOf(', '[').replace(')', ']')}," \
    #            f" handlingParty: {','.join(o[3:]).replace('listOf(', '[').lower() + '])' if len(o) >= 4 else 'null'} ),"
    # new_line = new_line.replace("JobEnum.", "")
    # new_line = new_line.replace("jobenum.", "")
    # new_line = new_line.replace("area.", "Area.")
    # new_line = new_line.replace("handlingpartyenum.", "HandlingParty.")
    # new_line = new_line.replace("case.", "Case.")
    # new_line = new_line.replace("non_pmsmc", "nonPmsmc")
    # new_line = new_line.replace("in_house", "inhouse")
    # print(o)
# print(objs)
