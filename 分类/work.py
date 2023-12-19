import csv
import pandas as pd
import numpy as np

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

def read_from_excel(filename, sheet_name):
    # reader = pd.ExcelFile(filename)
    # dataframe = reader.parse(sheet_name)
    # return np.array(dataframe)
    df = pd.read_excel(filename,sheet_name)
    return df

def O(O):
    datas = read_from_csv("./data/test.csv")
    # print(datas)
    for data in datas:
        if eval(data[10])==2:
            O.append(data)
    return O

def main():
    O2=[]
    O3=[]
    O4=[]
    O5=[]
    O6=[]
    O7=[]
    O8=[]
    O9=[]
    O10=[]
    O11=[]
    O12=[]
    O13=[]
    O14=[]
    O15=[]
    O16=[]
    N1O3=[]
    N1O4=[]
    N1O5=[]
    N1O6=[]
    N1O7=[]
    N1O8=[]
    N1O9=[]
    N1O10=[]
    N1O11=[]
    N1O12=[]
    N1O13=[]
    N1O14=[]
    O3S1=[]
    O4S1=[]
    O5S1=[]
    O6S1=[]
    O7S1=[]
    O8S1=[]
    O9S1=[]
    O10S1=[]
    O11S1=[]
    O12S1=[]

    datas = read_from_csv("./data/1.csv")
    # print(datas)
    for data in datas:
        if eval(data[10])==2:
            O2.append(data)
    for data in datas:
        if eval(data[10])==3:
            O3.append(data)
    for data in datas:
        if eval(data[10])==4:
            O4.append(data)
    for data in datas:
        if eval(data[10])==5:
            O5.append(data)
    for data in datas:
        if eval(data[10])==6:
            O6.append(data)
    for data in datas:
        if eval(data[10])==7:
            O7.append(data)
    for data in datas:
        if eval(data[10])==8:
            O8.append(data)
    for data in datas:
        if eval(data[10])==9:
            O9.append(data)
    for data in datas:
        if eval(data[10])==10:
            O10.append(data)
    for data in datas:
        if eval(data[10])==11:
            O11.append(data)
    for data in datas:
        if eval(data[10])==12:
            O12.append(data)
    for data in datas:
        if eval(data[10])==13:
            O13.append(data)
    for data in datas:
        if eval(data[10])==14:
            O14.append(data)
    for data in datas:
        if eval(data[10])==15:
            O15.append(data)
    for data in datas:
        if eval(data[10])==16:
            O16.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==3):
            N1O3.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==4):
            N1O4.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==5):
            N1O5.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==6):
            N1O6.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==7):
            N1O7.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==8):
            N1O8.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==9):
            N1O9.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==10):
            N1O10.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==11):
            N1O11.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==12):
            N1O12.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==13):
            N1O13.append(data)
    for data in datas:
        if data[9]==1 and eval(data[10]==14):
            N1O14.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==3):
            O3S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==4):
            O4S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==5):
            O5S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==6):
            O6S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==7):
            O7S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==8):
            O8S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==9):
            O9S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==10):
            O10S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==11):
            O11S1.append(data)
    for data in datas:
        if data[11]==1 and eval(data[10]==12):
            O12S1.append(data)

    header = ["mSigma","ObservedIntens","ObservedM_z","calc_M_z","errMDa","errPpm","sumFormula","C","H","N","O","S","H1","HCraito","OCraito","CN2","NSP","abserrPpm"
              ,"sumintens","relativeintens","avemass","dbe_o","aimod","dbe","nosc","kmdch2","nkmch2","kmdh2","nkmh2","kmdh2o","nkmh2o","kmdo","nkmo","kmdcoo","nkmcoo"]
    fileO2 = f"./result/O2.csv"
    write_to_csv(O2,header,fileO2)
    fileO3 = f"./result/O3.csv"
    write_to_csv(O3,header,fileO3)
    fileO4 = f"./result/O4.csv"
    write_to_csv(O4,header,fileO4)
    fileO5 = f"./result/O5.csv"
    write_to_csv(O5,header,fileO5)
    fileO6 = f"./result/O6.csv"
    write_to_csv(O6,header,fileO6)
    fileO7 = f"./result/O7.csv"
    write_to_csv(O7,header,fileO7)
    fileO8 = f"./result/O8.csv"
    write_to_csv(O8,header,fileO8)
    fileO9 = f"./result/O9.csv"
    write_to_csv(O9,header,fileO9)
    fileO10 = f"./result/O10.csv"
    write_to_csv(O10,header,fileO10)
    fileO11 = f"./result/O11.csv"
    write_to_csv(O11,header,fileO11)
    fileO12 = f"./result/O12.csv"
    write_to_csv(O12,header,fileO12)
    fileO13 = f"./result/O13.csv"
    write_to_csv(O13,header,fileO13)
    fileO14 = f"./result/O14.csv"
    write_to_csv(O14,header,fileO14)
    fileO15 = f"./result/O15.csv"
    write_to_csv(O15,header,fileO15)
    fileO16 = f"./result/O16.csv"
    write_to_csv(O16,header,fileO16)

    fileN1O3 = f"./result/N1O3.csv"
    write_to_csv(N1O3,header,fileN1O3)
    fileN1O4 = f"./result/N1O4.csv"
    write_to_csv(N1O4,header,fileN1O4)
    fileN1O5 = f"./result/N1O5.csv"
    write_to_csv(N1O5,header,fileN1O5)
    fileN1O6 = f"./result/N1O6.csv"
    write_to_csv(N1O6,header,fileN1O6)
    fileN1O7 = f"./result/N1O7 .csv"
    write_to_csv(N1O7,header,fileN1O7)
    fileN1O8 = f"./result/N1O8.csv"
    write_to_csv(N1O8,header,fileN1O8)
    fileN1O9 = f"./result/N1O9.csv"
    write_to_csv(N1O9,header,fileN1O9)
    fileN1O10 = f"./result/N1O10.csv"
    write_to_csv(N1O10,header,fileN1O10)
    fileN1O11 = f"./result/N1O11.csv"
    write_to_csv(N1O11,header,fileN1O11)
    fileN1O12 = f"./result/N1O12.csv"
    write_to_csv(N1O12,header,fileN1O12)
    fileN1O13 = f"./result/N1O13.csv"
    write_to_csv(N1O13,header,fileN1O13)
    fileN1O14 = f"./result/N1O14.csv"
    write_to_csv(N1O14,header,fileN1O14)

    fileO3S1 = f"./result/O3S1.csv"
    write_to_csv(O3S1,header,fileO3S1)
    fileO4S1 = f"./result/O4S1.csv"
    write_to_csv(O4S1,header,fileO4S1)
    fileO5S1 = f"./result/O5S1.csv"
    write_to_csv(O5S1,header,fileO5S1)
    fileO6S1 = f"./result/O6S1.csv"
    write_to_csv(O6S1,header,fileO6S1)
    fileO7S1 = f"./result/O7S1.csv"
    write_to_csv(O7S1,header,fileO7S1)
    fileO8S1 = f"./result/O8S1.csv"
    write_to_csv(O8S1,header,fileO8S1)
    fileO9S1 = f"./result/O9S1.csv"
    write_to_csv(O9S1,header,fileO9S1)
    fileO10S1 = f"./result/O10S1.csv"
    write_to_csv(O10S1,header,fileO10S1)
    fileO11S1 = f"./result/O11S1.csv"
    write_to_csv(O11S1,header,fileO11S1)
    fileO12S1 = f"./result/O12S1.csv"
    write_to_csv(O12S1,header,fileO12S1)


if __name__ == '__main__':
    main()