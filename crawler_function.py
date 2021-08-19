'''

    爬取 Pchome 股價函式庫

'''

from bs4 import BeautifulSoup
import requests
import re

from requests.models import Response




def send_request(url : str) -> requests:
    ''' 發送 request '''

    # 發送情求時帶上的資訊
    config = {
        'headers' : {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'},
        'data' : {'is_check' : '1'}
    }

    response = requests.post(url=url, **config)

    # 處理錯誤資訊
    if response.status_code != 200:
        return f'錯誤! status_code : {response.status_code}'

    return response


def get_stock_numbers() -> list:
    ''' 取得前 30 家公司的股票代碼 '''

    response = send_request('https://pchome.megatime.com.tw/group/mkt0/cid24.html')
    
    # 取得股票代碼的正規表達示
    stock_number_re = re.compile(r'(\d+)')

    # 轉為 BeautifulSoup 物件
    soup = BeautifulSoup(response.text, 'html.parser')

    # 取得股票代碼所在的位置
    datas = data = soup.find('tbody', id='cpidStock').find_all('a')

    stock_numbner_list = []

    # 依序取出股票代碼
    for data in datas:
        number = stock_number_re.search(data.text)
        # 如果沒有股票代碼，則跳出並繼續
        if number is None:
            continue
        stock_numbner_list.append(number.group())

    return stock_numbner_list

def get_balance_sheet(url : str) -> list:
    ''' 取得資產負債表資料 '''

    response = send_request(url)

    # 轉為 BeautifulSoup 物件
    soup = BeautifulSoup(response.text, 'html.parser')

    # 取得 table 中的資料
    table_datas = soup.find('div', id = 'bttb').find_all('td', class_ = 'ct16')

    # 取得每列標題
    titles = soup.find('div', id = 'bttb').find_all('td', class_ = 'ct2')

    title_list = []


    # 依序取出標題
    for title in titles:
        title_list.append(title.text.replace(' ', ''))


    datas_list = []

    # 依序取出資料
    for index, data in enumerate(table_datas, 1):

        # 只取得 第一季 和 第二季 的資料
        if index %6 == 0 or (index + 1) %6 == 0:
            continue

        datas_list.append(data.text)
    
    # 準備將資料分類
    datas_list2 = []
    items = []

    # 將相同列的資料處理成為同一個 list
    for index,data in enumerate(datas_list, 1):
        items.append(data)

        if index %4 == 0:
            datas_list2.append(items)
            items = []

    # 將標題與資料和併
    data_dict_list = []

    for index, data in enumerate(datas_list2):
        try:
            d_dict = {
                title_list[index] : data
            }

            data_dict_list.append(d_dict)
        
        except IndexError:
            continue

    return data_dict_list
    

def get_income_statement(url : str) -> list:
    ''' 獲得損益表的資料 '''

    response = send_request(url)

    # 轉為 BeautifulSoup 物件
    soup = BeautifulSoup(response.text, 'html.parser')

    # 取得每列標題
    titles = titles = soup.find('div', id = 'bttb').find_all('td', class_ = 'ct2')

    title_list = []

    # 依序取出標題
    for title in titles:
        title_list.append(title.text.replace(' ', '').replace('\u3000', ''))

    # 取得 table 中的資料
    datas = soup.find_all('td', class_ = 'ct16')

    data_list = []

    # 依序取出資料
    for index,data  in enumerate(datas):
        # 只取 第一欄的資料
        if index == 0 or index %6 == 0:
            data_list.append(data.text)
        else:
            continue
    
    data_dict_list = []

    # 將資料與標題合併
    for index, item in enumerate(data_list):
        try:
            d_dict = {
                title_list[index] : item
            }
            data_dict_list.append(d_dict)

        except IndexError:
            continue

    return data_dict_list

