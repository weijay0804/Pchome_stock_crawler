import time

# --- 自訂函式 ---
from crawler_function import get_balance_sheet, get_income_statement
from file_function import save_datas, read_datas
from export_to_excel import export_income_to_excel




def income(seasion : str) -> None:
    ''' 取得 損益表資料 並存成 json 文件 (seasion = 20212 or 20211) '''

    number_list = read_datas('number', 'stock_number.txt')

    number_list = number_list[0].split('\n')

    for number in number_list:

        datas_list = get_income_statement(f'https://pchome.megatime.com.tw/stock/sto2/ock1/{seasion}/sid{number}.html')
        print(datas_list)
        print('-----------------------')
        save_datas(datas_list, str(number), f'income_statement_{seasion}.json')
        time.sleep(5)

    print('Done!')


def balance() -> None:
    ''' 取得 資產負債表 並存成 json 文件 '''

    number_list = read_datas('number', 'stock_number.txt')

    number_list = number_list[0].split('\n')

    for number in number_list:
        datas_list = get_balance_sheet(f'https://pchome.megatime.com.tw/stock/sto2/ock0/sid{number}.html')
        print(datas_list)
        print('-----------------------')
        save_datas(datas_list, str(number), 'balance_sheet.json')
        time.sleep(5)

    print('Done!')


if __name__ == '__main__':
    export_income_to_excel('20211')
        