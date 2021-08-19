import requests
from crawler_function import get_stock_numbers, get_balance_sheet, get_income_statement, send_request
from file_function import save_datas, read_datas
from bs4 import BeautifulSoup
import time
import json


number_list = read_datas('number', 'stock_number.txt')

number_list = number_list[0].split('\n')

for number in number_list:
    income_statement_20211 = get_income_statement(f'https://pchome.megatime.com.tw/stock/sto2/ock1/20211/sid{number}.html')
    print(income_statement_20211)
    print('-----------------------')
    save_datas(income_statement_20211, str(number), 'income_statement_20211.json')
    time.sleep(2)

print('Done!')
# datas = get_income_statement('https://pchome.megatime.com.tw/stock/sto2/ock1/sid2388.html')

# print(datas)
