'''

    爬取 Pchome 股價函式庫

'''

from bs4 import BeautifulSoup
import requests
import re



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

    return datas_list2
    
