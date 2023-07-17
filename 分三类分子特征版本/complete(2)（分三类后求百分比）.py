import csv
import re
import pandas as pd
import numpy as np

def read_from_excel(filename, sheet_name):
    reader = pd.ExcelFile(filename)
    dataframe = reader.parse(sheet_name)
    return np.array(dataframe)

def read_from_csv(filename):
    csvfile = open(filename,"r")
    reader = csv.reader(csvfile)
    result = []
    for item in reader:
        if reader.line_num == 1:
            continue
        result.append(item)
    csvfile.close()
    return result

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
    return re.findall(r'[A-Z][a-z]*|[0-9]+',molecular)

def find_ele(data):
    final_ele = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_ele = get_elements(data)
    # print(list_ele)
    for i in range(0, len(list_ele), 2):
        if list_ele[i] == 'C':
            final_ele[0] = int(list_ele[i+1])
        elif list_ele[i] == 'H':
            final_ele[1] = int(list_ele[i+1])
        elif list_ele[i] == 'O':
            final_ele[2] = int(list_ele[i+1])
        elif list_ele[i] == 'N':
            final_ele[3] = int(list_ele[i+1])
        elif list_ele[i] == 'S':
            final_ele[4] = int(list_ele[i+1])
        elif list_ele[i] == 'P':
            final_ele[5] = int(list_ele[i+1])
        elif list_ele[i] == 'Cl':
            final_ele[6] = int(list_ele[i+1])
        elif list_ele[i] == 'Br':
            final_ele[7] = int(list_ele[i+1])
        else:
            final_ele[8] = int(list_ele[i+1])
    # print(final_ele)
    return final_ele
def count_result(data):
    # DBE
    data.append((2*data[0]+data[3]+data[5]-data[1]-(data[6]+data[7]+data[8])+2)/2)
    # O/C
    data.append(data[2]/data[0])
    # H/C
    data.append(data[1]/data[0])
    # N/C
    data.append(data[3]/data[0])
    # S/C
    data.append(data[4]/data[0])
    # P/C
    data.append(data[5]/data[0])
    # Cl/C
    data.append(data[6]/data[0])
    # Br/C
    data.append(data[7]/data[0])
    # I/C
    data.append(data[8]/data[0])
    # Aimod
    if (data[0] - 0.5 * data[2] - data[3] - data[4]) != 0:
        data.append((1+data[0]-0.5*data[2]-data[4]-0.5*(data[3]+data[5]+data[1]+data[6]+data[7]+data[8]))/(data[0]-0.5*data[2]-data[3]-data[4]))
    else:
        data.append("0")
    # NOSC
    data.append(4-((4*data[0]+data[1]+data[6]+data[7]+data[8]-3*data[3]-2*data[2]-2*data[4])/data[0]))
    # X/C
    if data[0] != 0:
        data.append((data[6]+data[7]+data[8])/data[0])
    else:
        data.append(0)
    # DBE-O
    data.append(data[9]-data[2])
    # DBE/C
    if data[0] != 0:
        data.append(data[9]/data[0])
    else:
        data.append(0)

def element_division():
    print("work start!")
    datas = []
    names = []
    for i in range(1,4):
        datas.append(read_from_excel(f"D:/ftms数据处理代码/workspace/分三类分子特征版本/data{i}.xlsx","Sheet1"))
        names.append(f'data{i}')
    for data,name in zip(datas,names):
        result = []
        for da in data:
            ele_get = find_ele(da[1])
            count_result(ele_get)
            result.append(list(da[0:3:])+ele_get)
        header = ["weight", "molecular", "strength", "C", "H", "O", "N", "S", "P", "Cl", "Br", "I", "DBE", "O/C", "H/C", "N/C", "S/C", "P/C", "Cl/C", "Br/C", "I/C", "Almod", "NOSC", "X/C", "DBE-O", "DBE/C"]
        file = "D:/ftms数据处理代码/workspace/分三类分子特征版本/result/result(元素比)_"+ name +".csv"
        write_to_csv(result, header, file)

