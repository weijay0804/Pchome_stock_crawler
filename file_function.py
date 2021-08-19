'''

    處裡文件的函式庫

'''

import os


def save_datas(datas : list, dirname : str, filename : str) -> None:
    ''' 儲存資料 '''

    if not os.path.exists(f'./DATA/{dirname}'):
        os.mkdir(f'./DATA/{dirname}')

    with open(f'DATA/{dirname}/{filename}.txt', 'w', encoding='utf-8') as f:
        for data in datas:
            f.write(str(data))
            f.write('\n')

    return None

def read_datas(dirname : str, filename : str) -> list:
    ''' 讀取資料 '''

    if not os.path.exists(f'DATA/{dirname}/{filename}.txt'):
        return '資料不存在'

    datas_list = []
    with open(f'DATA/{dirname}/{filename}.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        datas_list.append(data)

    return datas_list
