import csv
import numba
import pandas as pd
import datetime
import numpy as np
from collections import Counter
import re
import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def read_from_excel(file_name, sheet_name):
    reader = pd.ExcelFile(file_name)
    dataframe = reader.parse(sheet_name)
    return np.array(dataframe)


def to_list(data):
    list_data = []
    for key, value in data.items():
        list_data.append([key, value])
    return list_data


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def write_to_csv(file, header, data):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for d in data:
            writer.writerow(d)


# @numba.jit(nopython=True)
def new_molecular_weight(data, data_iupac):
    data_mo = re.findall(r"[A-Z][a-z]*|[0-9]+", data)
    result = 0.0
    for i in range(0, len(data_mo), 2):
        for data_i in data_iupac:
            if data_mo[i] == data_i[0]:
                result += float(data_i[1]) * float(data_mo[i + 1])
    return result


def Update_Mol(data_file, data_sheet_a, data_sheet_b, iupac_file, iupac_sheet, save_file):
    print("Start update data!")
    data_a = read_from_excel(data_file, data_sheet_a)
    data_b = read_from_excel(data_file, data_sheet_b)
    data_iupac = read_from_excel(iupac_file, iupac_sheet)
    i = 1
    len_data = len(data_a)+len(data_b)
    for data in data_a:
        data[1] = new_molecular_weight(data[0], data_iupac)
        percent = int(i/len_data*50)
        print(f'\r[{"#"*percent}{"."*(50-percent)}]\t{percent*2}%', end=".")
        i += 1
    for data in data_b:
        data[1] = new_molecular_weight(data[0], data_iupac)
        percent = int(i/len_data*50)
        print(f'\r[{"#"*percent}{"."*(50-percent)}]\t{percent*2}%', end=".")
        i += 1
    print()

    print("Update data over! start saving data!")
    new_dataframe1 = pd.DataFrame(data_a)
    new_dataframe1.columns = ['mol', 'wei', 'str']
    new_dataframe2 = pd.DataFrame(data_b)
    new_dataframe2.columns = ['mol', 'wei', 'str']

    writer = pd.ExcelWriter(save_file)
    new_dataframe1.to_excel(writer, sheet_name=data_sheet_a, index=False)
    new_dataframe2.to_excel(writer, sheet_name=data_sheet_b, index=False)
    writer.save()
    print("saved!")


def main(n):
    print("work start!")
    '''
        原始数据请以data加数字命名，数字从1开始，放在excelfile/data目录下。
        替换分子量之后的数据请以new_data加数字命名，数字从1开始，放在excelfile/temp目录下。
    '''
    for i in range(1, n+1):
        org_data_file = f'excelfile/data/data{i}.xlsx'
        temp_dir = 'excelfile/temp'
        mkdir(temp_dir)
        new_data_file = f'{temp_dir}/new_data{i}.xlsx'
        save_dir = f'excelfile/result/{i}'
        mkdir(save_dir)
        choice = input("如果你是第一次启动本程序没有换算后的数据请按enter键继续，\n如果你已经运行一次，并且有换算后的数据请输入c并回车跳过分子量换算步骤(这会为你节约大量的时间)\n:")
        if choice != "c" and choice != "C":
            Update_Mol(org_data_file, 'A', 'B', 'excelfile/data/iupac.xlsx', 'Sheet1', f'{temp_dir}/new_data{i}.xlsx')
        data_A = read_from_excel(new_data_file, 'A')
        data_B = read_from_excel(new_data_file, 'B')
        # print(len(data_A))
        # print(len(data_B))
        result = []
        result2 = []
        data_len = len(data_A)*len(data_B)
        count = 1
        for data_a in data_A:
            for data_b in data_B:
                result.append([data_b[0], data_b[1], data_b[2], data_a[0], data_a[1], data_b[2], data_b[1] - data_a[1]])
                result2.append(data_b[1] - data_a[1])
                percent = int(count / data_len * 50)
                count += 1
            print(f'\r[{"#"*percent}{"."*(50-percent)}]\t{percent*2}%', end=".")
        print()

        r2_len = len(result2)
        for i in range(r2_len):
            result2[i] = round(result2[i], 7)
            percent = int((i+1)/r2_len*50)
            if i%50==0 or i==r2_len-1:
                print(f'\r[{"#" * percent}{"." * (50 - percent)}]\t{percent * 2}%', end=".")
        print()
        result_count2 = np.array(list(set([tuple(t) for t in to_list(dict(Counter(result2)))])))
        result_count2 = sorted(result_count2, key=(lambda x:x[1]), reverse=True)
        # print(len(result_count2))

        '''
        print("start writing count!")
        count = len(result)/1000000
        if count%1 != 0:
            count = int(count)+1
        else :
            count = int(count)
        for i in range(count):
            file = f"{save_dir}/count{i+1}.csv"
            header = ["mol", "wei", "str", "mol", "wei", "str", "result"]
            data = result[i*1000000:(i+1)*1000000:]
            write_to_csv(file, header, data)
        print("count write completed!")
        '''

        print("start writing result!")
        count = len(result_count2)/1000000
        if count%1 != 0:
            count = int(count)+1
        else :
            count = int(count)
        for i in range(count):
            file = f"{save_dir}/result{i+1}.csv"
            header = ["reasult", "count"]
            data = result_count2[i*1000000:(i+1)*1000000:]
            write_to_csv(file, header, data)
        print("result write completed!")


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    n = 1
    # data_iupac = read_from_excel('excelfile/data/iupac.xlsx', 'Sheet1')
    # print(data_iupac)
    main(n)
    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    print(run_time.seconds)