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

def add_to_csv(data, file):
    with open(file, "a+") as f:
        csv_writer = csv.writer(f)
        for da in data:
            csv_writer.writerow(da)
        f.close()

def main():
    dbe1O2=dbe2O2=dbe3O2=dbe4O2=dbe5O2=dbe6O2=dbe7O2=dbe8O2=dbe9O2=dbe10O2=dbe11O2=dbe12O2=dbe13O2=dbe14O2=dbe15O2=dbe16O2=dbe17O2=dbe18O2=dbe19O2=dbe20O2=0
    dbe1O3 = dbe2O3 = dbe3O3 = dbe4O3 = dbe5O3 = dbe6O3 = dbe7O3 = dbe8O3 = dbe9O3 = dbe10O3 = dbe11O3 = dbe12O3 = dbe13O3 = dbe14O3 = dbe15O3 = dbe16O3 = dbe17O3 = dbe18O3 = dbe19O3 = dbe20O3 = 0
    dbe1O4 = dbe2O4 = dbe3O4 = dbe4O4 = dbe5O4 = dbe6O4 = dbe7O4 = dbe8O4 = dbe9O4 = dbe10O4 = dbe11O4 = dbe12O4 = dbe13O4 = dbe14O4 = dbe15O4 = dbe16O4 = dbe17O4 = dbe18O4 = dbe19O4 = dbe20O4 = 0
    dbe1O5 = dbe2O5 = dbe3O5 = dbe4O5 = dbe5O5 = dbe6O5 = dbe7O5 = dbe8O5 = dbe9O5 = dbe10O5 = dbe11O5 = dbe12O5 = dbe13O5 = dbe14O5 = dbe15O5 = dbe16O5 = dbe17O5 = dbe18O5 = dbe19O5 = dbe20O5 = 0
    dbe1O6 = dbe2O6 = dbe3O6 = dbe4O6 = dbe5O6 = dbe6O6 = dbe7O6 = dbe8O6 = dbe9O6 = dbe10O6 = dbe11O6 = dbe12O6 = dbe13O6 = dbe14O6 = dbe15O6 = dbe16O6 = dbe17O6 = dbe18O6 = dbe19O6 = dbe20O6 = 0
    dbe1O7 = dbe2O7 = dbe3O7 = dbe4O7 = dbe5O7 = dbe6O7 = dbe7O7 = dbe8O7 = dbe9O7 = dbe10O7 = dbe11O7 = dbe12O7 = dbe13O7 = dbe14O7 = dbe15O7 = dbe16O7 = dbe17O7 = dbe18O7 = dbe19O7 = dbe20O7 = 0
    dbe1O8 = dbe2O8 = dbe3O8 = dbe4O8 = dbe5O8 = dbe6O8 = dbe7O8 = dbe8O8 = dbe9O8 = dbe10O8 = dbe11O8 = dbe12O8 = dbe13O8 = dbe14O8 = dbe15O8 = dbe16O8 = dbe17O8 = dbe18O8 = dbe19O8 = dbe20O8 = 0
    dbe1O9 = dbe2O9 = dbe3O9 = dbe4O9 = dbe5O9 = dbe6O9 = dbe7O9 = dbe8O9 = dbe9O9 = dbe10O9 = dbe11O9 = dbe12O9 = dbe13O9 = dbe14O9 = dbe15O9 = dbe16O9 = dbe17O9 = dbe18O9 = dbe19O9 = dbe20O9 = 0
    dbe1O10 = dbe2O10 = dbe3O10 = dbe4O10 = dbe5O10 = dbe6O10 = dbe7O10 = dbe8O10 = dbe9O10 = dbe10O10 = dbe11O10 = dbe12O10 = dbe13O10 = dbe14O10 = dbe15O10 = dbe16O10 = dbe17O10 = dbe18O10 = dbe19O10 = dbe20O10 = 0
    dbe1O11 = dbe2O11 = dbe3O11 = dbe4O11 = dbe5O11 = dbe6O11 = dbe7O11 = dbe8O11 = dbe9O11 = dbe10O11 = dbe11O11 = dbe12O11 = dbe13O11 = dbe14O11 = dbe15O11 = dbe16O11 = dbe17O11 = dbe18O11 = dbe19O11 = dbe20O11 = 0
    dbe1O12 = dbe2O12 = dbe3O12 = dbe4O12 = dbe5O12 = dbe6O12 = dbe7O12 = dbe8O12 = dbe9O12 = dbe10O12 = dbe11O12 = dbe12O12 = dbe13O12 = dbe14O12 = dbe15O12 = dbe16O12 = dbe17O12 = dbe18O12 = dbe19O12 = dbe20O12 = 0
    dbe1O13 = dbe2O13 = dbe3O13 = dbe4O13 = dbe5O13 = dbe6O13 = dbe7O13 = dbe8O13 = dbe9O13 = dbe10O13 = dbe11O13 = dbe12O13 = dbe13O13 = dbe14O13 = dbe15O13 = dbe16O13 = dbe17O13 = dbe18O13 = dbe19O13 = dbe20O13 = 0
    dbe1O14 = dbe2O14 = dbe3O14 = dbe4O14 = dbe5O14 = dbe6O14 = dbe7O14 = dbe8O14 = dbe9O14 = dbe10O14 = dbe11O14 = dbe12O14 = dbe13O14 = dbe14O14 = dbe15O14 = dbe16O14 = dbe17O14 = dbe18O14 = dbe19O14 = dbe20O14 = 0
    dbe1O15 = dbe2O15 = dbe3O15 = dbe4O15 = dbe5O15 = dbe6O15 = dbe7O15 = dbe8O15 = dbe9O15 = dbe10O15 = dbe11O15 = dbe12O15 = dbe13O15 = dbe14O15 = dbe15O15 = dbe16O15 = dbe17O15 = dbe18O15 = dbe19O15 = dbe20O15 = 0
    dbe1O16 = dbe2O16 = dbe3O16 = dbe4O16 = dbe5O16 = dbe6O16 = dbe7O16 = dbe8O16 = dbe9O16 = dbe10O16 = dbe11O16 = dbe12O16 = dbe13O16 = dbe14O16 = dbe15O16 = dbe16O16 = dbe17O16 = dbe18O16 = dbe19O16 = dbe20O16 = 0

    intensityO2dbe1 = {}
    intensityO3dbe1 = {}
    intensityO4dbe1 = {}
    intensityO5dbe1 = {}
    intensityO6dbe1 = {}
    intensityO7dbe1 = {}
    intensityO8dbe1 = {}
    intensityO9dbe1 = {}
    intensityO10dbe1 = {}
    intensityO11dbe1 = {}
    intensityO12dbe1 = {}
    intensityO13dbe1 = {}
    intensityO14dbe1 = {}
    intensityO15dbe1 = {}
    intensityO16dbe1 = {}

    dataFile = "./data/1.csv"
    resultFile = "./result/result_new.csv"
    datas = read_from_csv(dataFile)
    for data in datas:
        # if eval(data[9]) == 0 and eval(data[11]) == 0:
        #     data.append(f"O{data[10]}")
        if eval(data[9]) == 0 and eval(data[11]) != 0:
            data.append(f"O{data[10]}S{data[11]}")
        elif eval(data[11]) == 0 and eval(data[9]) != 0:
            data.append(f"N{data[9]}O{data[10]}")
        else:
            data.append(f"O{data[10]}")
            # data.append(f"N{data[9]}O{data[10]}S{data[11]}")
    header = ["mSigma","ObservedIntens","ObservedM_z","calc_M_z","errMDa","errPpm","sumFormula","C","H","N","O","S","H1","HCraito","OCraito","CN2","NSP","abserrPpm"
              ,"sumintens","relativeintens","avemass","dbe_o","aimod","dbe","nosc","kmdch2","nkmch2","kmdh2","nkmh2","kmdh2o","nkmh2o","kmdo","nkmo","kmdcoo","nkmcoo","class"]
    write_to_csv(datas, header, resultFile)

    for data in datas:
        if eval(data[10])==2:
            if eval(data[23]) == 1:
                dbe1O2 += eval(data[1])
                intensityO2dbe1["dbe1"] = dbe1O2
            if eval(data[23]) == 2:
                dbe2O2 += eval(data[1])
                intensityO2dbe1["dbe2"] = dbe2O2
            if eval(data[23]) == 3:
                dbe3O2 += eval(data[1])
                intensityO2dbe1["dbe3"] = dbe3O2
            if eval(data[23]) == 4:
                dbe4O2 += eval(data[1])
                intensityO2dbe1["dbe4"] = dbe4O2
            if eval(data[23]) == 5:
                dbe5O2 += eval(data[1])
                intensityO2dbe1["dbe5"] = dbe5O2
            if eval(data[23]) == 6:
                dbe6O2 += eval(data[1])
                intensityO2dbe1["dbe6"] = dbe6O2
            if eval(data[23]) == 7:
                dbe7O2 += eval(data[1])
                intensityO2dbe1["dbe7"] = dbe7O2
            if eval(data[23]) == 8:
                dbe8O2 += eval(data[1])
                intensityO2dbe1["dbe8"] = dbe8O2
            if eval(data[23]) == 9:
                dbe9O2 += eval(data[1])
                intensityO2dbe1["dbe9"] = dbe9O2
            if eval(data[23]) == 10:
                dbe10O2 += eval(data[1])
                intensityO2dbe1["dbe10"] = dbe10O2
            if eval(data[23]) == 11:
                dbe11O2 += eval(data[1])
                intensityO2dbe1["dbe11"] = dbe11O2
            if eval(data[23]) == 12:
                dbe12O2 += eval(data[1])
                intensityO2dbe1["dbe12"] = dbe12O2
            if eval(data[23]) == 13:
                dbe13O2 += eval(data[1])
                intensityO2dbe1["dbe13"] = dbe13O2
            if eval(data[23]) == 14:
                dbe14O2 += eval(data[1])
                intensityO2dbe1["dbe14"] = dbe14O2
            if eval(data[23]) == 15:
                dbe15O2 += eval(data[1])
                intensityO2dbe1["dbe15"] = dbe15O2
            if eval(data[23]) == 16:
                dbe16O2 += eval(data[1])
                intensityO2dbe1["dbe16"] = dbe16O2
            if eval(data[23]) == 17:
                dbe17O2 += eval(data[1])
                intensityO2dbe1["dbe17"] = dbe17O2
            if eval(data[23]) == 18:
                dbe18O2 += eval(data[1])
                intensityO2dbe1["dbe18"] = dbe18O2
            if eval(data[23]) == 19:
                dbe19O2 += eval(data[1])
                intensityO2dbe1["dbe19"] = dbe19O2
            if eval(data[23]) == 20:
                dbe20O2 += eval(data[1])
                intensityO2dbe1["dbe20"] = dbe20O2
    print("O2类中各dbe强度之和为：")
    print(intensityO2dbe1)

    # print(intensity)
    # print(dbeO2)

    for data in datas:
        if eval(data[10])==3:
            if eval(data[23]) == 1:
                dbe1O3 += eval(data[1])
                intensityO3dbe1["dbe1"] = dbe1O3
            if eval(data[23]) == 2:
                dbe2O3 += eval(data[1])
                intensityO3dbe1["dbe2"] = dbe2O3
            if eval(data[23]) == 3:
                dbe3O3 += eval(data[1])
                intensityO3dbe1["dbe3"] = dbe3O3
            if eval(data[23]) == 4:
                dbe4O3 += eval(data[1])
                intensityO3dbe1["dbe4"] = dbe4O3
            if eval(data[23]) == 5:
                dbe5O3 += eval(data[1])
                intensityO3dbe1["dbe5"] = dbe5O3
            if eval(data[23]) == 6:
                dbe6O3 += eval(data[1])
                intensityO3dbe1["dbe6"] = dbe6O3
            if eval(data[23]) == 7:
                dbe7O3 += eval(data[1])
                intensityO3dbe1["dbe7"] = dbe7O3
            if eval(data[23]) == 8:
                dbe8O3 += eval(data[1])
                intensityO3dbe1["dbe8"] = dbe8O3
            if eval(data[23]) == 9:
                dbe9O3 += eval(data[1])
                intensityO3dbe1["dbe9"] = dbe9O3
            if eval(data[23]) == 10:
                dbe10O3 += eval(data[1])
                intensityO3dbe1["dbe10"] = dbe10O3
            if eval(data[23]) == 11:
                dbe11O3 += eval(data[1])
                intensityO3dbe1["dbe11"] = dbe11O3
            if eval(data[23]) == 12:
                dbe12O3 += eval(data[1])
                intensityO3dbe1["dbe12"] = dbe12O3
            if eval(data[23]) == 13:
                dbe13O3 += eval(data[1])
                intensityO3dbe1["dbe13"] = dbe13O3
            if eval(data[23]) == 14:
                dbe14O3 += eval(data[1])
                intensityO3dbe1["dbe14"] = dbe14O3
            if eval(data[23]) == 15:
                dbe15O3 += eval(data[1])
                intensityO3dbe1["dbe15"] = dbe15O3
            if eval(data[23]) == 16:
                dbe16O3 += eval(data[1])
                intensityO3dbe1["dbe16"] = dbe16O3
            if eval(data[23]) == 17:
                dbe17O3 += eval(data[1])
                intensityO3dbe1["dbe17"] = dbe17O3
            if eval(data[23]) == 18:
                dbe18O3 += eval(data[1])
                intensityO3dbe1["dbe18"] = dbe18O3
            if eval(data[23]) == 19:
                dbe19O3 += eval(data[1])
                intensityO3dbe1["dbe19"] = dbe19O3
            if eval(data[23]) == 20:
                dbe20O3 += eval(data[1])
                intensityO3dbe1["dbe20"] = dbe20O3
    print("O3类中各dbe强度之和为：")
    print(intensityO3dbe1)


    for data in datas:
        if eval(data[10])==4:
            if eval(data[23]) == 1:
                dbe1O4 += eval(data[1])
                intensityO4dbe1["dbe1"] = dbe1O4
            if eval(data[23]) == 2:
                dbe2O4 += eval(data[1])
                intensityO4dbe1["dbe2"] = dbe2O4
            if eval(data[23]) == 3:
                dbe3O4 += eval(data[1])
                intensityO4dbe1["dbe3"] = dbe3O4
            if eval(data[23]) == 4:
                dbe4O4 += eval(data[1])
                intensityO4dbe1["dbe4"] = dbe4O4
            if eval(data[23]) == 5:
                dbe5O4 += eval(data[1])
                intensityO4dbe1["dbe5"] = dbe5O4
            if eval(data[23]) == 6:
                dbe6O4 += eval(data[1])
                intensityO4dbe1["dbe6"] = dbe6O4
            if eval(data[23]) == 7:
                dbe7O4 += eval(data[1])
                intensityO4dbe1["dbe7"] = dbe7O4
            if eval(data[23]) == 8:
                dbe8O4 += eval(data[1])
                intensityO4dbe1["dbe8"] = dbe8O4
            if eval(data[23]) == 9:
                dbe9O4 += eval(data[1])
                intensityO4dbe1["dbe9"] = dbe9O4
            if eval(data[23]) == 10:
                dbe10O4 += eval(data[1])
                intensityO4dbe1["dbe10"] = dbe10O4
            if eval(data[23]) == 11:
                dbe11O4 += eval(data[1])
                intensityO4dbe1["dbe11"] = dbe11O4
            if eval(data[23]) == 12:
                dbe12O4 += eval(data[1])
                intensityO4dbe1["dbe12"] = dbe12O4
            if eval(data[23]) == 13:
                dbe13O4 += eval(data[1])
                intensityO4dbe1["dbe13"] = dbe13O4
            if eval(data[23]) == 14:
                dbe14O4 += eval(data[1])
                intensityO4dbe1["dbe14"] = dbe14O4
            if eval(data[23]) == 15:
                dbe15O4 += eval(data[1])
                intensityO4dbe1["dbe15"] = dbe15O4
            if eval(data[23]) == 16:
                dbe16O4 += eval(data[1])
                intensityO4dbe1["dbe16"] = dbe16O4
            if eval(data[23]) == 17:
                dbe17O4 += eval(data[1])
                intensityO4dbe1["dbe17"] = dbe17O4
            if eval(data[23]) == 18:
                dbe18O4 += eval(data[1])
                intensityO4dbe1["dbe18"] = dbe18O4
            if eval(data[23]) == 19:
                dbe19O4 += eval(data[1])
                intensityO4dbe1["dbe19"] = dbe19O4
            if eval(data[23]) == 20:
                dbe20O4 += eval(data[1])
                intensityO4dbe1["dbe20"] = dbe20O4
    print("O4类中各dbe强度之和为：")
    print(intensityO4dbe1)

    for data in datas:
        if eval(data[10])==5:
            if eval(data[23]) == 1:
                dbe1O5 += eval(data[1])
                intensityO5dbe1["dbe1"] = dbe1O5
            if eval(data[23]) == 2:
                dbe2O5 += eval(data[1])
                intensityO5dbe1["dbe2"] = dbe2O5
            if eval(data[23]) == 3:
                dbe3O5 += eval(data[1])
                intensityO5dbe1["dbe3"] = dbe3O5
            if eval(data[23]) == 4:
                dbe4O5 += eval(data[1])
                intensityO5dbe1["dbe4"] = dbe4O5
            if eval(data[23]) == 5:
                dbe5O5 += eval(data[1])
                intensityO5dbe1["dbe5"] = dbe5O5
            if eval(data[23]) == 6:
                dbe6O5 += eval(data[1])
                intensityO5dbe1["dbe6"] = dbe6O5
            if eval(data[23]) == 7:
                dbe7O5 += eval(data[1])
                intensityO5dbe1["dbe7"] = dbe7O5
            if eval(data[23]) == 8:
                dbe8O5 += eval(data[1])
                intensityO5dbe1["dbe8"] = dbe8O5
            if eval(data[23]) == 9:
                dbe9O5 += eval(data[1])
                intensityO5dbe1["dbe9"] = dbe9O5
            if eval(data[23]) == 10:
                dbe10O5 += eval(data[1])
                intensityO5dbe1["dbe10"] = dbe10O5
            if eval(data[23]) == 11:
                dbe11O5 += eval(data[1])
                intensityO5dbe1["dbe11"] = dbe11O5
            if eval(data[23]) == 12:
                dbe12O5 += eval(data[1])
                intensityO5dbe1["dbe12"] = dbe12O5
            if eval(data[23]) == 13:
                dbe13O5 += eval(data[1])
                intensityO5dbe1["dbe13"] = dbe13O5
            if eval(data[23]) == 14:
                dbe14O5 += eval(data[1])
                intensityO5dbe1["dbe14"] = dbe14O5
            if eval(data[23]) == 15:
                dbe15O5 += eval(data[1])
                intensityO5dbe1["dbe15"] = dbe15O5
            if eval(data[23]) == 16:
                dbe16O5 += eval(data[1])
                intensityO5dbe1["dbe16"] = dbe16O5
            if eval(data[23]) == 17:
                dbe17O5 += eval(data[1])
                intensityO5dbe1["dbe17"] = dbe17O5
            if eval(data[23]) == 18:
                dbe18O5 += eval(data[1])
                intensityO5dbe1["dbe18"] = dbe18O5
            if eval(data[23]) == 19:
                dbe19O5 += eval(data[1])
                intensityO5dbe1["dbe19"] = dbe19O5
            if eval(data[23]) == 20:
                dbe20O5 += eval(data[1])
                intensityO5dbe1["dbe20"] = dbe20O5
    print("O5类中各dbe强度之和为：")
    print(intensityO5dbe1)

    for data in datas:
        if eval(data[10])==6:
            if eval(data[23]) == 1:
                dbe1O6 += eval(data[1])
                intensityO6dbe1["dbe1"] = dbe1O6
            if eval(data[23]) == 2:
                dbe2O6 += eval(data[1])
                intensityO6dbe1["dbe2"] = dbe2O6
            if eval(data[23]) == 3:
                dbe3O6 += eval(data[1])
                intensityO6dbe1["dbe3"] = dbe3O6
            if eval(data[23]) == 4:
                dbe4O6 += eval(data[1])
                intensityO6dbe1["dbe4"] = dbe4O6
            if eval(data[23]) == 5:
                dbe5O6 += eval(data[1])
                intensityO6dbe1["dbe5"] = dbe5O6
            if eval(data[23]) == 6:
                dbe6O6 += eval(data[1])
                intensityO6dbe1["dbe6"] = dbe6O6
            if eval(data[23]) == 7:
                dbe7O6 += eval(data[1])
                intensityO6dbe1["dbe7"] = dbe7O6
            if eval(data[23]) == 8:
                dbe8O6 += eval(data[1])
                intensityO6dbe1["dbe8"] = dbe8O6
            if eval(data[23]) == 9:
                dbe9O6 += eval(data[1])
                intensityO6dbe1["dbe9"] = dbe9O6
            if eval(data[23]) == 10:
                dbe10O6 += eval(data[1])
                intensityO6dbe1["dbe10"] = dbe10O6
            if eval(data[23]) == 11:
                dbe11O6 += eval(data[1])
                intensityO6dbe1["dbe11"] = dbe11O6
            if eval(data[23]) == 12:
                dbe12O6 += eval(data[1])
                intensityO6dbe1["dbe12"] = dbe12O6
            if eval(data[23]) == 13:
                dbe13O6 += eval(data[1])
                intensityO6dbe1["dbe13"] = dbe13O6
            if eval(data[23]) == 14:
                dbe14O6 += eval(data[1])
                intensityO6dbe1["dbe14"] = dbe14O6
            if eval(data[23]) == 15:
                dbe15O6 += eval(data[1])
                intensityO6dbe1["dbe15"] = dbe15O6
            if eval(data[23]) == 16:
                dbe16O6 += eval(data[1])
                intensityO6dbe1["dbe16"] = dbe16O6
            if eval(data[23]) == 17:
                dbe17O6 += eval(data[1])
                intensityO6dbe1["dbe17"] = dbe17O6
            if eval(data[23]) == 18:
                dbe18O6 += eval(data[1])
                intensityO6dbe1["dbe18"] = dbe18O6
            if eval(data[23]) == 19:
                dbe19O6 += eval(data[1])
                intensityO6dbe1["dbe19"] = dbe19O6
            if eval(data[23]) == 20:
                dbe20O6 += eval(data[1])
                intensityO6dbe1["dbe20"] = dbe20O6
    print("O6类中各dbe强度之和为：")
    print(intensityO6dbe1)

    for data in datas:
        if eval(data[10])==7:
            if eval(data[23]) == 1:
                dbe1O7 += eval(data[1])
                intensityO7dbe1["dbe1"] = dbe1O7
            if eval(data[23]) == 2:
                dbe2O7 += eval(data[1])
                intensityO7dbe1["dbe2"] = dbe2O7
            if eval(data[23]) == 3:
                dbe3O7 += eval(data[1])
                intensityO7dbe1["dbe3"] = dbe3O7
            if eval(data[23]) == 4:
                dbe4O7 += eval(data[1])
                intensityO7dbe1["dbe4"] = dbe4O7
            if eval(data[23]) == 5:
                dbe5O7 += eval(data[1])
                intensityO7dbe1["dbe5"] = dbe5O7
            if eval(data[23]) == 6:
                dbe6O7 += eval(data[1])
                intensityO7dbe1["dbe6"] = dbe6O7
            if eval(data[23]) == 7:
                dbe7O7 += eval(data[1])
                intensityO7dbe1["dbe7"] = dbe7O7
            if eval(data[23]) == 8:
                dbe8O7 += eval(data[1])
                intensityO7dbe1["dbe8"] = dbe8O7
            if eval(data[23]) == 9:
                dbe9O7 += eval(data[1])
                intensityO7dbe1["dbe9"] = dbe9O7
            if eval(data[23]) == 10:
                dbe10O7 += eval(data[1])
                intensityO7dbe1["dbe10"] = dbe10O7
            if eval(data[23]) == 11:
                dbe11O7 += eval(data[1])
                intensityO7dbe1["dbe11"] = dbe11O7
            if eval(data[23]) == 12:
                dbe12O7 += eval(data[1])
                intensityO7dbe1["dbe12"] = dbe12O7
            if eval(data[23]) == 13:
                dbe13O7 += eval(data[1])
                intensityO7dbe1["dbe13"] = dbe13O7
            if eval(data[23]) == 14:
                dbe14O7 += eval(data[1])
                intensityO7dbe1["dbe14"] = dbe14O7
            if eval(data[23]) == 15:
                dbe15O7 += eval(data[1])
                intensityO7dbe1["dbe15"] = dbe15O7
            if eval(data[23]) == 16:
                dbe16O7 += eval(data[1])
                intensityO7dbe1["dbe16"] = dbe16O7
            if eval(data[23]) == 17:
                dbe17O7 += eval(data[1])
                intensityO7dbe1["dbe17"] = dbe17O7
            if eval(data[23]) == 18:
                dbe18O7 += eval(data[1])
                intensityO7dbe1["dbe18"] = dbe18O7
            if eval(data[23]) == 19:
                dbe19O7 += eval(data[1])
                intensityO7dbe1["dbe19"] = dbe19O7
            if eval(data[23]) == 20:
                dbe20O7 += eval(data[1])
                intensityO7dbe1["dbe20"] = dbe20O7
    print("O7类中各dbe强度之和为：")
    print(intensityO7dbe1)

    for data in datas:
        if eval(data[10])==8:
            if eval(data[23]) == 1:
                dbe1O8 += eval(data[1])
                intensityO8dbe1["dbe1"] = dbe1O8
            if eval(data[23]) == 2:
                dbe2O8 += eval(data[1])
                intensityO8dbe1["dbe2"] = dbe2O8
            if eval(data[23]) == 3:
                dbe3O8 += eval(data[1])
                intensityO8dbe1["dbe3"] = dbe3O8
            if eval(data[23]) == 4:
                dbe4O8 += eval(data[1])
                intensityO8dbe1["dbe4"] = dbe4O8
            if eval(data[23]) == 5:
                dbe5O8 += eval(data[1])
                intensityO8dbe1["dbe5"] = dbe5O8
            if eval(data[23]) == 6:
                dbe6O8 += eval(data[1])
                intensityO8dbe1["dbe6"] = dbe6O8
            if eval(data[23]) == 7:
                dbe7O8 += eval(data[1])
                intensityO8dbe1["dbe7"] = dbe7O8
            if eval(data[23]) == 8:
                dbe8O8 += eval(data[1])
                intensityO8dbe1["dbe8"] = dbe8O8
            if eval(data[23]) == 9:
                dbe9O8 += eval(data[1])
                intensityO8dbe1["dbe9"] = dbe9O8
            if eval(data[23]) == 10:
                dbe10O8 += eval(data[1])
                intensityO8dbe1["dbe10"] = dbe10O8
            if eval(data[23]) == 11:
                dbe11O8 += eval(data[1])
                intensityO8dbe1["dbe11"] = dbe11O8
            if eval(data[23]) == 12:
                dbe12O8 += eval(data[1])
                intensityO8dbe1["dbe12"] = dbe12O8
            if eval(data[23]) == 13:
                dbe13O8 += eval(data[1])
                intensityO8dbe1["dbe13"] = dbe13O8
            if eval(data[23]) == 14:
                dbe14O8 += eval(data[1])
                intensityO8dbe1["dbe14"] = dbe14O8
            if eval(data[23]) == 15:
                dbe15O8 += eval(data[1])
                intensityO8dbe1["dbe15"] = dbe15O8
            if eval(data[23]) == 16:
                dbe16O8 += eval(data[1])
                intensityO8dbe1["dbe16"] = dbe16O8
            if eval(data[23]) == 17:
                dbe17O8 += eval(data[1])
                intensityO8dbe1["dbe17"] = dbe17O8
            if eval(data[23]) == 18:
                dbe18O8 += eval(data[1])
                intensityO8dbe1["dbe18"] = dbe18O8
            if eval(data[23]) == 19:
                dbe19O8 += eval(data[1])
                intensityO8dbe1["dbe19"] = dbe19O8
            if eval(data[23]) == 20:
                dbe20O8 += eval(data[1])
                intensityO8dbe1["dbe20"] = dbe20O8
    print("O8类中各dbe强度之和为：")
    print(intensityO8dbe1)

    for data in datas:
        if eval(data[10])==9:
            if eval(data[23]) == 1:
                dbe1O9 += eval(data[1])
                intensityO9dbe1["dbe1"] = dbe1O9
            if eval(data[23]) == 2:
                dbe2O9 += eval(data[1])
                intensityO9dbe1["dbe2"] = dbe2O9
            if eval(data[23]) == 3:
                dbe3O9 += eval(data[1])
                intensityO9dbe1["dbe3"] = dbe3O9
            if eval(data[23]) == 4:
                dbe4O9 += eval(data[1])
                intensityO9dbe1["dbe4"] = dbe4O9
            if eval(data[23]) == 5:
                dbe5O9 += eval(data[1])
                intensityO9dbe1["dbe5"] = dbe5O9
            if eval(data[23]) == 6:
                dbe6O9 += eval(data[1])
                intensityO9dbe1["dbe6"] = dbe6O9
            if eval(data[23]) == 7:
                dbe7O9 += eval(data[1])
                intensityO9dbe1["dbe7"] = dbe7O9
            if eval(data[23]) == 8:
                dbe8O9 += eval(data[1])
                intensityO9dbe1["dbe8"] = dbe8O9
            if eval(data[23]) == 9:
                dbe9O9 += eval(data[1])
                intensityO9dbe1["dbe9"] = dbe9O9
            if eval(data[23]) == 10:
                dbe10O9 += eval(data[1])
                intensityO9dbe1["dbe10"] = dbe10O9
            if eval(data[23]) == 11:
                dbe11O9 += eval(data[1])
                intensityO9dbe1["dbe11"] = dbe11O9
            if eval(data[23]) == 12:
                dbe12O9 += eval(data[1])
                intensityO9dbe1["dbe12"] = dbe12O9
            if eval(data[23]) == 13:
                dbe13O9 += eval(data[1])
                intensityO9dbe1["dbe13"] = dbe13O9
            if eval(data[23]) == 14:
                dbe14O9 += eval(data[1])
                intensityO9dbe1["dbe14"] = dbe14O9
            if eval(data[23]) == 15:
                dbe15O9 += eval(data[1])
                intensityO9dbe1["dbe15"] = dbe15O9
            if eval(data[23]) == 16:
                dbe16O9 += eval(data[1])
                intensityO9dbe1["dbe16"] = dbe16O9
            if eval(data[23]) == 17:
                dbe17O9 += eval(data[1])
                intensityO9dbe1["dbe17"] = dbe17O9
            if eval(data[23]) == 18:
                dbe18O9 += eval(data[1])
                intensityO9dbe1["dbe18"] = dbe18O9
            if eval(data[23]) == 19:
                dbe19O9 += eval(data[1])
                intensityO9dbe1["dbe19"] = dbe19O9
            if eval(data[23]) == 20:
                dbe20O9 += eval(data[1])
                intensityO9dbe1["dbe20"] = dbe20O9
    print("O9类中各dbe强度之和为：")
    print(intensityO9dbe1)

    for data in datas:
        if eval(data[10])==10:
            if eval(data[23]) == 1:
                dbe1O10 += eval(data[1])
                intensityO10dbe1["dbe1"] = dbe1O10
            if eval(data[23]) == 2:
                dbe2O10 += eval(data[1])
                intensityO10dbe1["dbe2"] = dbe2O10
            if eval(data[23]) == 3:
                dbe3O10 += eval(data[1])
                intensityO10dbe1["dbe3"] = dbe3O10
            if eval(data[23]) == 4:
                dbe4O10 += eval(data[1])
                intensityO10dbe1["dbe4"] = dbe4O10
            if eval(data[23]) == 5:
                dbe5O10 += eval(data[1])
                intensityO10dbe1["dbe5"] = dbe5O10
            if eval(data[23]) == 6:
                dbe6O10 += eval(data[1])
                intensityO10dbe1["dbe6"] = dbe6O10
            if eval(data[23]) == 7:
                dbe7O10 += eval(data[1])
                intensityO10dbe1["dbe7"] = dbe7O10
            if eval(data[23]) == 8:
                dbe8O10 += eval(data[1])
                intensityO10dbe1["dbe8"] = dbe8O10
            if eval(data[23]) == 9:
                dbe9O10 += eval(data[1])
                intensityO10dbe1["dbe9"] = dbe9O10
            if eval(data[23]) == 10:
                dbe10O10 += eval(data[1])
                intensityO10dbe1["dbe10"] = dbe10O10
            if eval(data[23]) == 11:
                dbe11O10 += eval(data[1])
                intensityO10dbe1["dbe11"] = dbe11O10
            if eval(data[23]) == 12:
                dbe12O10 += eval(data[1])
                intensityO10dbe1["dbe12"] = dbe12O10
            if eval(data[23]) == 13:
                dbe13O10 += eval(data[1])
                intensityO10dbe1["dbe13"] = dbe13O10
            if eval(data[23]) == 14:
                dbe14O10 += eval(data[1])
                intensityO10dbe1["dbe14"] = dbe14O10
            if eval(data[23]) == 15:
                dbe15O10 += eval(data[1])
                intensityO10dbe1["dbe15"] = dbe15O10
            if eval(data[23]) == 16:
                dbe16O10 += eval(data[1])
                intensityO10dbe1["dbe16"] = dbe16O10
            if eval(data[23]) == 17:
                dbe17O10 += eval(data[1])
                intensityO10dbe1["dbe17"] = dbe17O10
            if eval(data[23]) == 18:
                dbe18O10 += eval(data[1])
                intensityO10dbe1["dbe18"] = dbe18O10
            if eval(data[23]) == 19:
                dbe19O10 += eval(data[1])
                intensityO10dbe1["dbe19"] = dbe19O10
            if eval(data[23]) == 20:
                dbe20O10 += eval(data[1])
                intensityO10dbe1["dbe20"] = dbe20O10
    print("O10类中各dbe强度之和为：")
    print(intensityO10dbe1)

    for data in datas:
        if eval(data[10])==11:
            if eval(data[23]) == 1:
                dbe1O11 += eval(data[1])
                intensityO11dbe1["dbe1"] = dbe1O11
            if eval(data[23]) == 2:
                dbe2O11 += eval(data[1])
                intensityO11dbe1["dbe2"] = dbe2O11
            if eval(data[23]) == 3:
                dbe3O11 += eval(data[1])
                intensityO11dbe1["dbe3"] = dbe3O11
            if eval(data[23]) == 4:
                dbe4O11 += eval(data[1])
                intensityO11dbe1["dbe4"] = dbe4O11
            if eval(data[23]) == 5:
                dbe5O11 += eval(data[1])
                intensityO11dbe1["dbe5"] = dbe5O11
            if eval(data[23]) == 6:
                dbe6O11 += eval(data[1])
                intensityO11dbe1["dbe6"] = dbe6O11
            if eval(data[23]) == 7:
                dbe7O11 += eval(data[1])
                intensityO11dbe1["dbe7"] = dbe7O11
            if eval(data[23]) == 8:
                dbe8O11 += eval(data[1])
                intensityO11dbe1["dbe8"] = dbe8O11
            if eval(data[23]) == 9:
                dbe9O11 += eval(data[1])
                intensityO11dbe1["dbe9"] = dbe9O11
            if eval(data[23]) == 10:
                dbe10O11 += eval(data[1])
                intensityO11dbe1["dbe10"] = dbe10O11
            if eval(data[23]) == 11:
                dbe11O11 += eval(data[1])
                intensityO11dbe1["dbe11"] = dbe11O11
            if eval(data[23]) == 12:
                dbe12O11 += eval(data[1])
                intensityO11dbe1["dbe12"] = dbe12O11
            if eval(data[23]) == 13:
                dbe13O11 += eval(data[1])
                intensityO11dbe1["dbe13"] = dbe13O11
            if eval(data[23]) == 14:
                dbe14O11 += eval(data[1])
                intensityO11dbe1["dbe14"] = dbe14O11
            if eval(data[23]) == 15:
                dbe15O11 += eval(data[1])
                intensityO11dbe1["dbe15"] = dbe15O11
            if eval(data[23]) == 16:
                dbe16O11 += eval(data[1])
                intensityO11dbe1["dbe16"] = dbe16O11
            if eval(data[23]) == 17:
                dbe17O11 += eval(data[1])
                intensityO11dbe1["dbe17"] = dbe17O11
            if eval(data[23]) == 18:
                dbe18O11 += eval(data[1])
                intensityO11dbe1["dbe18"] = dbe18O11
            if eval(data[23]) == 19:
                dbe19O11 += eval(data[1])
                intensityO11dbe1["dbe19"] = dbe19O11
            if eval(data[23]) == 20:
                dbe20O11 += eval(data[1])
                intensityO11dbe1["dbe20"] = dbe20O11
    print("O11类中各dbe强度之和为：")
    print(intensityO11dbe1)

    for data in datas:
        if eval(data[10])==12:
            if eval(data[23]) == 1:
                dbe1O12 += eval(data[1])
                intensityO12dbe1["dbe1"] = dbe1O12
            if eval(data[23]) == 2:
                dbe2O12 += eval(data[1])
                intensityO12dbe1["dbe2"] = dbe2O12
            if eval(data[23]) == 3:
                dbe3O12 += eval(data[1])
                intensityO12dbe1["dbe3"] = dbe3O12
            if eval(data[23]) == 4:
                dbe4O12 += eval(data[1])
                intensityO12dbe1["dbe4"] = dbe4O12
            if eval(data[23]) == 5:
                dbe5O12 += eval(data[1])
                intensityO12dbe1["dbe5"] = dbe5O12
            if eval(data[23]) == 6:
                dbe6O12 += eval(data[1])
                intensityO12dbe1["dbe6"] = dbe6O12
            if eval(data[23]) == 7:
                dbe7O12 += eval(data[1])
                intensityO12dbe1["dbe7"] = dbe7O12
            if eval(data[23]) == 8:
                dbe8O12 += eval(data[1])
                intensityO12dbe1["dbe8"] = dbe8O12
            if eval(data[23]) == 9:
                dbe9O12 += eval(data[1])
                intensityO12dbe1["dbe9"] = dbe9O12
            if eval(data[23]) == 10:
                dbe10O12 += eval(data[1])
                intensityO12dbe1["dbe10"] = dbe10O12
            if eval(data[23]) == 11:
                dbe11O12 += eval(data[1])
                intensityO12dbe1["dbe11"] = dbe11O12
            if eval(data[23]) == 12:
                dbe12O12 += eval(data[1])
                intensityO12dbe1["dbe12"] = dbe12O12
            if eval(data[23]) == 13:
                dbe13O12 += eval(data[1])
                intensityO12dbe1["dbe13"] = dbe13O12
            if eval(data[23]) == 14:
                dbe14O12 += eval(data[1])
                intensityO12dbe1["dbe14"] = dbe14O12
            if eval(data[23]) == 15:
                dbe15O12 += eval(data[1])
                intensityO12dbe1["dbe15"] = dbe15O12
            if eval(data[23]) == 16:
                dbe16O12 += eval(data[1])
                intensityO12dbe1["dbe16"] = dbe16O12
            if eval(data[23]) == 17:
                dbe17O12 += eval(data[1])
                intensityO12dbe1["dbe17"] = dbe17O12
            if eval(data[23]) == 18:
                dbe18O12 += eval(data[1])
                intensityO12dbe1["dbe18"] = dbe18O12
            if eval(data[23]) == 19:
                dbe19O12 += eval(data[1])
                intensityO12dbe1["dbe19"] = dbe19O12
            if eval(data[23]) == 20:
                dbe20O12 += eval(data[1])
                intensityO12dbe1["dbe20"] = dbe20O12
    print("O12类中各dbe强度之和为：")
    print(intensityO12dbe1)


    for data in datas:
        if eval(data[10])==13:
            if eval(data[23]) == 1:
                dbe1O13 += eval(data[1])
                intensityO13dbe1["dbe1"] = dbe1O13
            if eval(data[23]) == 2:
                dbe2O13 += eval(data[1])
                intensityO13dbe1["dbe2"] = dbe2O13
            if eval(data[23]) == 3:
                dbe3O13 += eval(data[1])
                intensityO13dbe1["dbe3"] = dbe3O13
            if eval(data[23]) == 4:
                dbe4O13 += eval(data[1])
                intensityO13dbe1["dbe4"] = dbe4O13
            if eval(data[23]) == 5:
                dbe5O13 += eval(data[1])
                intensityO13dbe1["dbe5"] = dbe5O13
            if eval(data[23]) == 6:
                dbe6O13 += eval(data[1])
                intensityO13dbe1["dbe6"] = dbe6O13
            if eval(data[23]) == 7:
                dbe7O13 += eval(data[1])
                intensityO13dbe1["dbe7"] = dbe7O13
            if eval(data[23]) == 8:
                dbe8O13 += eval(data[1])
                intensityO13dbe1["dbe8"] = dbe8O13
            if eval(data[23]) == 9:
                dbe9O13 += eval(data[1])
                intensityO13dbe1["dbe9"] = dbe9O13
            if eval(data[23]) == 10:
                dbe10O13 += eval(data[1])
                intensityO13dbe1["dbe10"] = dbe10O13
            if eval(data[23]) == 11:
                dbe11O13 += eval(data[1])
                intensityO13dbe1["dbe11"] = dbe11O13
            if eval(data[23]) == 12:
                dbe12O13 += eval(data[1])
                intensityO13dbe1["dbe12"] = dbe12O13
            if eval(data[23]) == 13:
                dbe13O13 += eval(data[1])
                intensityO13dbe1["dbe13"] = dbe13O13
            if eval(data[23]) == 14:
                dbe14O13 += eval(data[1])
                intensityO13dbe1["dbe14"] = dbe14O13
            if eval(data[23]) == 15:
                dbe15O13 += eval(data[1])
                intensityO13dbe1["dbe15"] = dbe15O13
            if eval(data[23]) == 16:
                dbe16O13 += eval(data[1])
                intensityO13dbe1["dbe16"] = dbe16O13
            if eval(data[23]) == 17:
                dbe17O13 += eval(data[1])
                intensityO13dbe1["dbe17"] = dbe17O13
            if eval(data[23]) == 18:
                dbe18O13 += eval(data[1])
                intensityO13dbe1["dbe18"] = dbe18O13
            if eval(data[23]) == 19:
                dbe19O13 += eval(data[1])
                intensityO13dbe1["dbe19"] = dbe19O13
            if eval(data[23]) == 20:
                dbe20O13 += eval(data[1])
                intensityO13dbe1["dbe20"] = dbe20O13
    print("O13类中各dbe强度之和为：")
    print(intensityO13dbe1)


    for data in datas:
        if eval(data[10])==14:
            if eval(data[23]) == 1:
                dbe1O14 += eval(data[1])
                intensityO14dbe1["dbe1"] = dbe1O14
            if eval(data[23]) == 2:
                dbe2O14 += eval(data[1])
                intensityO14dbe1["dbe2"] = dbe2O14
            if eval(data[23]) == 3:
                dbe3O14 += eval(data[1])
                intensityO14dbe1["dbe3"] = dbe3O14
            if eval(data[23]) == 4:
                dbe4O14 += eval(data[1])
                intensityO14dbe1["dbe4"] = dbe4O14
            if eval(data[23]) == 5:
                dbe5O14 += eval(data[1])
                intensityO14dbe1["dbe5"] = dbe5O14
            if eval(data[23]) == 6:
                dbe6O14 += eval(data[1])
                intensityO14dbe1["dbe6"] = dbe6O14
            if eval(data[23]) == 7:
                dbe7O14 += eval(data[1])
                intensityO14dbe1["dbe7"] = dbe7O14
            if eval(data[23]) == 8:
                dbe8O14 += eval(data[1])
                intensityO14dbe1["dbe8"] = dbe8O14
            if eval(data[23]) == 9:
                dbe9O14 += eval(data[1])
                intensityO14dbe1["dbe9"] = dbe9O14
            if eval(data[23]) == 10:
                dbe10O14 += eval(data[1])
                intensityO14dbe1["dbe10"] = dbe10O14
            if eval(data[23]) == 11:
                dbe11O14 += eval(data[1])
                intensityO14dbe1["dbe11"] = dbe11O14
            if eval(data[23]) == 12:
                dbe12O14 += eval(data[1])
                intensityO14dbe1["dbe12"] = dbe12O14
            if eval(data[23]) == 13:
                dbe13O14 += eval(data[1])
                intensityO14dbe1["dbe13"] = dbe13O14
            if eval(data[23]) == 14:
                dbe14O14 += eval(data[1])
                intensityO14dbe1["dbe14"] = dbe14O14
            if eval(data[23]) == 15:
                dbe15O14 += eval(data[1])
                intensityO14dbe1["dbe15"] = dbe15O14
            if eval(data[23]) == 16:
                dbe16O14 += eval(data[1])
                intensityO14dbe1["dbe16"] = dbe16O14
            if eval(data[23]) == 17:
                dbe17O14 += eval(data[1])
                intensityO14dbe1["dbe17"] = dbe17O14
            if eval(data[23]) == 18:
                dbe18O14 += eval(data[1])
                intensityO14dbe1["dbe18"] = dbe18O14
            if eval(data[23]) == 19:
                dbe19O14 += eval(data[1])
                intensityO14dbe1["dbe19"] = dbe19O14
            if eval(data[23]) == 20:
                dbe20O14 += eval(data[1])
                intensityO14dbe1["dbe20"] = dbe20O14
    print("O14类中各dbe强度之和为：")
    print(intensityO14dbe1)

    for data in datas:
        if eval(data[10])==15:
            if eval(data[23]) == 1:
                dbe1O15 += eval(data[1])
                intensityO15dbe1["dbe1"] = dbe1O15
            if eval(data[23]) == 2:
                dbe2O15 += eval(data[1])
                intensityO15dbe1["dbe2"] = dbe2O15
            if eval(data[23]) == 3:
                dbe3O15 += eval(data[1])
                intensityO15dbe1["dbe3"] = dbe3O15
            if eval(data[23]) == 4:
                dbe4O15 += eval(data[1])
                intensityO15dbe1["dbe4"] = dbe4O15
            if eval(data[23]) == 5:
                dbe5O15 += eval(data[1])
                intensityO15dbe1["dbe5"] = dbe5O15
            if eval(data[23]) == 6:
                dbe6O15 += eval(data[1])
                intensityO15dbe1["dbe6"] = dbe6O15
            if eval(data[23]) == 7:
                dbe7O15 += eval(data[1])
                intensityO15dbe1["dbe7"] = dbe7O15
            if eval(data[23]) == 8:
                dbe8O15 += eval(data[1])
                intensityO15dbe1["dbe8"] = dbe8O15
            if eval(data[23]) == 9:
                dbe9O15 += eval(data[1])
                intensityO15dbe1["dbe9"] = dbe9O15
            if eval(data[23]) == 10:
                dbe10O15 += eval(data[1])
                intensityO15dbe1["dbe10"] = dbe10O15
            if eval(data[23]) == 11:
                dbe11O15 += eval(data[1])
                intensityO15dbe1["dbe11"] = dbe11O15
            if eval(data[23]) == 12:
                dbe12O15 += eval(data[1])
                intensityO15dbe1["dbe12"] = dbe12O15
            if eval(data[23]) == 13:
                dbe13O15 += eval(data[1])
                intensityO15dbe1["dbe13"] = dbe13O15
            if eval(data[23]) == 14:
                dbe14O15 += eval(data[1])
                intensityO15dbe1["dbe14"] = dbe14O15
            if eval(data[23]) == 15:
                dbe15O15 += eval(data[1])
                intensityO15dbe1["dbe15"] = dbe15O15
            if eval(data[23]) == 16:
                dbe16O15 += eval(data[1])
                intensityO15dbe1["dbe16"] = dbe16O15
            if eval(data[23]) == 17:
                dbe17O15 += eval(data[1])
                intensityO15dbe1["dbe17"] = dbe17O15
            if eval(data[23]) == 18:
                dbe18O15 += eval(data[1])
                intensityO15dbe1["dbe18"] = dbe18O15
            if eval(data[23]) == 19:
                dbe19O15 += eval(data[1])
                intensityO15dbe1["dbe19"] = dbe19O15
            if eval(data[23]) == 20:
                dbe20O15 += eval(data[1])
                intensityO15dbe1["dbe20"] = dbe20O15
    print("O15类中各dbe强度之和为：")
    print(intensityO15dbe1)

    for data in datas:
        if eval(data[10])==16:
            if eval(data[23]) == 1:
                dbe1O16 += eval(data[1])
                intensityO16dbe1["dbe1"] = dbe1O16
            if eval(data[23]) == 2:
                dbe2O16 += eval(data[1])
                intensityO16dbe1["dbe2"] = dbe2O16
            if eval(data[23]) == 3:
                dbe3O16 += eval(data[1])
                intensityO16dbe1["dbe3"] = dbe3O16
            if eval(data[23]) == 4:
                dbe4O16 += eval(data[1])
                intensityO16dbe1["dbe4"] = dbe4O16
            if eval(data[23]) == 5:
                dbe5O16 += eval(data[1])
                intensityO16dbe1["dbe5"] = dbe5O16
            if eval(data[23]) == 6:
                dbe6O16 += eval(data[1])
                intensityO16dbe1["dbe6"] = dbe6O16
            if eval(data[23]) == 7:
                dbe7O16 += eval(data[1])
                intensityO16dbe1["dbe7"] = dbe7O16
            if eval(data[23]) == 8:
                dbe8O16 += eval(data[1])
                intensityO16dbe1["dbe8"] = dbe8O16
            if eval(data[23]) == 9:
                dbe9O16 += eval(data[1])
                intensityO16dbe1["dbe9"] = dbe9O16
            if eval(data[23]) == 10:
                dbe10O16 += eval(data[1])
                intensityO16dbe1["dbe10"] = dbe10O16
            if eval(data[23]) == 11:
                dbe11O16 += eval(data[1])
                intensityO16dbe1["dbe11"] = dbe11O16
            if eval(data[23]) == 12:
                dbe12O16 += eval(data[1])
                intensityO16dbe1["dbe12"] = dbe12O16
            if eval(data[23]) == 13:
                dbe13O16 += eval(data[1])
                intensityO16dbe1["dbe13"] = dbe13O16
            if eval(data[23]) == 14:
                dbe14O16 += eval(data[1])
                intensityO16dbe1["dbe14"] = dbe14O16
            if eval(data[23]) == 15:
                dbe15O16 += eval(data[1])
                intensityO16dbe1["dbe15"] = dbe15O16
            if eval(data[23]) == 16:
                dbe16O16 += eval(data[1])
                intensityO16dbe1["dbe16"] = dbe16O16
            if eval(data[23]) == 17:
                dbe17O16 += eval(data[1])
                intensityO16dbe1["dbe17"] = dbe17O16
            if eval(data[23]) == 18:
                dbe18O16 += eval(data[1])
                intensityO16dbe1["dbe18"] = dbe18O16
            if eval(data[23]) == 19:
                dbe19O16 += eval(data[1])
                intensityO16dbe1["dbe19"] = dbe19O16
            if eval(data[23]) == 20:
                dbe20O16 += eval(data[1])
                intensityO16dbe1["dbe20"] = dbe20O16
    print("O16类中各dbe强度之和为：")
    print(intensityO16dbe1)
    print(intensityO16dbe1["dbe1"])

    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==3):
    #         label.append("N1O3")
    #         N1O3.append(data)
    #         dbeN1O3 += eval(data[1])
    #         intensity["N1O3"] = dbeN1O3
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==4):
    #         label.append("N1O4")
    #         N1O4.append(data)
    #         dbeN1O4 += eval(data[1])
    #         intensity["N1O4"] = dbeN1O4
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==5):
    #         label.append("N1O5")
    #         N1O5.append(data)
    #         dbeN1O5 += eval(data[1])
    #         intensity["N1O5"] = dbeN1O5
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==6):
    #         label.append("N1O6")
    #         N1O6.append(data)
    #         dbeN1O6 += eval(data[1])
    #         intensity["N1O6"] = dbeN1O6
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==7):
    #         label.append("N1O7")
    #         N1O7.append(data)
    #         dbeN1O7 += eval(data[1])
    #         intensity["N1O7"] = dbeN1O7
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==8):
    #         label.append("N1O8")
    #         N1O8.append(data)
    #         dbeN1O8 += eval(data[1])
    #         intensity["N1O8"] = dbeN1O8
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==9):
    #         label.append("N1O9")
    #         N1O9.append(data)
    #         dbeN1O9 += eval(data[1])
    #         intensity["N1O9"] = dbeN1O9
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==10):
    #         label.append("N1O10")
    #         N1O10.append(data)
    #         dbeN1O10 += eval(data[1])
    #         intensity["N1O10"] = dbeN1O10
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==11):
    #         label.append("N1O11")
    #         N1O11.append(data)
    #         dbeN1O11 += eval(data[1])
    #         intensity["N1O11"] = dbeN1O11
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==12):
    #         label.append("N1O12")
    #         N1O12.append(data)
    #         dbeN1O12 += eval(data[1])
    #         intensity["N1O12"] = dbeN1O12
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==13):
    #         label.append("N1O13")
    #         N1O13.append(data)
    #         dbeN1O13 += eval(data[1])
    #         intensity["N1O13"] = dbeN1O13
    #
    # for data in datas:
    #     if data[9]==1 and eval(data[10]==14):
    #         label.append("N1O14")
    #         N1O14.append(data)
    #         dbeN1O14 += eval(data[1])
    #         intensity["N1O14"] = dbeN1O14
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==3):
    #         label.append("O3S1")
    #         O3S1.append(data)
    #         dbeO3S1 += eval(data[1])
    #         intensity["O3S1"] = dbeO3S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==4):
    #         label.append("O4S1")
    #         O4S1.append(data)
    #         dbeO4S1 += eval(data[1])
    #         intensity["O4S1"] = dbeO4S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==5):
    #         label.append("O5S1")
    #         O5S1.append(data)
    #         dbeO5S1 += eval(data[1])
    #         intensity["O5S1"] = dbeO5S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==6):
    #         label.append("O6S1")
    #         O6S1.append(data)
    #         dbeO6S1 += eval(data[1])
    #         intensity["O6S1"] = dbeO6S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==7):
    #         label.append("O7S1")
    #         O7S1.append(data)
    #         dbeO7S1 += eval(data[1])
    #         intensity["O7S1"] = dbeO7S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==8):
    #         label.append("O8S1")
    #         O8S1.append(data)
    #         dbeO8S1 += eval(data[1])
    #         intensity["O8S1"] = dbeO8S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==9):
    #         label.append("O9S1")
    #         O9S1.append(data)
    #         dbeO9S1 += eval(data[1])
    #         intensity["O9S1"] = dbeO9S1
    #     else:
    #         break
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==10):
    #         label.append("O10S1")
    #         O10S1.append(data)
    #         dbeO10S1 += eval(data[1])
    #         intensity["O10S1"] = dbeO10S1
    #
    # for data in datas:
    #     if data[11]==1 and eval(data[10]==11):
    #         label.append("O11S1")
    #         O11S1.append(data)
    #         dbeO11S1 += eval(data[1])
    #         intensity["O11S1"] = dbeO11S1
    #
    # for data in datas:
    #     if data[11] == 1 and eval(data[10]==12):
    #         label.append("O12S1")
    #         O12S1.append(data)
    #         dbeO12S1 += eval(data[1])
    #         intensity["O12S1"] = dbeO12S1

if __name__ == '__main__':
    main()