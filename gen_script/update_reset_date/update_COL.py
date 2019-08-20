from datetime import *

from common import *
from dateU import get_next_working_date


def update_sql():
    path = 'P:\\ISSD.ESD.IPSS\\Staff Communication\\Training\\Reset Script\\Reset Script for COL PIC (SPT HUB)\\00_Reset_Run.sql'
    lines = get_text_from_file(path)
    result = ''
    for line in lines:
        if 'collDate' in line:
            line = 'define collDate = \'' + datetime.strftime(get_next_working_date(datetime.today()),
                                                              "%Y-%m-%d") + '\'' + '\n'
        result += line
    write_output_to_file(result, path)
