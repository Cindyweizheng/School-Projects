import re
import pandas as pd
import numpy as np
from openpyxl import Workbook


def read_from_excel(filename, sheet_name):
    reader = pd.ExcelFile(filename)
    dataframe = reader.parse(sheet_name)
    return np.array(dataframe)


def get_elements(molecular):
    str = ''
    return str.join(re.findall(r'[A-Z][a-z]*', molecular))


def percentage_element(n):
    print("work start!")
    for i in range(1,n+1):
        datas = read_from_excel(f"data/da{i}.xlsx", "Sheet1")
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
        print(f"请注意da{i}结果中将会出现{len(total)}个sheet！")
        wb = Workbook()
        ws = wb.active
        ws.title = total[0][0]
        total[0].pop(0)
        for t in total[0]:
            ws.append(list(t))
        total.pop(0)
        for to in total:
            ws = wb.create_sheet(to[0])
            to.pop(0)
            for t in to:
                t = list(t)
                ws.append(t)
        wb.save(f"result/da{i}.xlsx")


if __name__ == "__main__":
    percentage_element(1)
