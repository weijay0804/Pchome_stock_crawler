from crawler_function import get_stock_numbers, get_balance_sheet
from file_function import save_datas

data = get_balance_sheet('https://pchome.megatime.com.tw/stock/sto2/ock0/sid2303.html')

save_datas(data, 'balance_sheet')

print(data)



    