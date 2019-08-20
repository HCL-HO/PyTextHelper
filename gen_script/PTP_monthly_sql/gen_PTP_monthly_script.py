import calendar
import datetime

from common import *

#      replace start date and end date
#      to generate sql for each moth
#

# Basic config
MERCHANT_CODE = 10
RANGE = ['201807', '201906']
DATE_FORMAT = "%d-%m-%Y"
TEMPLATE = "PTP_Traffic.sql"
SEPERATOR = '\n*****************************************************************************************************************************\n'

START_DATE_REPLACE = ":pFromDate"
END_DATE_REPLACE = ":pToDate"
MERCHANT_CODE_REPLACE = ':pMerhCode'


def get_start_date(year, month):
    x = datetime.date(year, month, 1)
    return '\'' + x.strftime(DATE_FORMAT) + '\''


def get_end_date(year, month):
    date_range = calendar.monthrange(year, month)
    x = datetime.datetime(year, month, date_range[1])
    return '\'' + x.strftime(DATE_FORMAT) + '\''


def get_monthly_date_pairs(time_frame):
    pair = []
    start_year = int(time_frame[0][:4])
    end_year = int(time_frame[1][:4])
    start_month = int(time_frame[0][4:])
    end_month = int(time_frame[0][4:])

    for year in range(start_year, end_year + 1):
        m_start_month = start_month if year == start_year else 1
        m_end_month = end_month if year == end_year else 12
        for month in range(m_start_month, m_end_month + 1):
            pair.append([get_start_date(year, month), get_end_date(year, month)])
    return pair


def gen_script(merchant, time_frame, template_path):
    script = ''
    template = get_text_from_file_in_str(template_path).replace(MERCHANT_CODE_REPLACE, str(merchant))
    dates = get_monthly_date_pairs(time_frame)
    for pair in dates:
        m_script = template.replace(START_DATE_REPLACE, pair[0]).replace(END_DATE_REPLACE, pair[1])
        write_output_to_file(m_script, 'out_' + pair[0].replace('\'', '') + '_' + pair[1].replace('\'', ''))
    print(script)


gen_script(MERCHANT_CODE, RANGE, TEMPLATE)
