import re
from typing import get_args
with open('chek.txt','r',encoding='utf-8') as ch:
    all_lines = ''.join(ch.readlines())
company_name = re.search(r'ДУБЛИКАТ\n(.+)\n',all_lines).group(1)
bin_number = re.search(r'БИН (\d+)',all_lines).group(1)

items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)',all_lines)

date = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}',all_lines).group(0)
address = re.search(r'г\.([^\n]+)',all_lines).group(0)
total_sum = re.search(r'ИТОГО:\n([^\n]+)',all_lines).group(1)

print(f'Company name: {company_name}')
print(f'BIN number: {bin_number}')
print("All products: ")

def prettify(s):
    s = s.replace(' ', '')
    s = s.replace(',', '.')
    return float(s)

check_sum = 0

for ind, item in enumerate(items):
    print(f'{ind+1}) Product name: {item[0]}')
    print(f'\t{item[1]} * {item[2]} = {item[3]}')
    check_sum+=prettify(item[3])

print(f'Overall sum: {check_sum}')
print(f'Total sum: {total_sum}')
print(f'Date: {date}')
print(f'Address: {address}')


# CSV

import csv
#Russian Windows features:
csv.excel.delimiter = ';'
csv.excel.lineterminator = '\n'
# comma separated value

#Writing to Csv
with open('File.csv','w',encoding='cp1251') as f:
    writer = csv.writer(f,csv.excel)
    writer.writerow([f'Company name: {company_name}'])
    writer.writerow([f'BIN number: {bin_number}'])
    writer.writerows([('Name','Quantity','Price','Sum')]+ (items))
    writer.writerow([f'Date: {date}',f'Address: {address}'])
#Reading from CSV
with open('File.csv','r',encoding='cp1251') as f:
    for line in  csv.reader(f, csv.excel):
        #print(line)
        pass