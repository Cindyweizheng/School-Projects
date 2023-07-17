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

def add_to_csv(data,file):
    df = pd.DataFrame(data)
    df.to_csv(file,mode='a',header=False)

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
    data.append((1+data[0]-0.5-0.5*(data[3]+data[5]+data[1]+data[6]+data[7]+data[8]))/(data[0]-0.5-data[3]-data[4]))
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
    for i in range(1,2):
        datas.append(read_from_excel(f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/data{i}.xlsx","Sheet1"))
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

def percentage_five_seven(datas,names):
    print("work start!")
    for data,name in zip(datas,names):
        result = []
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
        result.append(["Percentage is"])
        result.append(["Car",Ca/total])
        result.append(["Pro",Pr/total])
        result.append(["Lip",Li/total])
        result.append(["Tan",Ta/total])
        result.append(["Lig",Lica/total])
        result.append(["Uns",Un/total])
        result.append(["Con",Co/total])
        result.append(["Cpa",cpa/total])
        result.append(["Pol",P/total])
        result.append(["Hupc",hupc/total])
        result.append(["Ac",ac/total])
        result.append(["Sc",sc/total])
        add_to_csv(result,f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/{name}.csv")


def count_number(datas,names):
    print("work start!")
    for data, name in zip(datas, names):
        result = []
        mz2 = mz3 = mz4 = mz5 = mz6 = mz7= mz8 = 0
        hc04 = hc06 = hc08 = hc10 = hc12 = hc14 =hc16 = 0
        oc2 = oc3 = oc4 = oc5 = oc6 = oc7 = 0
        nosc1 = nosc2 = nosc3 = nosc4 = nosc5 = nosc6 = nosc7 = 0
        obe1 = obe2 = obe3 = obe4 = obe5 = obe6 = obe7 = 0
        AImod1 = AImod2 = AImod3 = AImod4 = AImod5 = AImod6 = 0
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
            if -0.2 < float(da[21]) < 0:
                AImod1 += 1
            elif 0 < float(da[21]) < 0.2:
                AImod2 += 1
            elif 0.2 < float(da[21]) < 0.4:
                AImod3 += 1
            elif 0.4 < float(da[21]) < 0.6:
                AImod4 += 1
            elif 0.6 < float(da[21]) < 0.8:
                AImod5 += 1
            elif 0.8 < float(da[21]) < 1:
                AImod6 += 1
        result.append(["The number is"])
        result.append(["M/Z"])
        result.append(["200-300",mz2])
        result.append(["300-400",mz3])
        result.append(["400-500",mz4])
        result.append(["500-600",mz5])
        result.append(["600-700",mz6])
        result.append(["700-800",mz7])
        result.append(["800-900",mz8])
        result.append(["H/C"])
        result.append(["0.4-0.6",hc04])
        result.append(["0.6-0.8",hc06])
        result.append(["0.6-0.8",hc08])
        result.append(["0.8-1.0",hc10])
        result.append(["1.0-1.2", hc12])
        result.append(["1.2-1.4", hc14])
        result.append(["1.4-1.6", hc16])
        result.append(["O/C"])
        result.append(["0.2-0.3",oc2])
        result.append(["0.3-0.4", oc3])
        result.append(["0.4-0.5", oc4])
        result.append(["0.5-0.6", oc5])
        result.append(["0.6-0.7", oc6])
        result.append(["0.7-0.8", oc7])
        result.append(["NOSC"])
        result.append(["-1.5~-1",nosc1])
        result.append(["-1~-0.5",nosc2])
        result.append(["-0.5~0", nosc3])
        result.append(["0-0.5", nosc4])
        result.append(["0.5-1", nosc5])
        result.append(["1-1.5", nosc6])
        result.append(["1.5-2", nosc7])
        result.append(["OBE"])
        result.append(["0-4",obe1])
        result.append(["4~8", obe2])
        result.append(["8~12", obe3])
        result.append(["12~16", obe4])
        result.append(["16~20", obe5])
        result.append(["20-24", obe6])
        result.append(["24-28", obe1])
        result.append(["AImod"])
        result.append(["-0.2~0",AImod1])
        result.append(["0~0.2", AImod2])
        result.append(["0.2~0.4", AImod3])
        result.append(["0.4~0.6", AImod4])
        result.append(["0.6~0.8", AImod5])
        result.append(["0.8~1", AImod6])
        add_to_csv(result,f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/{name}.csv")


def percentage_element():
    print("work start!")
    datas = []
    names = []
    for i in range(1,19):
        datas.append(read_from_excel(f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/data{i}.xlsx","Sheet1"))
        names.append(f"result(元素比)_data{i}")
    for data, name in zip(datas, names):
        results = []
        cho = []
        chon = []
        chos = []
        chons = []
        cho_strength = 0
        chos_strength = 0
        chon_strength = 0
        chons_strength = 0
        total_strength = 0
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

        results.append(["cho",cho_strength/total_strength])
        results.append(["chon",chon_strength/total_strength])
        results.append(["chos",chos_strength/total_strength])
        results.append(["chons",chons_strength/total_strength])
        add_to_csv(results,f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/{name}.csv")


if __name__ == '__main__':
    element_division()
    print("================================")
    datas = []
    names = []
    for i in range(1,19):
        datas.append(read_from_csv(f"D:/ftms数据处理代码/workspace/新建文件夹 (2)/result/result(元素比)_data{i}.csv"))
        names.append(f"result(元素比)_data{i}")
    percentage_five_seven(datas,names)
    print("================================")
    percentage_element()
    print("================================")
    count_number(datas,names)