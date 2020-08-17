import csv
import common

csv_file_path = 'C:\\workspace\\E-cert\\update_e-cert_services_fee\\e-cert price (as at 2019-11-13)-CAM.csv'

CODE_EFF_DATE = 'TEMP_EFF_DATE'
CODE_PROMO_PRICE = 'TEMP_PROM_PRICE'
CODE_DESC_E = 'TEMP_DESC_E'

eff_date = 'TO_DATE(\'2020/01/01\', \'yyyy/mm/dd\')'
# eff_date = 'TO_DATE(\'2019/12/17\', \'yyyy/mm/dd\')'
template = common.get_text_from_file_in_str('template.txt')
output = []

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            promo_price = row[len(row) - 1]
            eng_desc = row[0]
            sql = template.replace(CODE_EFF_DATE, eff_date). \
                replace(CODE_PROMO_PRICE, promo_price).replace(CODE_DESC_E, eng_desc)
            output.append('--********************* ' + eng_desc + '*********************\n\n ' + sql)
            line_count += 1
            print(f'{CODE_DESC_E} : {eng_desc}')
            print(f'{CODE_PROMO_PRICE} : {promo_price}')
    print(line_count)

    common.write_output_to_file('\n'.join(output), 'C:\\workspace\\E-cert\\update_e-cert_services_fee\\update_e-cert_fee.sql')
