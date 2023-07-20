import csv
import re
import pandas as pd
import numpy as np


def read_from_excel(filename, sheet_name):
    reader = pd.ExcelFile(filename)
    dataframe = reader.parse(sheet_name)
    return np.array(dataframe)


# def read_from_csv(filename):
#     csvfile = open(filename,"r")
#     reader = csv.reader(csvfile)
#     result = []
#     for item in reader:
#         if reader.line_num == 1:
#             continue
#         result.append(item)
#     csvfile.close()
#     return result


def write_to_csv(data, header, file):
    with open(file, "w", newline="")as f:
        writer = csv.writer(f)
        writer.writerow(header)
        count = 1
        for da in data:
            writer.writerow(da)
            percent = int(count / len(data) * 50)
            print(f'\r[{"#" * percent}{"." * (50 - percent)}]\t{count}/{len(data)}', end=".")
            count += 1
        print()
        f.close()


def percentage_element(n):
    print("work start!")
    for i in range(1,n+1):
        datas = read_from_excel(f"data/da{i}.xlsx", "Sheet1")
        cho = []
        chon = []
        chos = []
        chons = []
        others = []
        for data in datas:
            # 7:C, 8:H, 9:N, 10:O, 11:S
            if data[7] != 0 and data[8] != 0 and data[9] != 0 and data[10] != 0 and data[11] != 0:
                chons.append(data)
            elif data[7] != 0 and data[8] != 0 and data[9] != 0 and data[10] != 0:
                chon.append(data)
            elif data[7] != 0 and data[8] != 0 and data[11] != 0 and data[10] != 0:
                chos.append(data)
            elif data[7] != 0 and data[8] != 0 and data[10] != 0:
                cho.append(data)
            else :
                others.append(data)
        write_to_csv(cho, [''], f'result/{i}_cho.csv')
        write_to_csv(chon, [''], f'result/{i}_chon.csv')
        write_to_csv(chos, [''], f'result/{i}_chos.csv')
        write_to_csv(chons, [''], f'result/{i}_chons.csv')
        write_to_csv(others, [''], f'result/{i}_others.csv')


if __name__ == "__main__":
    percentage_element(1)