def percentage_five_seven():
    print("work start!")
    datas = []
    for i in range(1,4):
        datas.append(read_from_csv(f"D:/ftms数据处理代码/workspace/分三类分子特征版本/result/result(元素比)_data{i}.csv"))
    Ca = 0
    Pr = 0
    Li = 0
    Ta = 0
    Lica = 0
    Un  = 0
    Co = 0
    cpa = 0
    P = 0
    hupc = 0
    ac = 0
    sc = 0
    total = 0
    for data in datas:
        for da in data:
            total += float(da[2])
            if 1.5 < float(da[14]) < 2.2 and 0.67 < float(da[13]) < 1.0:
                Ca += float(da[2])
            elif 1.5 < float(da[14]) < 2.2 and 0.3 < float(da[13]) < 0.67:
                Pr += float(da[2])
            elif 1.5 < float(da[14]) < 2.0 and 0 < float(da[13]) < 0.3:
                Li += float(da[2])
            elif 0 < float(da[14]) < 1.5 and 0.67 < float(da[13]) < 1.0:
                Ta += float(da[2])
            elif 0.7 < float(da[14]) < 1.5 and 0.1 < float(da[13]) < 0.67:
                Lica += float(da[2])
            elif 0.7 < float(da[14]) < 1.5 and 0 < float(da[13]) < 0.1:
                Un += float(da[2])
            elif 0.2 < float(da[14]) < 0.7 and 0 < float(da[13]) < 0.67:
                Co += float(da[2])
            if float(da[21]) > 0.66:
                cpa += float(da[2])
            elif 0.5 < float(da[21]) < 0.66:
                P += float(da[2])
            elif float(da[21]) <= 0.5 and float(da[14]) < 1.5:
                hupc += float(da[2])
            elif float(da[21]) <= 0.5 and 1.5 < float(da[14]) <2.0 :
                ac += float(da[2])
            elif float(da[14]) == 2.0:
                sc += float(da[2])

    print(f'Car:\t{Ca/total}')
    print(f'Pro:\t{Pr/total}')
    print(f'Lip:\t{Li/total}')
    print(f'Tan:\t{Ta/total}')
    print(f'Lig:\t{Lica/total}')
    print(f'Uns:\t{Un/total}')
    print(f'Con:\t{Co/total}')
    print()
    print(f'Cpa:\t{cpa/total}')
    print(f'Pol:\t{P/total}')
    print(f'Hupc:\t{hupc/total}')
    print(f'Ac:\t\t{ac/total}')
    print(f'Sc:\t\t{sc/total}')


def percentage_element():
    print("work start!")
    datas = []
    for i in range(1,4):
        datas.append(read_from_excel(f"D:/ftms数据处理代码/workspace/分三类分子特征版本/data{i}.xlsx","Sheet1"))
    cho = []
    chon = []
    chos = []
    chons = []
    cho_strength = 0
    chos_strength = 0
    chon_strength = 0
    chons_strength = 0
    total_strength = 0
    for data in datas:
        for da in data:
            total_strength += float(da[2])
            result = get_elements(da[1])
            if len(result) == 6:
                cho.append(da)
                cho_strength += float(da[2])
            elif len(result) == 10:
                chons.append(da)
                chons_strength += float(da[2])
            else:
                if result[6] == 'S':
                    chos.append(da)
                    chos_strength += float(da[2])
                else:
                    chon.append(da)
                    chon_strength += float(da[2])

    print(f'cho:\t\t{cho_strength / total_strength}')
    print(f'chon:\t\t{chon_strength / total_strength}')
    print(f'chos:\t\t{chos_strength / total_strength}')
    print(f'chons:\t\t{chons_strength / total_strength}')

if __name__ == '__main__':
    element_division()
    print("--------------------------------")
    percentage_five_seven()
    print("--------------------------------")
    percentage_element()