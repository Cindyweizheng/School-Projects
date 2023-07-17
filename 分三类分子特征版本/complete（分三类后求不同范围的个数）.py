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
    data.append((1+data[0]-0.5*data[2]-data[4]-0.5*(data[3]+data[5]+data[1]+data[6]+data[7]+data[8]))/(data[0]-0.5-data[3]-data[4]))
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
        datas.append(read_from_excel(f".D:/ftms数据处理代码/workspace/新建文件夹 (2)/data{i}.xlsx","Sheet1"))
        names.append(f'data{i}')
    for data,name in zip(datas,names):
        result = []
        for da in data:
            ele_get = find_ele(da[1])
            count_result(ele_get)
            result.append(list(da[0:3:])+ele_get)
        header = ["weight", "molecular", "strength", "C", "H", "O", "N", "S", "P", "Cl", "Br", "I", "DBE", "O/C", "H/C", "N/C", "S/C", "P/C", "Cl/C", "Br/C", "I/C", "Almod", "NOSC", "X/C", "DBE-O", "DBE/C"]
        file = "D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/result(元素比)_"+ name +".csv"
        write_to_csv(result, header, file)

def percentage_five_seven():
    print("work start!")
    datas = []
    for i in range(1,4):
        datas.append(read_from_csv(f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/result(元素比)_data{i}.csv"))
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

def count_number():
    print("work start!")
    datas = []
    for i in range(1,4):
        datas.append(read_from_csv(f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/result(元素比)_data{i}.csv"))
    mz2 = mz3 = mz4 = mz5 = mz6 = mz7= mz8 = 0
    hc04 = hc06 = hc08 = hc10 = hc12 = hc14 =hc16 = 0
    oc2 = oc3 = oc4 = oc5 = oc6 = oc7 = 0
    nosc1 = nosc2 = nosc3 = nosc4 = nosc5 = nosc6 = nosc7 = 0
    obe1 = obe2 = obe3 = obe4 = obe5 = obe6 = obe7 = 0
    for data in datas:
        for da in data:
            if 200 < float(da[0]) < 300:
                mz2 += 1
            elif 300 < float(da[0]) < 400:
                mz3 += 1
            elif 400 < float(da[0]) < 500:
                mz4 += 1
            elif 500 < float(da[0]) < 600:
                mz5 += 1
            elif 600 < float(da[0]) < 700:
                mz6 += 1
            elif 700 < float(da[0]) < 800:
                mz7 += 1
            elif 800 < float(da[0]) < 900:
                mz8 += 1
            if 0.4 < float(da[14]) < 0.6:
                hc04 +=1
            elif 0.6 < float(da[14]) < 0.8:
                hc06 += 1
            elif 0.8 < float(da[14]) < 1.0:
                hc08 += 1
            elif 1.0 < float(da[14]) < 1.2:
                hc10 += 1
            elif 1.2 < float(da[14]) < 1.4:
                hc12 += 1
            elif 1.4 < float(da[14]) < 1.6:
                hc14 += 1
            elif 1.6 < float(da[14]) < 1.8:
                hc16 += 1
            if 0.2 < float(da[13]) <0.3:
                oc2 += 1
            elif 0.3 <float(da[13]) < 0.4:
                oc3 += 1
            elif 0.4 <float(da[13]) < 0.5:
                oc4 += 1
            elif 0.5 <float(da[13]) < 0.6:
                oc5 += 1
            elif 0.6 <float(da[13]) < 0.7:
                oc6 += 1
            elif 0.7 <float(da[13]) < 0.8:
                oc7 += 1
            if -1.5 < float(da[22]) < -1:
                nosc1 += 1
            elif -1 < float(da[22]) < -0.5:
                nosc2 += 1
            elif -0.5 < float(da[22]) < 0:
                nosc3 += 1
            elif 0 < float(da[22]) < 0.5:
                nosc4 += 1
            elif 0.5 < float(da[22]) < 1:
                nosc5 += 1
            elif 1 < float(da[22]) < 1.5:
                nosc6 += 1
            elif 1.5 < float(da[22]) < 2:
                nosc7 += 1
            if 0 < float(da[12]) < 4:
                obe1 += 1
            elif 4 < float(da[12]) < 8:
                obe2 += 1
            elif 8 < float(da[12]) < 12:
                obe3 += 1
            elif 12 < float(da[12]) < 16:
                obe4 += 1
            elif 16 < float(da[12]) < 20:
                obe5 += 1
            elif 20 < float(da[12]) < 24:
                obe6 += 1
            elif 24 < float(da[12]) < 28:
                obe7 += 1

    print("每类的个数为：")
    print("M/Z")
    print(f"200-300:\t\t{mz2}")
    print(f"300-400:\t\t{mz3}")
    print(f"400-500:\t\t{mz4}")
    print(f"500-600:\t\t{mz5}")
    print(f"600-700:\t\t{mz6}")
    print(f"700-800:\t\t{mz7}")
    print(f"800-900:\t\t{mz8}")
    print("H/C")
    print(f"0.4-0.6:\t\t{hc04}")
    print(f"0.6-0.8:\t\t{hc06}")
    print(f"0.6-0.8:\t\t{hc08}")
    print(f"0.8-1.0:\t\t{hc10}")
    print(f"1.0-1.2:\t\t{hc12}")
    print(f"1.4-1.6:\t\t{hc14}")
    print(f"1.6-1.8:\t\t{hc16}")
    print("O/C")
    print(f"0.2-0.3:\t\t{oc2}")
    print(f"0.3-0.4:\t\t{oc3}")
    print(f"0.4-0.5:\t\t{oc4}")
    print(f"0.5-0.6:\t\t{oc5}")
    print(f"0.6-0.7:\t\t{oc6}")
    print(f"0.7-0.8:\t\t{oc7}")
    print("NOSC")
    print(f"-1.5--1:\t\t{nosc1}")
    print(f"-1--0.5:\t\t{nosc2}")
    print(f"-0.5-0: \t\t{nosc3}")
    print(f"0-0.5:  \t\t{nosc4}")
    print(f"0.5-1:  \t\t{nosc5}")
    print(f"1-1.5:  \t\t{nosc6}")
    print(f"1.5-2:  \t\t{nosc7}")
    print("OBE")
    print(f"0-4:\t\t{obe1}")
    print(f"4-8:\t\t{obe2}")
    print(f"8-12:\t\t{obe3}")
    print(f"12-16:\t\t{obe4}")
    print(f"16-20:\t\t{obe5}")
    print(f"20-24:\t\t{obe6}")
    print(f"24-28:\t\t{obe7}")


def percentage_element():
    print("work start!")
    datas = []
    for i in range(1,4):
        datas.append(read_from_excel(f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/data{i}.xlsx","Sheet1"))
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
    print("--------------------------------")
    count_number()