'''

    處裡文件的函式庫

'''

def save_datas(datas : list, filename : str) -> None:
    ''' 儲存資料 '''

    with open(f'{filename}.txt', 'w', encoding='utf-8') as f:
        for data in datas:
            f.write(str(data))
            f.write('\n')

    return None