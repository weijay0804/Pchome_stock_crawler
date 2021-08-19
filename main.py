from crawler_function import get_stock_numbers, get_balance_sheet, get_income_statement
from file_function import save_datas, read_datas
import time


number_list = read_datas('number', 'stock_number')

number_list = number_list[0].split('\n') 

for number in number_list:
    sheet = get_income_statement(f'https://pchome.megatime.com.tw/stock/sto2/ock1/sid{number}.html')
    save_datas(sheet, str(number), 'income_statement')
    print(sheet)
    time.sleep(2)
