from crawler_function import get_stock_numbers, get_balance_sheet, get_income_statement, send_request
from file_function import save_datas, read_datas
import openpyxl
import time
import json
import os


def main():
    number_list = read_datas('number', 'stock_number.txt')

    number_list = number_list[0].split('\n')

    for number in number_list:
        income_statement_20211 = get_income_statement(f'https://pchome.megatime.com.tw/stock/sto2/ock1/20211/sid{number}.html')
        print(income_statement_20211)
        print('-----------------------')
        save_datas(income_statement_20211, str(number), 'income_statement_20211.json')
        time.sleep(2)

    print('Done!')

def export_balance_to_excel():
    ''' 將資產負債表資料整理成 excel 型式 並匯出 '''
    
    number_list = read_datas('number', 'stock_number.txt')  # 讀取公司股票代號

    for number in number_list[0].split('\n'):
        workbook = openpyxl.Workbook()  # 建立活頁簿
        workbook.create_sheet('第二季') # 建立第二個工作表

        sheet1 = workbook.worksheets[0] # 取得第一個工作表
        sheet1.title = '第一季' # 更改工作表名稱

        sheet2 = workbook.worksheets[1] # 取得第二個工作表

        

        # 取得資產負債表資訊
        datas = read_datas(str(number), 'balance_sheet.json')
        
        s1_data_list = []   # 儲存 第一季 資料 list
        s2_data_list = []   # 儲存 第二季 資料 list

        for data in datas:
            items = list(data.items())[0]   # 將字典轉為 list

            # 將 str 型態轉為 float (123,456,1.12 -> 1234561.12)
            try:
                s1_values = float(items[1][0].replace(',',''))
                s1_percent = float(items[1][1].replace(',',''))

                s2_values = float(items[1][2].replace(',', ''))
                s2_percent = float(items[1][3].replace(',', ''))

            except:
                s1_values = 0
                s1_percent = 0

                s2_values = 0
                s2_percent = 0

            s1_values_list = [
                items[0],
                s1_values,
            ]

            s1_percent_list = [
                '%',
                s1_percent
            ]

            s2_values_list = [
                items[0],
                s2_values
            ]

            s2_percent_list = [
                '%',
                s2_percent
            ]
            
            s1_data_list.append(s1_values_list)
            s1_data_list.append(s1_percent_list)

            s2_data_list.append(s2_values_list)
            s2_data_list.append(s2_percent_list)
        
        for i in s1_data_list:
            sheet1.append(i)

        for j in s2_data_list:
            sheet2.append(j)

        workbook.save(f'DATA/{number}/{number}_balance.xlsx')


if __name__ == '__main__':
    export_balance_to_excel()