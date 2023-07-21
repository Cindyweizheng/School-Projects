import csv
import re
import pandas as pd
import numpy as np
import os


def read_from_excel(filename, sheet_name):
    reader = pd.ExcelFile(filename)
    dataframe = reader.parse(sheet_name)
    return np.array(dataframe)


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


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


def get_elements(molecular):
    str = ''
    return str.join(re.findall(r'[A-Z][a-z]*', molecular))


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


def percentage_element_new(n):
    print("work start!")
    for i in range(1,n+1):
        datas = read_from_excel(f"data/da{i}.xlsx", "Sheet1")
        file_name = f'result/da{i}'
        mkdir(file_name)
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
        for to in total:
            name = to[0]
            to.pop(0)
            write_to_csv(to, [''], f'{file_name}/{name}.csv')


if __name__ == "__main__":
    # percentage_element(1)
    # print(get_elements("C11H2O"))
    percentage_element_new(1)