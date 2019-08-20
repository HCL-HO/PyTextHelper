import calendar
from datetime import *

# TODO connect to API?

FORMAT = '%d-%b-%Y'
public_holiday = ['1-Jan-2019', '5-Feb-2019', '6-Feb-2019', '7-Feb-2019', '14-Feb-2019', '21-Mar-2019', '5-Apr-2019',
                  '19-Apr-2019', '20-Apr-2019', '21-Apr-2019', '22-Apr-2019', '1-May-2019', '12-May-2019',
                  '12-May-2019', '13-May-2019', '7-Jun-2019', '16-Jun-2019', '21-Jun-2019', '1-Jul-2019', '15-Aug-2019',
                  '13-Sep-2019', '14-Sep-2019', '23-Sep-2019', '25-Sep-2019', '1-Oct-2019', '7-Oct-2019', '31-Oct-2019',
                  '22-Dec-2019', '25-Dec-2019', '26-Dec-2019', '31-Dec-2019']


def get_datetime_public_holidays():
    array = []
    for s in public_holiday:
        this_date = datetime.strptime(s, FORMAT)
        array.append(this_date)
        # print(this_date.weekday())
    return array


def is_public_holiday(m_date: datetime):
    holidays = get_datetime_public_holidays()
    if m_date.weekday() in [5, 6]:
        return True
    elif m_date in holidays:
        return True
    else:
        return False


def get_next_working_date(m_date: datetime):
    nxt_date = datetime.today() + timedelta(days=1)
    while is_public_holiday(nxt_date):
        nxt_date = nxt_date + timedelta(days=1)
    return nxt_date


# def gen_dates():
#     x = ''
#     lines = get_text_from_file('source.txt')
#     for line in lines:
#         x += '\'' + line.replace('\n', '') + '-2019\','
#     print(x)
