import re
import pandas as pd
import numpy as np
from openpyxl import Workbook


def get_elements(molecular):
    str = ''
    return str.join(re.findall(r'[A-Z][a-z]*', molecular))


def switch_ele(data, n, m):
    data_temp = data[n]
    data[n] = data[m]
    data[m] = data_temp


def percentage_element(n):
    print("work start!")
    for i in range(1,n+1):
        datas = list(np.array(pd.read_excel(f'data/da{i}.xlsx', header=None)))
        name = list(datas[0])
        datas.pop(0)
        total = []
        for data in datas:
            result = get_elements(data[6])
            data = np.append(data, result)
            sig = 0
            for to in total:
                if result == to[0]:
                    to.append(data)
                    sig += 1
            if sig == 0:
                total.append([result, data])
        for j in range(len(total)):
            if total[j][0] == "CHO":
                switch_ele(total, j, 0)
            if total[j][0] == "CHNO":
                switch_ele(total, j, 1)
            if total[j][0] == "CHOS":
                switch_ele(total, j, 2)
            if total[j][0] == "CHNOS":
                switch_ele(total, j, 3)
        print(f"请注意da{i}结果中将会出现{len(total)}个sheet！")
        wb = Workbook()
        ws = wb.active
        ws.title = total[0][0]
        ws.append(name)
        total[0].pop(0)
        for t in total[0]:
            ws.append(list(t))
        total.pop(0)
        for to in total:
            ws = wb.create_sheet(to[0])
            ws.append(name)
            to.pop(0)
            for t in to:
                t = list(t)
                ws.append(t)
        wb.save(f"result/da{i}.xlsx")


if __name__ == "__main__":
    percentage_element(1)
