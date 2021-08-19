'''

    處裡文件的函式庫

'''

import os
import json


def save_datas(datas_list : list, dirname : str, filename : str) -> None:
    ''' 儲存資料 '''

    if not os.path.exists(f'./DATA/{dirname}'):
        os.mkdir(f'./DATA/{dirname}')

    if os.path.exists(f'DATA/{dirname}/{filename}'):
        os.remove(f'DATA/{dirname}/{filename}')

    if filename.endswith('.json'):

        with open(f'DATA/{dirname}/{filename}', 'w', encoding='utf-8') as f:
            datas = json.dumps(datas_list, indent=5)
            f.write(datas)

    elif filename.endswith('.txt'):

        with open(f'DATA/{dirname}/{filename}', 'w', encoding='utf-8') as f:
            for data in datas_list:
                f.write(str(data))
                f.write('\n')

    else:
        return '不支援的檔案格式'

    return None

def read_datas(dirname : str, filename : str) -> list:
    ''' 讀取資料 '''

    if not os.path.exists(f'DATA/{dirname}/{filename}'):
        return '資料不存在'

    if filename.endswith('txt'):
        datas_list = []
        with open(f'DATA/{dirname}/{filename}', 'r', encoding='utf-8') as f:
            data = f.read()
            datas_list.append(data)

    elif filename.endswith('json'):
        with open(f'DATA/{dirname}/{filename}', encoding='utf-8') as f:
            datas_list = json.load(f)

    else:
        return '不支援的檔案格式'
        
    return datas_list

