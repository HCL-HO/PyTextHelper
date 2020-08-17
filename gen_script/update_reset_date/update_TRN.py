from common import *
from datetime import *


def update_sql():
    path = 'P:\\ISSD.ESD.IPSS\\Staff Communication\\Training\\Reset Script\\00TRN_Reset_Run.sql'
    lines = get_text_from_file(path)
    result = ''
    for line in lines:
        if 'traningDate' in line:
            # line = 'define traningDate = \'' + datetime.strftime(get_next_working_date(datetime.today()),
            #                                                      "%Y-%m-%d") + '\'' + '\n'
            line = 'define traningDate = \'' + datetime.strftime(datetime.today(),
                                                                 "%Y-%m-%d") + '\'' + '\n'
        result += line
    write_output_to_file(result, path)
