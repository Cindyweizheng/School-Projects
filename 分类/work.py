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

def dict_to_list(data):
    keys = []
    values = []
    for key, value in data.items():
        keys.append(key)
        values.append(value)
    return [keys,values]


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

    dbe1N1O3 = dbe2N1O3 = dbe3N1O3 = dbe4N1O3 = dbe5N1O3 = dbe6N1O3 = dbe7N1O3 = dbe8N1O3 = dbe9N1O3 = dbe10N1O3 = dbe11N1O3 = dbe12N1O3 = dbe13N1O3 = dbe14N1O3 = dbe15N1O3 = dbe16N1O3 = dbe17N1O3 = dbe18N1O3 = dbe19N1O3 = dbe20N1O3 = 0
    dbe1N1O4 = dbe2N1O4 = dbe3N1O4 = dbe4N1O4 = dbe5N1O4 = dbe6N1O4 = dbe7N1O4 = dbe8N1O4 = dbe9N1O4 = dbe10N1O4 = dbe11N1O4 = dbe12N1O4 = dbe13N1O4 = dbe14N1O4 = dbe15N1O4 = dbe16N1O4 = dbe17N1O4 = dbe18N1O4 = dbe19N1O4 = dbe20N1O4 = 0
    dbe1N1O5 = dbe2N1O5 = dbe3N1O5 = dbe4N1O5 = dbe5N1O5 = dbe6N1O5 = dbe7N1O5 = dbe8N1O5 = dbe9N1O5 = dbe10N1O5 = dbe11N1O5 = dbe12N1O5 = dbe13N1O5 = dbe14N1O5 = dbe15N1O5 = dbe16N1O5 = dbe17N1O5 = dbe18N1O5 = dbe19N1O5 = dbe20N1O5 = 0
    dbe1N1O6 = dbe2N1O6 = dbe3N1O6 = dbe4N1O6 = dbe5N1O6 = dbe6N1O6 = dbe7N1O6 = dbe8N1O6 = dbe9N1O6 = dbe10N1O6 = dbe11N1O6 = dbe12N1O6 = dbe13N1O6 = dbe14N1O6 = dbe15N1O6 = dbe16N1O6 = dbe17N1O6 = dbe18N1O6 = dbe19N1O6 = dbe20N1O6 = 0
    dbe1N1O7 = dbe2N1O7 = dbe3N1O7 = dbe4N1O7 = dbe5N1O7 = dbe6N1O7 = dbe7N1O7 = dbe8N1O7 = dbe9N1O7 = dbe10N1O7 = dbe11N1O7 = dbe12N1O7 = dbe13N1O7 = dbe14N1O7 = dbe15N1O7 = dbe16N1O7 = dbe17N1O7 = dbe18N1O7 = dbe19N1O7 = dbe20N1O7 = 0
    dbe1N1O8 = dbe2N1O8 = dbe3N1O8 = dbe4N1O8 = dbe5N1O8 = dbe6N1O8 = dbe7N1O8 = dbe8N1O8 = dbe9N1O8 = dbe10N1O8 = dbe11N1O8 = dbe12N1O8 = dbe13N1O8 = dbe14N1O8 = dbe15N1O8 = dbe16N1O8 = dbe17N1O8 = dbe18N1O8 = dbe19N1O8 = dbe20N1O8 = 0
    dbe1N1O9 = dbe2N1O9 = dbe3N1O9 = dbe4N1O9 = dbe5N1O9 = dbe6N1O9 = dbe7N1O9 = dbe8N1O9 = dbe9N1O9 = dbe10N1O9 = dbe11N1O9 = dbe12N1O9 = dbe13N1O9 = dbe14N1O9 = dbe15N1O9 = dbe16N1O9 = dbe17N1O9 = dbe18N1O9 = dbe19N1O9 = dbe20N1O9 = 0
    dbe1N1O10 = dbe2N1O10 = dbe3N1O10 = dbe4N1O10 = dbe5N1O10 = dbe6N1O10 = dbe7N1O10 = dbe8N1O10 = dbe9N1O10 = dbe10N1O10 = dbe11N1O10 = dbe12N1O10 = dbe13N1O10 = dbe14N1O10 = dbe15N1O10 = dbe16N1O10 = dbe17N1O10 = dbe18N1O10 = dbe19N1O10 = dbe20N1O10 = 0
    dbe1N1O11 = dbe2N1O11 = dbe3N1O11 = dbe4N1O11 = dbe5N1O11 = dbe6N1O11 = dbe7N1O11 = dbe8N1O11 = dbe9N1O11 = dbe10N1O11 = dbe11N1O11 = dbe12N1O11 = dbe13N1O11 = dbe14N1O11 = dbe15N1O11 = dbe16N1O11 = dbe17N1O11 = dbe18N1O11 = dbe19N1O11 = dbe20N1O11 = 0
    dbe1N1O12 = dbe2N1O12 = dbe3N1O12 = dbe4N1O12 = dbe5N1O12 = dbe6N1O12 = dbe7N1O12 = dbe8N1O12 = dbe9N1O12 = dbe10N1O12 = dbe11N1O12 = dbe12N1O12 = dbe13N1O12 = dbe14N1O12 = dbe15N1O12 = dbe16N1O12 = dbe17N1O12 = dbe18N1O12 = dbe19N1O12 = dbe20N1O12 = 0
    dbe1N1O13 = dbe2N1O13 = dbe3N1O13 = dbe4N1O13 = dbe5N1O13 = dbe6N1O13 = dbe7N1O13 = dbe8N1O13 = dbe9N1O13 = dbe10N1O13 = dbe11N1O13 = dbe12N1O13 = dbe13N1O13 = dbe14N1O13 = dbe15N1O13 = dbe16N1O13 = dbe17N1O13 = dbe18N1O13 = dbe19N1O13 = dbe20N1O13 = 0
    dbe1N1O14 = dbe2N1O14 = dbe3N1O14 = dbe4N1O14 = dbe5N1O14 = dbe6N1O14 = dbe7N1O14 = dbe8N1O14 = dbe9N1O14 = dbe10N1O14 = dbe11N1O14 = dbe12N1O14 = dbe13N1O14 = dbe14N1O14 = dbe15N1O14 = dbe16N1O14 = dbe17N1O14 = dbe18N1O14 = dbe19N1O14 = dbe20N1O14 = 0

    dbe1O3S1 = dbe2O3S1 = dbe3O3S1 = dbe4O3S1 = dbe5O3S1 = dbe6O3S1 = dbe7O3S1 = dbe8O3S1 = dbe9O3S1 = dbe10O3S1 = dbe11O3S1 = dbe12O3S1 = dbe13O3S1 = dbe14O3S1 = dbe15O3S1 = dbe16O3S1 = dbe17O3S1 = dbe18O3S1 = dbe19O3S1 = dbe20O3S1 = 0
    dbe1O4S1 = dbe2O4S1 = dbe3O4S1 = dbe4O4S1 = dbe5O4S1 = dbe6O4S1 = dbe7O4S1 = dbe8O4S1 = dbe9O4S1 = dbe10O4S1 = dbe11O4S1 = dbe12O4S1 = dbe13O4S1 = dbe14O4S1 = dbe15O4S1 = dbe16O4S1 = dbe17O4S1 = dbe18O4S1 = dbe19O4S1 = dbe20O4S1 = 0
    dbe1O5S1 = dbe2O5S1 = dbe3O5S1 = dbe4O5S1 = dbe5O5S1 = dbe6O5S1 = dbe7O5S1 = dbe8O5S1 = dbe9O5S1 = dbe10O5S1 = dbe11O5S1 = dbe12O5S1 = dbe13O5S1 = dbe14O5S1 = dbe15O5S1 = dbe16O5S1 = dbe17O5S1 = dbe18O5S1 = dbe19O5S1 = dbe20O5S1 = 0
    dbe1O6S1 = dbe2O6S1 = dbe3O6S1 = dbe4O6S1 = dbe5O6S1 = dbe6O6S1 = dbe7O6S1 = dbe8O6S1 = dbe9O6S1 = dbe10O6S1 = dbe11O6S1 = dbe12O6S1 = dbe13O6S1 = dbe14O6S1 = dbe15O6S1 = dbe16O6S1 = dbe17O6S1 = dbe18O6S1 = dbe19O6S1 = dbe20O6S1 = 0
    dbe1O7S1 = dbe2O7S1 = dbe3O7S1 = dbe4O7S1 = dbe5O7S1 = dbe6O7S1 = dbe7O7S1 = dbe8O7S1 = dbe9O7S1 = dbe10O7S1 = dbe11O7S1 = dbe12O7S1 = dbe13O7S1 = dbe14O7S1 = dbe15O7S1 = dbe16O7S1 = dbe17O7S1 = dbe18O7S1 = dbe19O7S1 = dbe20O7S1 = 0
    dbe1O8S1 = dbe2O8S1 = dbe3O8S1 = dbe4O8S1 = dbe5O8S1 = dbe6O8S1 = dbe7O8S1 = dbe8O8S1 = dbe9O8S1 = dbe10O8S1 = dbe11O8S1 = dbe12O8S1 = dbe13O8S1 = dbe14O8S1 = dbe15O8S1 = dbe16O8S1 = dbe17O8S1 = dbe18O8S1 = dbe19O8S1 = dbe20O8S1 = 0
    dbe1O9S1 = dbe2O9S1 = dbe3O9S1 = dbe4O9S1 = dbe5O9S1 = dbe6O9S1 = dbe7O9S1 = dbe8O9S1 = dbe9O9S1 = dbe10O9S1 = dbe11O9S1 = dbe12O9S1 = dbe13O9S1 = dbe14O9S1 = dbe15O9S1 = dbe16O9S1 = dbe17O9S1 = dbe18O9S1 = dbe19O9S1 = dbe20O9S1 = 0
    dbe1O10S1 = dbe2O10S1 = dbe3O10S1 = dbe4O10S1 = dbe5O10S1 = dbe6O10S1 = dbe7O10S1 = dbe8O10S1 = dbe9O10S1 = dbe10O10S1 = dbe11O10S1 = dbe12O10S1 = dbe13O10S1 = dbe14O10S1 = dbe15O10S1 = dbe16O10S1 = dbe17O10S1 = dbe18O10S1 = dbe19O10S1 = dbe20O10S1 = 0
    dbe1O11S1 = dbe2O11S1 = dbe3O11S1 = dbe4O11S1 = dbe5O11S1 = dbe6O11S1 = dbe7O11S1 = dbe8O11S1 = dbe9O11S1 = dbe10O11S1 = dbe11O11S1 = dbe12O11S1 = dbe13O11S1 = dbe14O11S1 = dbe15O11S1 = dbe16O11S1 = dbe17O11S1 = dbe18O11S1 = dbe19O11S1 = dbe20O11S1 = 0
    dbe1O12S1 = dbe2O12S1 = dbe3O12S1 = dbe4O12S1 = dbe5O12S1 = dbe6O12S1 = dbe7O12S1 = dbe8O12S1 = dbe9O12S1 = dbe10O12S1 = dbe11O12S1 = dbe12O12S1 = dbe13O12S1 = dbe14O12S1 = dbe15O12S1 = dbe16O12S1 = dbe17O12S1 = dbe18O12S1 = dbe19O12S1 = dbe20O12S1 = 0

    intensityO2dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO3dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO4dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO5dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO6dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO7dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO8dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO9dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO10dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO11dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO12dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO13dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO14dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO15dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO16dbe1 = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }

    intensityN1O3dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O4dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O5dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O6dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O7dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O8dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O9dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O10dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O11dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O12dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O13dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityN1O14dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }

    intensityO3S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO4S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO5S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO6S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO7S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO8S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO9S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO10S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO11S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    intensityO12S1dbe = {
        "dbe1": 0,
        "dbe2": 0,
        "dbe3": 0,
        "dbe4": 0,
        "dbe5": 0,
        "dbe6": 0,
        "dbe7": 0,
        "dbe8": 0,
        "dbe9": 0,
        "dbe10": 0,
        "dbe11": 0,
        "dbe12": 0,
        "dbe13": 0,
        "dbe14": 0,
        "dbe15": 0,
        "dbe16": 0,
        "dbe17": 0,
        "dbe18": 0,
        "dbe19": 0,
        "dbe20": 0,
    }
    dbe = []

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
        elif eval(data[9]) != 0 and eval(data[10]) !=0 and eval(data[11]) != 0:
            data.append("others")
        else:
            data.append(f"O{data[10]}")
            # data.append(f"N{data[9]}O{data[10]}S{data[11]}")
    header = ["mSigma","ObservedIntens","ObservedM_z","calc_M_z","errMDa","errPpm","sumFormula","C","H","N","O","S","H1","HCraito","OCraito","CN2","NSP","abserrPpm"
              ,"sumintens","relativeintens","avemass","dbe_o","aimod","dbe","nosc","kmdch2","nkmch2","kmdh2","nkmh2","kmdh2o","nkmh2o","kmdo","nkmo","kmdcoo","nkmcoo","class"]
    write_to_csv(datas, header, resultFile)

    result_datas = [["dbe1"], ["dbe2"], ["dbe3"], ["dbe4"], ["dbe5"], ["dbe6"], ["dbe7"], ["dbe8"], ["dbe9"], ["dbe10"],
                    ["dbe11"], ["dbe12"], ["dbe13"], ["dbe14"], ["dbe15"], ["dbe16"], ["dbe17"], ["dbe18"], ["dbe19"], ["dbe20"]]

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
    result_datas[0].append(dbe1O2)
    result_datas[1].append(dbe2O2)
    result_datas[2].append(dbe3O2)
    result_datas[3].append(dbe4O2)
    result_datas[4].append(dbe5O2)
    result_datas[5].append(dbe6O2)
    result_datas[6].append(dbe7O2)
    result_datas[7].append(dbe8O2)
    result_datas[8].append(dbe9O2)
    result_datas[9].append(dbe10O2)
    result_datas[10].append(dbe11O2)
    result_datas[11].append(dbe12O2)
    result_datas[12].append(dbe13O2)
    result_datas[13].append(dbe14O2)
    result_datas[14].append(dbe15O2)
    result_datas[15].append(dbe16O2)
    result_datas[16].append(dbe17O2)
    result_datas[17].append(dbe18O2)
    result_datas[18].append(dbe19O2)
    result_datas[19].append(dbe20O2)
    # print("O2类中各dbe强度之和为：")
    # print(intensityO2dbe1)
    intensityO2dbe = dict_to_list(intensityO2dbe1)
    # print(intensityO2dbe)
    add_to_csv(" ", resultFile)
    add_to_csv([["O2类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO2dbe,resultFile)
    # print(intensity)
    # print(dbeO2)

    result_datas[0].append(dbe1O3)
    result_datas[1].append(dbe2O3)
    result_datas[2].append(dbe3O3)
    result_datas[3].append(dbe4O3)
    result_datas[4].append(dbe5O3)
    result_datas[5].append(dbe6O3)
    result_datas[6].append(dbe7O3)
    result_datas[7].append(dbe8O3)
    result_datas[8].append(dbe9O3)
    result_datas[9].append(dbe10O3)
    result_datas[10].append(dbe11O3)
    result_datas[11].append(dbe12O3)
    result_datas[12].append(dbe13O3)
    result_datas[13].append(dbe14O3)
    result_datas[14].append(dbe15O3)
    result_datas[15].append(dbe16O3)
    result_datas[16].append(dbe17O3)
    result_datas[17].append(dbe18O3)
    result_datas[18].append(dbe19O3)
    result_datas[19].append(dbe20O3)
    # print("O3类中各dbe强度之和为：")
    # print(intensityO3dbe1)
    intensityO3dbe = dict_to_list(intensityO3dbe1)
    add_to_csv([["O3类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO3dbe,resultFile)


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
    # print("O4类中各dbe强度之和为：")
    # print(intensityO4dbe1)
    result_datas[0].append(dbe1O4)
    result_datas[1].append(dbe2O4)
    result_datas[2].append(dbe3O4)
    result_datas[3].append(dbe4O4)
    result_datas[4].append(dbe5O4)
    result_datas[5].append(dbe6O4)
    result_datas[6].append(dbe7O4)
    result_datas[7].append(dbe8O4)
    result_datas[8].append(dbe9O4)
    result_datas[9].append(dbe10O4)
    result_datas[10].append(dbe11O4)
    result_datas[11].append(dbe12O4)
    result_datas[12].append(dbe13O4)
    result_datas[13].append(dbe14O4)
    result_datas[14].append(dbe15O4)
    result_datas[15].append(dbe16O4)
    result_datas[16].append(dbe17O4)
    result_datas[17].append(dbe18O4)
    result_datas[18].append(dbe19O4)
    result_datas[19].append(dbe20O4)
    intensityO4dbe = dict_to_list(intensityO4dbe1)
    add_to_csv([["O4类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO4dbe,resultFile)

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
    # print("O5类中各dbe强度之和为：")
    # print(intensityO5dbe1)
    result_datas[0].append(dbe1O5)
    result_datas[1].append(dbe2O5)
    result_datas[2].append(dbe3O5)
    result_datas[3].append(dbe4O5)
    result_datas[4].append(dbe5O5)
    result_datas[5].append(dbe6O5)
    result_datas[6].append(dbe7O5)
    result_datas[7].append(dbe8O5)
    result_datas[8].append(dbe9O5)
    result_datas[9].append(dbe10O5)
    result_datas[10].append(dbe11O5)
    result_datas[11].append(dbe12O5)
    result_datas[12].append(dbe13O5)
    result_datas[13].append(dbe14O5)
    result_datas[14].append(dbe15O5)
    result_datas[15].append(dbe16O5)
    result_datas[16].append(dbe17O5)
    result_datas[17].append(dbe18O5)
    result_datas[18].append(dbe19O5)
    result_datas[19].append(dbe20O5)
    intensityO5dbe = dict_to_list(intensityO5dbe1)
    add_to_csv([["O5类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO5dbe,resultFile)

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
    # print("O6类中各dbe强度之和为：")
    # print(intensityO6dbe1)
    result_datas[0].append(dbe1O6)
    result_datas[1].append(dbe2O6)
    result_datas[2].append(dbe3O6)
    result_datas[3].append(dbe4O6)
    result_datas[4].append(dbe5O6)
    result_datas[5].append(dbe6O6)
    result_datas[6].append(dbe7O6)
    result_datas[7].append(dbe8O6)
    result_datas[8].append(dbe9O6)
    result_datas[9].append(dbe10O6)
    result_datas[10].append(dbe11O6)
    result_datas[11].append(dbe12O6)
    result_datas[12].append(dbe13O6)
    result_datas[13].append(dbe14O6)
    result_datas[14].append(dbe15O6)
    result_datas[15].append(dbe16O6)
    result_datas[16].append(dbe17O6)
    result_datas[17].append(dbe18O6)
    result_datas[18].append(dbe19O6)
    result_datas[19].append(dbe20O6)
    intensityO6dbe = dict_to_list(intensityO6dbe1)
    add_to_csv([["O6类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO6dbe,resultFile)

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
    # print("O7类中各dbe强度之和为：")
    # print(intensityO7dbe1)
    result_datas[0].append(dbe1O7)
    result_datas[1].append(dbe2O7)
    result_datas[2].append(dbe3O7)
    result_datas[3].append(dbe4O7)
    result_datas[4].append(dbe5O7)
    result_datas[5].append(dbe6O7)
    result_datas[6].append(dbe7O7)
    result_datas[7].append(dbe8O7)
    result_datas[8].append(dbe9O7)
    result_datas[9].append(dbe10O7)
    result_datas[10].append(dbe11O7)
    result_datas[11].append(dbe12O7)
    result_datas[12].append(dbe13O7)
    result_datas[13].append(dbe14O7)
    result_datas[14].append(dbe15O7)
    result_datas[15].append(dbe16O7)
    result_datas[16].append(dbe17O7)
    result_datas[17].append(dbe18O7)
    result_datas[18].append(dbe19O7)
    result_datas[19].append(dbe20O7)
    intensityO7dbe = dict_to_list(intensityO7dbe1)
    add_to_csv([["O7类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO7dbe,resultFile)

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
    # print("O8类中各dbe强度之和为：")
    # print(intensityO8dbe1)
    result_datas[0].append(dbe1O8)
    result_datas[1].append(dbe2O8)
    result_datas[2].append(dbe3O8)
    result_datas[3].append(dbe4O8)
    result_datas[4].append(dbe5O8)
    result_datas[5].append(dbe6O8)
    result_datas[6].append(dbe7O8)
    result_datas[7].append(dbe8O8)
    result_datas[8].append(dbe9O8)
    result_datas[9].append(dbe10O8)
    result_datas[10].append(dbe11O8)
    result_datas[11].append(dbe12O8)
    result_datas[12].append(dbe13O8)
    result_datas[13].append(dbe14O8)
    result_datas[14].append(dbe15O8)
    result_datas[15].append(dbe16O8)
    result_datas[16].append(dbe17O8)
    result_datas[17].append(dbe18O8)
    result_datas[18].append(dbe19O8)
    result_datas[19].append(dbe20O8)
    intensityO8dbe = dict_to_list(intensityO8dbe1)
    add_to_csv([["O8类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO8dbe,resultFile)

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
    # print("O9类中各dbe强度之和为：")
    # print(intensityO9dbe1)
    result_datas[0].append(dbe1O9)
    result_datas[1].append(dbe2O9)
    result_datas[2].append(dbe3O9)
    result_datas[3].append(dbe4O9)
    result_datas[4].append(dbe5O9)
    result_datas[5].append(dbe6O9)
    result_datas[6].append(dbe7O9)
    result_datas[7].append(dbe8O9)
    result_datas[8].append(dbe9O9)
    result_datas[9].append(dbe10O9)
    result_datas[10].append(dbe11O9)
    result_datas[11].append(dbe12O9)
    result_datas[12].append(dbe13O9)
    result_datas[13].append(dbe14O9)
    result_datas[14].append(dbe15O9)
    result_datas[15].append(dbe16O9)
    result_datas[16].append(dbe17O9)
    result_datas[17].append(dbe18O9)
    result_datas[18].append(dbe19O9)
    result_datas[19].append(dbe20O9)
    intensityO9dbe = dict_to_list(intensityO9dbe1)
    add_to_csv([["O9类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO9dbe,resultFile)

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
    # print("O10类中各dbe强度之和为：")
    # print(intensityO10dbe1)
    result_datas[0].append(dbe1O10)
    result_datas[1].append(dbe2O10)
    result_datas[2].append(dbe3O10)
    result_datas[3].append(dbe4O10)
    result_datas[4].append(dbe5O10)
    result_datas[5].append(dbe6O10)
    result_datas[6].append(dbe7O10)
    result_datas[7].append(dbe8O10)
    result_datas[8].append(dbe9O10)
    result_datas[9].append(dbe10O10)
    result_datas[10].append(dbe11O10)
    result_datas[11].append(dbe12O10)
    result_datas[12].append(dbe13O10)
    result_datas[13].append(dbe14O10)
    result_datas[14].append(dbe15O10)
    result_datas[15].append(dbe16O10)
    result_datas[16].append(dbe17O10)
    result_datas[17].append(dbe18O10)
    result_datas[18].append(dbe19O10)
    result_datas[19].append(dbe20O10)
    intensityO10dbe = dict_to_list(intensityO10dbe1)
    add_to_csv([["O10类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO10dbe,resultFile)

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
    # print("O11类中各dbe强度之和为：")
    # print(intensityO11dbe1)
    result_datas[0].append(dbe1O11)
    result_datas[1].append(dbe2O11)
    result_datas[2].append(dbe3O11)
    result_datas[3].append(dbe4O11)
    result_datas[4].append(dbe5O11)
    result_datas[5].append(dbe6O11)
    result_datas[6].append(dbe7O11)
    result_datas[7].append(dbe8O11)
    result_datas[8].append(dbe9O11)
    result_datas[9].append(dbe10O11)
    result_datas[10].append(dbe11O11)
    result_datas[11].append(dbe12O11)
    result_datas[12].append(dbe13O11)
    result_datas[13].append(dbe14O11)
    result_datas[14].append(dbe15O11)
    result_datas[15].append(dbe16O11)
    result_datas[16].append(dbe17O11)
    result_datas[17].append(dbe18O11)
    result_datas[18].append(dbe19O11)
    result_datas[19].append(dbe20O11)
    intensityO11dbe = dict_to_list(intensityO11dbe1)
    add_to_csv([["O11类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO11dbe,resultFile)

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
    # print("O12类中各dbe强度之和为：")
    # print(intensityO12dbe1)
    result_datas[0].append(dbe1O12)
    result_datas[1].append(dbe2O12)
    result_datas[2].append(dbe3O12)
    result_datas[3].append(dbe4O12)
    result_datas[4].append(dbe5O12)
    result_datas[5].append(dbe6O12)
    result_datas[6].append(dbe7O12)
    result_datas[7].append(dbe8O12)
    result_datas[8].append(dbe9O12)
    result_datas[9].append(dbe10O12)
    result_datas[10].append(dbe11O12)
    result_datas[11].append(dbe12O12)
    result_datas[12].append(dbe13O12)
    result_datas[13].append(dbe14O12)
    result_datas[14].append(dbe15O12)
    result_datas[15].append(dbe16O12)
    result_datas[16].append(dbe17O12)
    result_datas[17].append(dbe18O12)
    result_datas[18].append(dbe19O12)
    result_datas[19].append(dbe20O12)
    intensityO12dbe = dict_to_list(intensityO12dbe1)
    add_to_csv([["O12类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO12dbe,resultFile)


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
    # print("O13类中各dbe强度之和为：")
    # print(intensityO13dbe1)
    result_datas[0].append(dbe1O13)
    result_datas[1].append(dbe2O13)
    result_datas[2].append(dbe3O13)
    result_datas[3].append(dbe4O13)
    result_datas[4].append(dbe5O13)
    result_datas[5].append(dbe6O13)
    result_datas[6].append(dbe7O13)
    result_datas[7].append(dbe8O13)
    result_datas[8].append(dbe9O13)
    result_datas[9].append(dbe10O13)
    result_datas[10].append(dbe11O13)
    result_datas[11].append(dbe12O13)
    result_datas[12].append(dbe13O13)
    result_datas[13].append(dbe14O13)
    result_datas[14].append(dbe15O13)
    result_datas[15].append(dbe16O13)
    result_datas[16].append(dbe17O13)
    result_datas[17].append(dbe18O13)
    result_datas[18].append(dbe19O13)
    result_datas[19].append(dbe20O13)
    intensityO13dbe = dict_to_list(intensityO13dbe1)
    add_to_csv([["O13类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO13dbe,resultFile)


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
    # print("O14类中各dbe强度之和为：")
    # print(intensityO14dbe1)
    result_datas[0].append(dbe1O14)
    result_datas[1].append(dbe2O14)
    result_datas[2].append(dbe3O14)
    result_datas[3].append(dbe4O14)
    result_datas[4].append(dbe5O14)
    result_datas[5].append(dbe6O14)
    result_datas[6].append(dbe7O14)
    result_datas[7].append(dbe8O14)
    result_datas[8].append(dbe9O14)
    result_datas[9].append(dbe10O14)
    result_datas[10].append(dbe11O14)
    result_datas[11].append(dbe12O14)
    result_datas[12].append(dbe13O14)
    result_datas[13].append(dbe14O14)
    result_datas[14].append(dbe15O14)
    result_datas[15].append(dbe16O14)
    result_datas[16].append(dbe17O14)
    result_datas[17].append(dbe18O14)
    result_datas[18].append(dbe19O14)
    result_datas[19].append(dbe20O14)
    intensityO14dbe = dict_to_list(intensityO14dbe1)
    add_to_csv([["O14类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO14dbe,resultFile)

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
    # print("O15类中各dbe强度之和为：")
    # print(intensityO15dbe1)
    result_datas[0].append(dbe1O15)
    result_datas[1].append(dbe2O15)
    result_datas[2].append(dbe3O15)
    result_datas[3].append(dbe4O15)
    result_datas[4].append(dbe5O15)
    result_datas[5].append(dbe6O15)
    result_datas[6].append(dbe7O15)
    result_datas[7].append(dbe8O15)
    result_datas[8].append(dbe9O15)
    result_datas[9].append(dbe10O15)
    result_datas[10].append(dbe11O15)
    result_datas[11].append(dbe12O15)
    result_datas[12].append(dbe13O15)
    result_datas[13].append(dbe14O15)
    result_datas[14].append(dbe15O15)
    result_datas[15].append(dbe16O15)
    result_datas[16].append(dbe17O15)
    result_datas[17].append(dbe18O15)
    result_datas[18].append(dbe19O15)
    result_datas[19].append(dbe20O15)
    intensityO15dbe = dict_to_list(intensityO15dbe1)
    add_to_csv([["O15类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO15dbe,resultFile)

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
    # print("O16类中各dbe强度之和为：")
    # print(intensityO16dbe1)
    result_datas[0].append(dbe1O15)
    result_datas[1].append(dbe2O16)
    result_datas[2].append(dbe3O16)
    result_datas[3].append(dbe4O16)
    result_datas[4].append(dbe5O16)
    result_datas[5].append(dbe6O16)
    result_datas[6].append(dbe7O16)
    result_datas[7].append(dbe8O16)
    result_datas[8].append(dbe9O16)
    result_datas[9].append(dbe10O16)
    result_datas[10].append(dbe11O16)
    result_datas[11].append(dbe12O16)
    result_datas[12].append(dbe13O16)
    result_datas[13].append(dbe14O16)
    result_datas[14].append(dbe15O16)
    result_datas[15].append(dbe16O16)
    result_datas[16].append(dbe17O16)
    result_datas[17].append(dbe18O16)
    result_datas[18].append(dbe19O16)
    result_datas[19].append(dbe20O16)
    intensityO16dbe = dict_to_list(intensityO16dbe1)
    add_to_csv([["O16类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityO16dbe,resultFile)

    for data in datas:
        if eval(data[9])==1 and eval(data[10])==3:
            if eval(data[23]) == 1:
                dbe1N1O3 += eval(data[1])
                intensityN1O3dbe["dbe1"] = dbe1N1O3
            if eval(data[23]) == 2:
                dbe2N1O3 += eval(data[1])
                intensityN1O3dbe["dbe2"] = dbe2N1O3
            if eval(data[23]) == 3:
                dbe3N1O3 += eval(data[1])
                intensityN1O3dbe["dbe3"] = dbe3N1O3
            if eval(data[23]) == 4:
                dbe4N1O3 += eval(data[1])
                intensityN1O3dbe["dbe4"] = dbe4N1O3
            if eval(data[23]) == 5:
                dbe5N1O3 += eval(data[1])
                intensityN1O3dbe["dbe5"] = dbe5N1O3
            if eval(data[23]) == 6:
                dbe6N1O3 += eval(data[1])
                intensityN1O3dbe["dbe6"] = dbe6N1O3
            if eval(data[23]) == 7:
                dbe7N1O3 += eval(data[1])
                intensityN1O3dbe["dbe7"] = dbe7N1O3
            if eval(data[23]) == 8:
                dbe8N1O3 += eval(data[1])
                intensityN1O3dbe["dbe8"] = dbe8N1O3
            if eval(data[23]) == 9:
                dbe9N1O3 += eval(data[1])
                intensityN1O3dbe["dbe9"] = dbe9N1O3
            if eval(data[23]) == 10:
                dbe10N1O3 += eval(data[1])
                intensityN1O3dbe["dbe10"] = dbe10N1O3
            if eval(data[23]) == 11:
                dbe11N1O3 += eval(data[1])
                intensityN1O3dbe["dbe11"] = dbe11N1O3
            if eval(data[23]) == 12:
                dbe12N1O3 += eval(data[1])
                intensityN1O3dbe["dbe12"] = dbe12N1O3
            if eval(data[23]) == 13:
                dbe13N1O3 += eval(data[1])
                intensityN1O3dbe["dbe13"] = dbe13N1O3
            if eval(data[23]) == 14:
                dbe14N1O3 += eval(data[1])
                intensityN1O3dbe["dbe14"] = dbe14N1O3
            if eval(data[23]) == 15:
                dbe15N1O3 += eval(data[1])
                intensityN1O3dbe["dbe15"] = dbe15N1O3
            if eval(data[23]) == 16:
                dbe16N1O3 += eval(data[1])
                intensityN1O3dbe["dbe16"] = dbe16N1O3
            if eval(data[23]) == 17:
                dbe17N1O3 += eval(data[1])
                intensityN1O3dbe["dbe17"] = dbe17N1O3
            if eval(data[23]) == 18:
                dbe18N1O3 += eval(data[1])
                intensityN1O3dbe["dbe18"] = dbe18N1O3
            if eval(data[23]) == 19:
                dbe19N1O3 += eval(data[1])
                intensityN1O3dbe["dbe19"] = dbe19N1O3
            if eval(data[23]) == 20:
                dbe20N1O3 += eval(data[1])
                intensityN1O3dbe["dbe20"] = dbe20N1O3
    result_datas[0].append(dbe1N1O3)
    result_datas[1].append(dbe2N1O3)
    result_datas[2].append(dbe3N1O3)
    result_datas[3].append(dbe4N1O3)
    result_datas[4].append(dbe5N1O3)
    result_datas[5].append(dbe6N1O3)
    result_datas[6].append(dbe7N1O3)
    result_datas[7].append(dbe8N1O3)
    result_datas[8].append(dbe9N1O3)
    result_datas[9].append(dbe10N1O3)
    result_datas[10].append(dbe11N1O3)
    result_datas[11].append(dbe12N1O3)
    result_datas[12].append(dbe13N1O3)
    result_datas[13].append(dbe14N1O3)
    result_datas[14].append(dbe15N1O3)
    result_datas[15].append(dbe16N1O3)
    result_datas[16].append(dbe17N1O3)
    result_datas[17].append(dbe18N1O3)
    result_datas[18].append(dbe19N1O3)
    result_datas[19].append(dbe20N1O3)
    intensityN1O3 = dict_to_list(intensityN1O3dbe)
    add_to_csv([["N1O3类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O3,resultFile)

    for data in datas:
        if eval(data[9])==1 and eval(data[10])==4:
            if eval(data[23]) == 1:
                dbe1N1O4 += eval(data[1])
                intensityN1O4dbe["dbe1"] = dbe1N1O4
            if eval(data[23]) == 2:
                dbe2N1O4 += eval(data[1])
                intensityN1O4dbe["dbe2"] = dbe2N1O4
            if eval(data[23]) == 3:
                dbe3N1O4 += eval(data[1])
                intensityN1O4dbe["dbe3"] = dbe3N1O4
            if eval(data[23]) == 4:
                dbe4N1O4 += eval(data[1])
                intensityN1O4dbe["dbe4"] = dbe4N1O4
            if eval(data[23]) == 5:
                dbe5N1O4 += eval(data[1])
                intensityN1O4dbe["dbe5"] = dbe5N1O4
            if eval(data[23]) == 6:
                dbe6N1O4 += eval(data[1])
                intensityN1O4dbe["dbe6"] = dbe6N1O4
            if eval(data[23]) == 7:
                dbe7N1O4 += eval(data[1])
                intensityN1O4dbe["dbe7"] = dbe7N1O4
            if eval(data[23]) == 8:
                dbe8N1O4 += eval(data[1])
                intensityN1O4dbe["dbe8"] = dbe8N1O4
            if eval(data[23]) == 9:
                dbe9N1O4 += eval(data[1])
                intensityN1O4dbe["dbe9"] = dbe9N1O4
            if eval(data[23]) == 10:
                dbe10N1O4 += eval(data[1])
                intensityN1O4dbe["dbe10"] = dbe10N1O4
            if eval(data[23]) == 11:
                dbe11N1O4 += eval(data[1])
                intensityN1O4dbe["dbe11"] = dbe11N1O4
            if eval(data[23]) == 12:
                dbe12N1O4 += eval(data[1])
                intensityN1O4dbe["dbe12"] = dbe12N1O4
            if eval(data[23]) == 13:
                dbe13N1O4 += eval(data[1])
                intensityN1O4dbe["dbe13"] = dbe13N1O4
            if eval(data[23]) == 14:
                dbe14N1O4 += eval(data[1])
                intensityN1O4dbe["dbe14"] = dbe14N1O4
            if eval(data[23]) == 15:
                dbe15N1O4 += eval(data[1])
                intensityN1O4dbe["dbe15"] = dbe15N1O4
            if eval(data[23]) == 16:
                dbe16N1O4 += eval(data[1])
                intensityN1O4dbe["dbe16"] = dbe16N1O4
            if eval(data[23]) == 17:
                dbe17N1O4 += eval(data[1])
                intensityN1O4dbe["dbe17"] = dbe17N1O4
            if eval(data[23]) == 18:
                dbe18N1O4 += eval(data[1])
                intensityN1O4dbe["dbe18"] = dbe18N1O4
            if eval(data[23]) == 19:
                dbe19N1O4 += eval(data[1])
                intensityN1O4dbe["dbe19"] = dbe19N1O4
            if eval(data[23]) == 20:
                dbe20N1O4 += eval(data[1])
                intensityN1O4dbe["dbe20"] = dbe20N1O4
    result_datas[0].append(dbe1N1O4)
    result_datas[1].append(dbe2N1O4)
    result_datas[2].append(dbe3N1O4)
    result_datas[3].append(dbe4N1O4)
    result_datas[4].append(dbe5N1O4)
    result_datas[5].append(dbe6N1O4)
    result_datas[6].append(dbe7N1O4)
    result_datas[7].append(dbe8N1O4)
    result_datas[8].append(dbe9N1O4)
    result_datas[9].append(dbe10N1O4)
    result_datas[10].append(dbe11N1O4)
    result_datas[11].append(dbe12N1O4)
    result_datas[12].append(dbe13N1O4)
    result_datas[13].append(dbe14N1O4)
    result_datas[14].append(dbe15N1O4)
    result_datas[15].append(dbe16N1O4)
    result_datas[16].append(dbe17N1O4)
    result_datas[17].append(dbe18N1O4)
    result_datas[18].append(dbe19N1O4)
    result_datas[19].append(dbe20N1O4)
    intensityN1O4 = dict_to_list(intensityN1O4dbe)
    add_to_csv([["N1O4类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O4,resultFile)

    for data in datas:
        if eval(data[9])==1 and eval(data[10])==5:
            if eval(data[23]) == 1:
                dbe1N1O5 += eval(data[1])
                intensityN1O5dbe["dbe1"] = dbe1N1O5
            if eval(data[23]) == 2:
                dbe2N1O5 += eval(data[1])
                intensityN1O5dbe["dbe2"] = dbe2N1O5
            if eval(data[23]) == 3:
                dbe3N1O5 += eval(data[1])
                intensityN1O5dbe["dbe3"] = dbe3N1O5
            if eval(data[23]) == 4:
                dbe4N1O5 += eval(data[1])
                intensityN1O5dbe["dbe4"] = dbe4N1O5
            if eval(data[23]) == 5:
                dbe5N1O5 += eval(data[1])
                intensityN1O5dbe["dbe5"] = dbe5N1O5
            if eval(data[23]) == 6:
                dbe6N1O5 += eval(data[1])
                intensityN1O5dbe["dbe6"] = dbe6N1O5
            if eval(data[23]) == 7:
                dbe7N1O5 += eval(data[1])
                intensityN1O5dbe["dbe7"] = dbe7N1O5
            if eval(data[23]) == 8:
                dbe8N1O5 += eval(data[1])
                intensityN1O5dbe["dbe8"] = dbe8N1O5
            if eval(data[23]) == 9:
                dbe9N1O5 += eval(data[1])
                intensityN1O5dbe["dbe9"] = dbe9N1O5
            if eval(data[23]) == 10:
                dbe10N1O5 += eval(data[1])
                intensityN1O5dbe["dbe10"] = dbe10N1O5
            if eval(data[23]) == 11:
                dbe11N1O5 += eval(data[1])
                intensityN1O5dbe["dbe11"] = dbe11N1O5
            if eval(data[23]) == 12:
                dbe12N1O5 += eval(data[1])
                intensityN1O5dbe["dbe12"] = dbe12N1O5
            if eval(data[23]) == 13:
                dbe13N1O5 += eval(data[1])
                intensityN1O5dbe["dbe13"] = dbe13N1O5
            if eval(data[23]) == 14:
                dbe14N1O5 += eval(data[1])
                intensityN1O5dbe["dbe14"] = dbe14N1O5
            if eval(data[23]) == 15:
                dbe15N1O5 += eval(data[1])
                intensityN1O5dbe["dbe15"] = dbe15N1O5
            if eval(data[23]) == 16:
                dbe16N1O5 += eval(data[1])
                intensityN1O5dbe["dbe16"] = dbe16N1O5
            if eval(data[23]) == 17:
                dbe17N1O5 += eval(data[1])
                intensityN1O5dbe["dbe17"] = dbe17N1O5
            if eval(data[23]) == 18:
                dbe18N1O5 += eval(data[1])
                intensityN1O5dbe["dbe18"] = dbe18N1O5
            if eval(data[23]) == 19:
                dbe19N1O5 += eval(data[1])
                intensityN1O5dbe["dbe19"] = dbe19N1O5
            if eval(data[23]) == 20:
                dbe20N1O5 += eval(data[1])
                intensityN1O5dbe["dbe20"] = dbe20N1O5
    result_datas[0].append(dbe1N1O5)
    result_datas[1].append(dbe2N1O5)
    result_datas[2].append(dbe3N1O5)
    result_datas[3].append(dbe4N1O5)
    result_datas[4].append(dbe5N1O5)
    result_datas[5].append(dbe6N1O5)
    result_datas[6].append(dbe7N1O5)
    result_datas[7].append(dbe8N1O5)
    result_datas[8].append(dbe9N1O5)
    result_datas[9].append(dbe10N1O5)
    result_datas[10].append(dbe11N1O5)
    result_datas[11].append(dbe12N1O5)
    result_datas[12].append(dbe13N1O5)
    result_datas[13].append(dbe14N1O5)
    result_datas[14].append(dbe15N1O5)
    result_datas[15].append(dbe16N1O5)
    result_datas[16].append(dbe17N1O5)
    result_datas[17].append(dbe18N1O5)
    result_datas[18].append(dbe19N1O5)
    result_datas[19].append(dbe20N1O5)
    intensityN1O5 = dict_to_list(intensityN1O5dbe)
    add_to_csv([["N1O5类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O5,resultFile)

    for data in datas:
        if eval(data[9])==1 and eval(data[10])==6:
            if eval(data[23]) == 1:
                dbe1N1O6 += eval(data[1])
                intensityN1O6dbe["dbe1"] = dbe1N1O6
            if eval(data[23]) == 2:
                dbe2N1O6 += eval(data[1])
                intensityN1O6dbe["dbe2"] = dbe2N1O6
            if eval(data[23]) == 3:
                dbe3N1O6 += eval(data[1])
                intensityN1O6dbe["dbe3"] = dbe3N1O6
            if eval(data[23]) == 4:
                dbe4N1O6 += eval(data[1])
                intensityN1O6dbe["dbe4"] = dbe4N1O6
            if eval(data[23]) == 5:
                dbe5N1O6 += eval(data[1])
                intensityN1O6dbe["dbe5"] = dbe5N1O6
            if eval(data[23]) == 6:
                dbe6N1O6 += eval(data[1])
                intensityN1O6dbe["dbe6"] = dbe6N1O6
            if eval(data[23]) == 7:
                dbe7N1O6 += eval(data[1])
                intensityN1O6dbe["dbe7"] = dbe7N1O6
            if eval(data[23]) == 8:
                dbe8N1O6 += eval(data[1])
                intensityN1O6dbe["dbe8"] = dbe8N1O6
            if eval(data[23]) == 9:
                dbe9N1O6 += eval(data[1])
                intensityN1O6dbe["dbe9"] = dbe9N1O6
            if eval(data[23]) == 10:
                dbe10N1O6 += eval(data[1])
                intensityN1O6dbe["dbe10"] = dbe10N1O6
            if eval(data[23]) == 11:
                dbe11N1O6 += eval(data[1])
                intensityN1O6dbe["dbe11"] = dbe11N1O6
            if eval(data[23]) == 12:
                dbe12N1O6 += eval(data[1])
                intensityN1O6dbe["dbe12"] = dbe12N1O6
            if eval(data[23]) == 13:
                dbe13N1O6 += eval(data[1])
                intensityN1O6dbe["dbe13"] = dbe13N1O6
            if eval(data[23]) == 14:
                dbe14N1O6 += eval(data[1])
                intensityN1O6dbe["dbe14"] = dbe14N1O6
            if eval(data[23]) == 15:
                dbe15N1O6 += eval(data[1])
                intensityN1O6dbe["dbe15"] = dbe15N1O6
            if eval(data[23]) == 16:
                dbe16N1O6 += eval(data[1])
                intensityN1O6dbe["dbe16"] = dbe16N1O6
            if eval(data[23]) == 17:
                dbe17N1O6 += eval(data[1])
                intensityN1O6dbe["dbe17"] = dbe17N1O6
            if eval(data[23]) == 18:
                dbe18N1O6 += eval(data[1])
                intensityN1O6dbe["dbe18"] = dbe18N1O6
            if eval(data[23]) == 19:
                dbe19N1O6 += eval(data[1])
                intensityN1O6dbe["dbe19"] = dbe19N1O6
            if eval(data[23]) == 20:
                dbe20N1O6 += eval(data[1])
                intensityN1O6dbe["dbe20"] = dbe20N1O6
    result_datas[0].append(dbe1N1O6)
    result_datas[1].append(dbe2N1O6)
    result_datas[2].append(dbe3N1O6)
    result_datas[3].append(dbe4N1O6)
    result_datas[4].append(dbe5N1O6)
    result_datas[5].append(dbe6N1O6)
    result_datas[6].append(dbe7N1O6)
    result_datas[7].append(dbe8N1O6)
    result_datas[8].append(dbe9N1O6)
    result_datas[9].append(dbe10N1O6)
    result_datas[10].append(dbe11N1O6)
    result_datas[11].append(dbe12N1O6)
    result_datas[12].append(dbe13N1O6)
    result_datas[13].append(dbe14N1O6)
    result_datas[14].append(dbe15N1O6)
    result_datas[15].append(dbe16N1O6)
    result_datas[16].append(dbe17N1O6)
    result_datas[17].append(dbe18N1O6)
    result_datas[18].append(dbe19N1O6)
    result_datas[19].append(dbe20N1O6)
    intensityN1O6 = dict_to_list(intensityN1O6dbe)
    add_to_csv([["N1O6类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O6,resultFile)

    for data in datas:
        if eval(data[9])==1 and eval(data[10])==7:
            if eval(data[23]) == 1:
                dbe1N1O7 += eval(data[1])
                intensityN1O7dbe["dbe1"] = dbe1N1O7
            if eval(data[23]) == 2:
                dbe2N1O7 += eval(data[1])
                intensityN1O7dbe["dbe2"] = dbe2N1O7
            if eval(data[23]) == 3:
                dbe3N1O7 += eval(data[1])
                intensityN1O7dbe["dbe3"] = dbe3N1O7
            if eval(data[23]) == 4:
                dbe4N1O7 += eval(data[1])
                intensityN1O7dbe["dbe4"] = dbe4N1O7
            if eval(data[23]) == 5:
                dbe5N1O7 += eval(data[1])
                intensityN1O7dbe["dbe5"] = dbe5N1O7
            if eval(data[23]) == 6:
                dbe6N1O7 += eval(data[1])
                intensityN1O7dbe["dbe6"] = dbe6N1O7
            if eval(data[23]) == 7:
                dbe7N1O7 += eval(data[1])
                intensityN1O7dbe["dbe7"] = dbe7N1O7
            if eval(data[23]) == 8:
                dbe8N1O7 += eval(data[1])
                intensityN1O7dbe["dbe8"] = dbe8N1O7
            if eval(data[23]) == 9:
                dbe9N1O7 += eval(data[1])
                intensityN1O7dbe["dbe9"] = dbe9N1O7
            if eval(data[23]) == 10:
                dbe10N1O7 += eval(data[1])
                intensityN1O7dbe["dbe10"] = dbe10N1O7
            if eval(data[23]) == 11:
                dbe11N1O7 += eval(data[1])
                intensityN1O7dbe["dbe11"] = dbe11N1O7
            if eval(data[23]) == 12:
                dbe12N1O7 += eval(data[1])
                intensityN1O7dbe["dbe12"] = dbe12N1O7
            if eval(data[23]) == 13:
                dbe13N1O7 += eval(data[1])
                intensityN1O7dbe["dbe13"] = dbe13N1O7
            if eval(data[23]) == 14:
                dbe14N1O7 += eval(data[1])
                intensityN1O7dbe["dbe14"] = dbe14N1O7
            if eval(data[23]) == 15:
                dbe15N1O7 += eval(data[1])
                intensityN1O7dbe["dbe15"] = dbe15N1O7
            if eval(data[23]) == 16:
                dbe16N1O7 += eval(data[1])
                intensityN1O7dbe["dbe16"] = dbe16N1O7
            if eval(data[23]) == 17:
                dbe17N1O7 += eval(data[1])
                intensityN1O7dbe["dbe17"] = dbe17N1O7
            if eval(data[23]) == 18:
                dbe18N1O7 += eval(data[1])
                intensityN1O7dbe["dbe18"] = dbe18N1O7
            if eval(data[23]) == 19:
                dbe19N1O7 += eval(data[1])
                intensityN1O7dbe["dbe19"] = dbe19N1O7
            if eval(data[23]) == 20:
                dbe20N1O7 += eval(data[1])
                intensityN1O7dbe["dbe20"] = dbe20N1O7
    result_datas[0].append(dbe1N1O7)
    result_datas[1].append(dbe2N1O7)
    result_datas[2].append(dbe3N1O7)
    result_datas[3].append(dbe4N1O7)
    result_datas[4].append(dbe5N1O7)
    result_datas[5].append(dbe6N1O7)
    result_datas[6].append(dbe7N1O7)
    result_datas[7].append(dbe8N1O7)
    result_datas[8].append(dbe9N1O7)
    result_datas[9].append(dbe10N1O7)
    result_datas[10].append(dbe11N1O7)
    result_datas[11].append(dbe12N1O7)
    result_datas[12].append(dbe13N1O7)
    result_datas[13].append(dbe14N1O7)
    result_datas[14].append(dbe15N1O7)
    result_datas[15].append(dbe16N1O7)
    result_datas[16].append(dbe17N1O7)
    result_datas[17].append(dbe18N1O7)
    result_datas[18].append(dbe19N1O7)
    result_datas[19].append(dbe20N1O7)
    intensityN1O7 = dict_to_list(intensityN1O7dbe)
    add_to_csv([["N1O7类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O7,resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 8:
            if eval(data[23]) == 1:
                dbe1N1O8 += eval(data[1])
                intensityN1O8dbe["dbe1"] = dbe1N1O8
            if eval(data[23]) == 2:
                dbe2N1O8 += eval(data[1])
                intensityN1O8dbe["dbe2"] = dbe2N1O8
            if eval(data[23]) == 3:
                dbe3N1O8 += eval(data[1])
                intensityN1O8dbe["dbe3"] = dbe3N1O8
            if eval(data[23]) == 4:
                dbe4N1O8 += eval(data[1])
                intensityN1O8dbe["dbe4"] = dbe4N1O8
            if eval(data[23]) == 5:
                dbe5N1O8 += eval(data[1])
                intensityN1O8dbe["dbe5"] = dbe5N1O8
            if eval(data[23]) == 6:
                dbe6N1O8 += eval(data[1])
                intensityN1O8dbe["dbe6"] = dbe6N1O8
            if eval(data[23]) == 7:
                dbe7N1O8 += eval(data[1])
                intensityN1O8dbe["dbe7"] = dbe7N1O8
            if eval(data[23]) == 8:
                dbe8N1O8 += eval(data[1])
                intensityN1O8dbe["dbe8"] = dbe8N1O8
            if eval(data[23]) == 9:
                dbe9N1O8 += eval(data[1])
                intensityN1O8dbe["dbe9"] = dbe9N1O8
            if eval(data[23]) == 10:
                dbe10N1O8 += eval(data[1])
                intensityN1O8dbe["dbe10"] = dbe10N1O8
            if eval(data[23]) == 11:
                dbe11N1O8 += eval(data[1])
                intensityN1O8dbe["dbe11"] = dbe11N1O8
            if eval(data[23]) == 12:
                dbe12N1O8 += eval(data[1])
                intensityN1O8dbe["dbe12"] = dbe12N1O8
            if eval(data[23]) == 13:
                dbe13N1O8 += eval(data[1])
                intensityN1O8dbe["dbe13"] = dbe13N1O8
            if eval(data[23]) == 14:
                dbe14N1O8 += eval(data[1])
                intensityN1O8dbe["dbe14"] = dbe14N1O8
            if eval(data[23]) == 15:
                dbe15N1O8 += eval(data[1])
                intensityN1O8dbe["dbe15"] = dbe15N1O8
            if eval(data[23]) == 16:
                dbe16N1O8 += eval(data[1])
                intensityN1O8dbe["dbe16"] = dbe16N1O8
            if eval(data[23]) == 17:
                dbe17N1O8 += eval(data[1])
                intensityN1O8dbe["dbe17"] = dbe17N1O8
            if eval(data[23]) == 18:
                dbe18N1O8 += eval(data[1])
                intensityN1O8dbe["dbe18"] = dbe18N1O8
            if eval(data[23]) == 19:
                dbe19N1O8 += eval(data[1])
                intensityN1O8dbe["dbe19"] = dbe19N1O8
            if eval(data[23]) == 20:
                dbe20N1O8 += eval(data[1])
                intensityN1O8dbe["dbe120"] = dbe20N1O8
    result_datas[0].append(dbe1N1O8)
    result_datas[1].append(dbe2N1O8)
    result_datas[2].append(dbe3N1O8)
    result_datas[3].append(dbe4N1O8)
    result_datas[4].append(dbe5N1O8)
    result_datas[5].append(dbe6N1O8)
    result_datas[6].append(dbe7N1O8)
    result_datas[7].append(dbe8N1O8)
    result_datas[8].append(dbe9N1O8)
    result_datas[9].append(dbe10N1O8)
    result_datas[10].append(dbe11N1O8)
    result_datas[11].append(dbe12N1O8)
    result_datas[12].append(dbe13N1O8)
    result_datas[13].append(dbe14N1O8)
    result_datas[14].append(dbe15N1O8)
    result_datas[15].append(dbe16N1O8)
    result_datas[16].append(dbe17N1O8)
    result_datas[17].append(dbe18N1O8)
    result_datas[18].append(dbe19N1O8)
    result_datas[19].append(dbe20N1O8)
    intensityN1O8 = dict_to_list(intensityN1O8dbe)
    add_to_csv([["N1O8类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O8,resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 9:
            if eval(data[23]) == 1:
                dbe1N1O9 += eval(data[1])
                intensityN1O9dbe["dbe1"] = dbe1N1O9
            if eval(data[23]) == 2:
                dbe2N1O9 += eval(data[1])
                intensityN1O9dbe["dbe2"] = dbe2N1O9
            if eval(data[23]) == 3:
                dbe3N1O9 += eval(data[1])
                intensityN1O9dbe["dbe3"] = dbe3N1O9
            if eval(data[23]) == 4:
                dbe4N1O9 += eval(data[1])
                intensityN1O9dbe["dbe4"] = dbe4N1O9
            if eval(data[23]) == 5:
                dbe5N1O9 += eval(data[1])
                intensityN1O9dbe["dbe5"] = dbe5N1O9
            if eval(data[23]) == 6:
                dbe6N1O9 += eval(data[1])
                intensityN1O9dbe["dbe6"] = dbe6N1O9
            if eval(data[23]) == 7:
                dbe7N1O9 += eval(data[1])
                intensityN1O9dbe["dbe7"] = dbe7N1O9
            if eval(data[23]) == 8:
                dbe8N1O9 += eval(data[1])
                intensityN1O9dbe["dbe8"] = dbe8N1O9
            if eval(data[23]) == 9:
                dbe9N1O9 += eval(data[1])
                intensityN1O9dbe["dbe9"] = dbe9N1O9
            if eval(data[23]) == 10:
                dbe10N1O9 += eval(data[1])
                intensityN1O9dbe["dbe10"] = dbe10N1O9
            if eval(data[23]) == 11:
                dbe11N1O9 += eval(data[1])
                intensityN1O9dbe["dbe11"] = dbe11N1O9
            if eval(data[23]) == 12:
                dbe12N1O9 += eval(data[1])
                intensityN1O9dbe["dbe12"] = dbe12N1O9
            if eval(data[23]) == 13:
                dbe13N1O9 += eval(data[1])
                intensityN1O9dbe["dbe13"] = dbe13N1O9
            if eval(data[23]) == 14:
                dbe14N1O9 += eval(data[1])
                intensityN1O9dbe["dbe14"] = dbe14N1O9
            if eval(data[23]) == 15:
                dbe15N1O9 += eval(data[1])
                intensityN1O9dbe["dbe15"] = dbe15N1O9
            if eval(data[23]) == 16:
                dbe16N1O9 += eval(data[1])
                intensityN1O9dbe["dbe16"] = dbe16N1O9
            if eval(data[23]) == 17:
                dbe17N1O9 += eval(data[1])
                intensityN1O9dbe["dbe17"] = dbe17N1O9
            if eval(data[23]) == 18:
                dbe18N1O9 += eval(data[1])
                intensityN1O9dbe["dbe18"] = dbe18N1O9
            if eval(data[23]) == 19:
                dbe19N1O9 += eval(data[1])
                intensityN1O9dbe["dbe19"] = dbe19N1O9
            if eval(data[23]) == 20:
                dbe20N1O9 += eval(data[1])
                intensityN1O9dbe["dbe20"] = dbe20N1O9
    result_datas[0].append(dbe1N1O9)
    result_datas[1].append(dbe2N1O9)
    result_datas[2].append(dbe3N1O9)
    result_datas[3].append(dbe4N1O9)
    result_datas[4].append(dbe5N1O9)
    result_datas[5].append(dbe6N1O9)
    result_datas[6].append(dbe7N1O9)
    result_datas[7].append(dbe8N1O9)
    result_datas[8].append(dbe9N1O9)
    result_datas[9].append(dbe10N1O9)
    result_datas[10].append(dbe11N1O9)
    result_datas[11].append(dbe12N1O9)
    result_datas[12].append(dbe13N1O9)
    result_datas[13].append(dbe14N1O9)
    result_datas[14].append(dbe15N1O9)
    result_datas[15].append(dbe16N1O9)
    result_datas[16].append(dbe17N1O9)
    result_datas[17].append(dbe18N1O9)
    result_datas[18].append(dbe19N1O9)
    result_datas[19].append(dbe20N1O9)
    intensityN1O9 = dict_to_list(intensityN1O9dbe)
    add_to_csv([["N1O9类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O9,resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 10:
            if eval(data[23]) == 1:
                dbe1N1O10 += eval(data[1])
                intensityN1O10dbe["dbe1"] = dbe1N1O10
            if eval(data[23]) == 2:
                dbe2N1O10 += eval(data[1])
                intensityN1O10dbe["dbe2"] = dbe2N1O10
            if eval(data[23]) == 3:
                dbe3N1O10 += eval(data[1])
                intensityN1O10dbe["dbe3"] = dbe3N1O10
            if eval(data[23]) == 4:
                dbe4N1O10 += eval(data[1])
                intensityN1O10dbe["dbe4"] = dbe4N1O10
            if eval(data[23]) == 5:
                dbe5N1O10 += eval(data[1])
                intensityN1O10dbe["dbe5"] = dbe5N1O10
            if eval(data[23]) == 6:
                dbe6N1O10 += eval(data[1])
                intensityN1O10dbe["dbe6"] = dbe6N1O10
            if eval(data[23]) == 7:
                dbe7N1O10 += eval(data[1])
                intensityN1O10dbe["dbe7"] = dbe7N1O10
            if eval(data[23]) == 8:
                dbe8N1O10 += eval(data[1])
                intensityN1O10dbe["dbe8"] = dbe8N1O10
            if eval(data[23]) == 9:
                dbe9N1O10 += eval(data[1])
                intensityN1O10dbe["dbe9"] = dbe9N1O10
            if eval(data[23]) == 10:
                dbe10N1O10 += eval(data[1])
                intensityN1O10dbe["dbe10"] = dbe10N1O10
            if eval(data[23]) == 11:
                dbe11N1O10 += eval(data[1])
                intensityN1O10dbe["dbe11"] = dbe11N1O10
            if eval(data[23]) == 12:
                dbe12N1O10 += eval(data[1])
                intensityN1O10dbe["dbe12"] = dbe12N1O10
            if eval(data[23]) == 13:
                dbe13N1O10 += eval(data[1])
                intensityN1O10dbe["dbe13"] = dbe13N1O10
            if eval(data[23]) == 14:
                dbe14N1O10 += eval(data[1])
                intensityN1O10dbe["dbe14"] = dbe14N1O10
            if eval(data[23]) == 15:
                dbe15N1O10 += eval(data[1])
                intensityN1O10dbe["dbe15"] = dbe15N1O10
            if eval(data[23]) == 16:
                dbe16N1O10 += eval(data[1])
                intensityN1O10dbe["dbe16"] = dbe16N1O10
            if eval(data[23]) == 17:
                dbe17N1O10 += eval(data[1])
                intensityN1O10dbe["dbe17"] = dbe17N1O10
            if eval(data[23]) == 18:
                dbe18N1O10 += eval(data[1])
                intensityN1O10dbe["dbe18"] = dbe18N1O10
            if eval(data[23]) == 19:
                dbe19N1O10 += eval(data[1])
                intensityN1O10dbe["dbe19"] = dbe19N1O10
            if eval(data[23]) == 20:
                dbe20N1O10 += eval(data[1])
                intensityN1O10dbe["dbe20"] = dbe20N1O10
    result_datas[0].append(dbe1N1O10)
    result_datas[1].append(dbe2N1O10)
    result_datas[2].append(dbe3N1O10)
    result_datas[3].append(dbe4N1O10)
    result_datas[4].append(dbe5N1O10)
    result_datas[5].append(dbe6N1O10)
    result_datas[6].append(dbe7N1O10)
    result_datas[7].append(dbe8N1O10)
    result_datas[8].append(dbe9N1O10)
    result_datas[9].append(dbe10N1O10)
    result_datas[10].append(dbe11N1O10)
    result_datas[11].append(dbe12N1O10)
    result_datas[12].append(dbe13N1O10)
    result_datas[13].append(dbe14N1O10)
    result_datas[14].append(dbe15N1O10)
    result_datas[15].append(dbe16N1O10)
    result_datas[16].append(dbe17N1O10)
    result_datas[17].append(dbe18N1O10)
    result_datas[18].append(dbe19N1O10)
    result_datas[19].append(dbe20N1O10)
    intensityN1O10 = dict_to_list(intensityN1O10dbe)
    add_to_csv([["N1O10类中各dbe强度之和为："]],resultFile)
    add_to_csv(intensityN1O10,resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 11:
            if eval(data[23]) == 1:
                dbe1N1O11 += eval(data[1])
                intensityN1O11dbe["dbe1"] = dbe1N1O11
            if eval(data[23]) == 2:
                dbe2N1O11 += eval(data[1])
                intensityN1O11dbe["dbe2"] = dbe2N1O11
            if eval(data[23]) == 3:
                dbe3N1O11 += eval(data[1])
                intensityN1O11dbe["dbe3"] = dbe3N1O11
            if eval(data[23]) == 4:
                dbe4N1O11 += eval(data[1])
                intensityN1O11dbe["dbe4"] = dbe4N1O11
            if eval(data[23]) == 5:
                dbe5N1O11 += eval(data[1])
                intensityN1O11dbe["dbe5"] = dbe5N1O11
            if eval(data[23]) == 6:
                dbe6N1O11 += eval(data[1])
                intensityN1O11dbe["dbe6"] = dbe6N1O11
            if eval(data[23]) == 7:
                dbe7N1O11 += eval(data[1])
                intensityN1O11dbe["dbe7"] = dbe7N1O11
            if eval(data[23]) == 8:
                dbe8N1O11 += eval(data[1])
                intensityN1O11dbe["dbe8"] = dbe8N1O11
            if eval(data[23]) == 9:
                dbe9N1O11 += eval(data[1])
                intensityN1O11dbe["dbe9"] = dbe9N1O11
            if eval(data[23]) == 10:
                dbe10N1O11 += eval(data[1])
                intensityN1O11dbe["dbe10"] = dbe10N1O11
            if eval(data[23]) == 11:
                dbe11N1O11 += eval(data[1])
                intensityN1O11dbe["dbe11"] = dbe11N1O11
            if eval(data[23]) == 12:
                dbe12N1O11 += eval(data[1])
                intensityN1O11dbe["dbe12"] = dbe12N1O11
            if eval(data[23]) == 13:
                dbe13N1O11 += eval(data[1])
                intensityN1O11dbe["dbe13"] = dbe13N1O11
            if eval(data[23]) == 14:
                dbe14N1O11 += eval(data[1])
                intensityN1O11dbe["dbe14"] = dbe14N1O11
            if eval(data[23]) == 15:
                dbe15N1O11 += eval(data[1])
                intensityN1O11dbe["dbe15"] = dbe15N1O11
            if eval(data[23]) == 16:
                dbe16N1O11 += eval(data[1])
                intensityN1O11dbe["dbe16"] = dbe16N1O11
            if eval(data[23]) == 17:
                dbe17N1O11 += eval(data[1])
                intensityN1O11dbe["dbe17"] = dbe17N1O11
            if eval(data[23]) == 18:
                dbe18N1O11 += eval(data[1])
                intensityN1O11dbe["dbe18"] = dbe18N1O11
            if eval(data[23]) == 19:
                dbe19N1O11 += eval(data[1])
                intensityN1O11dbe["dbe19"] = dbe19N1O11
            if eval(data[23]) == 20:
                dbe20N1O11 += eval(data[1])
                intensityN1O11dbe["dbe20"] = dbe20N1O11
    result_datas[0].append(dbe1N1O11)
    result_datas[1].append(dbe2N1O11)
    result_datas[2].append(dbe3N1O11)
    result_datas[3].append(dbe4N1O11)
    result_datas[4].append(dbe5N1O11)
    result_datas[5].append(dbe6N1O11)
    result_datas[6].append(dbe7N1O11)
    result_datas[7].append(dbe8N1O11)
    result_datas[8].append(dbe9N1O11)
    result_datas[9].append(dbe10N1O11)
    result_datas[10].append(dbe11N1O11)
    result_datas[11].append(dbe12N1O11)
    result_datas[12].append(dbe13N1O11)
    result_datas[13].append(dbe14N1O11)
    result_datas[14].append(dbe15N1O11)
    result_datas[15].append(dbe16N1O11)
    result_datas[16].append(dbe17N1O11)
    result_datas[17].append(dbe18N1O11)
    result_datas[18].append(dbe19N1O11)
    result_datas[19].append(dbe20N1O11)
    intensityN1O11 = dict_to_list(intensityN1O11dbe)
    add_to_csv([["N1O11类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityN1O11, resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 12:
            if eval(data[23]) == 1:
                dbe1N1O12 += eval(data[1])
                intensityN1O12dbe["dbe1"] = dbe1N1O12
            if eval(data[23]) == 2:
                dbe2N1O12 += eval(data[1])
                intensityN1O12dbe["dbe2"] = dbe2N1O12
            if eval(data[23]) == 3:
                dbe3N1O12 += eval(data[1])
                intensityN1O12dbe["dbe3"] = dbe3N1O12
            if eval(data[23]) == 4:
                dbe4N1O12 += eval(data[1])
                intensityN1O12dbe["dbe4"] = dbe4N1O12
            if eval(data[23]) == 5:
                dbe5N1O12 += eval(data[1])
                intensityN1O12dbe["dbe5"] = dbe5N1O12
            if eval(data[23]) == 6:
                dbe6N1O12 += eval(data[1])
                intensityN1O12dbe["dbe6"] = dbe6N1O12
            if eval(data[23]) == 7:
                dbe7N1O12 += eval(data[1])
                intensityN1O12dbe["dbe7"] = dbe7N1O12
            if eval(data[23]) == 8:
                dbe8N1O12 += eval(data[1])
                intensityN1O12dbe["dbe8"] = dbe8N1O12
            if eval(data[23]) == 9:
                dbe9N1O12 += eval(data[1])
                intensityN1O12dbe["dbe9"] = dbe9N1O12
            if eval(data[23]) == 10:
                dbe10N1O12 += eval(data[1])
                intensityN1O12dbe["dbe10"] = dbe10N1O12
            if eval(data[23]) == 11:
                dbe11N1O12 += eval(data[1])
                intensityN1O12dbe["dbe11"] = dbe11N1O12
            if eval(data[23]) == 12:
                dbe12N1O12 += eval(data[1])
                intensityN1O12dbe["dbe12"] = dbe12N1O12
            if eval(data[23]) == 13:
                dbe13N1O12 += eval(data[1])
                intensityN1O12dbe["dbe13"] = dbe13N1O12
            if eval(data[23]) == 14:
                dbe14N1O12 += eval(data[1])
                intensityN1O12dbe["dbe14"] = dbe14N1O12
            if eval(data[23]) == 15:
                dbe15N1O12 += eval(data[1])
                intensityN1O12dbe["dbe15"] = dbe15N1O12
            if eval(data[23]) == 16:
                dbe16N1O12 += eval(data[1])
                intensityN1O12dbe["dbe16"] = dbe16N1O12
            if eval(data[23]) == 17:
                dbe17N1O12 += eval(data[1])
                intensityN1O12dbe["dbe17"] = dbe17N1O12
            if eval(data[23]) == 18:
                dbe18N1O12 += eval(data[1])
                intensityN1O12dbe["dbe18"] = dbe18N1O12
            if eval(data[23]) == 19:
                dbe19N1O12 += eval(data[1])
                intensityN1O12dbe["dbe19"] = dbe19N1O12
            if eval(data[23]) == 20:
                dbe20N1O12 += eval(data[1])
                intensityN1O12dbe["dbe20"] = dbe20N1O12
    result_datas[0].append(dbe1N1O12)
    result_datas[1].append(dbe2N1O12)
    result_datas[2].append(dbe3N1O12)
    result_datas[3].append(dbe4N1O12)
    result_datas[4].append(dbe5N1O12)
    result_datas[5].append(dbe6N1O12)
    result_datas[6].append(dbe7N1O12)
    result_datas[7].append(dbe8N1O12)
    result_datas[8].append(dbe9N1O12)
    result_datas[9].append(dbe10N1O12)
    result_datas[10].append(dbe11N1O12)
    result_datas[11].append(dbe12N1O12)
    result_datas[12].append(dbe13N1O12)
    result_datas[13].append(dbe14N1O12)
    result_datas[14].append(dbe15N1O12)
    result_datas[15].append(dbe16N1O12)
    result_datas[16].append(dbe17N1O12)
    result_datas[17].append(dbe18N1O12)
    result_datas[18].append(dbe19N1O12)
    result_datas[19].append(dbe20N1O12)
    intensityN1O12 = dict_to_list(intensityN1O12dbe)
    add_to_csv([["N1O12类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityN1O12, resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 13:
            if eval(data[23]) == 1:
                dbe1N1O13 += eval(data[1])
                intensityN1O13dbe["dbe1"] = dbe1N1O13
            if eval(data[23]) == 2:
                dbe2N1O13 += eval(data[1])
                intensityN1O13dbe["dbe2"] = dbe2N1O13
            if eval(data[23]) == 3:
                dbe3N1O13 += eval(data[1])
                intensityN1O13dbe["dbe3"] = dbe3N1O13
            if eval(data[23]) == 4:
                dbe4N1O13 += eval(data[1])
                intensityN1O13dbe["dbe4"] = dbe4N1O13
            if eval(data[23]) == 5:
                dbe5N1O13 += eval(data[1])
                intensityN1O13dbe["dbe5"] = dbe5N1O13
            if eval(data[23]) == 6:
                dbe6N1O13 += eval(data[1])
                intensityN1O13dbe["dbe6"] = dbe6N1O13
            if eval(data[23]) == 7:
                dbe7N1O13 += eval(data[1])
                intensityN1O13dbe["dbe7"] = dbe7N1O13
            if eval(data[23]) == 8:
                dbe8N1O13 += eval(data[1])
                intensityN1O13dbe["dbe8"] = dbe8N1O13
            if eval(data[23]) == 9:
                dbe9N1O13 += eval(data[1])
                intensityN1O13dbe["dbe9"] = dbe9N1O13
            if eval(data[23]) == 10:
                dbe10N1O13 += eval(data[1])
                intensityN1O13dbe["dbe10"] = dbe10N1O13
            if eval(data[23]) == 11:
                dbe11N1O13 += eval(data[1])
                intensityN1O13dbe["dbe11"] = dbe11N1O13
            if eval(data[23]) == 12:
                dbe12N1O13 += eval(data[1])
                intensityN1O13dbe["dbe12"] = dbe12N1O13
            if eval(data[23]) == 13:
                dbe13N1O13 += eval(data[1])
                intensityN1O13dbe["dbe13"] = dbe13N1O13
            if eval(data[23]) == 14:
                dbe14N1O13 += eval(data[1])
                intensityN1O13dbe["dbe14"] = dbe14N1O13
            if eval(data[23]) == 15:
                dbe15N1O13 += eval(data[1])
                intensityN1O13dbe["dbe15"] = dbe15N1O13
            if eval(data[23]) == 16:
                dbe16N1O13 += eval(data[1])
                intensityN1O13dbe["dbe16"] = dbe16N1O13
            if eval(data[23]) == 17:
                dbe17N1O13 += eval(data[1])
                intensityN1O13dbe["dbe17"] = dbe17N1O13
            if eval(data[23]) == 18:
                dbe18N1O13 += eval(data[1])
                intensityN1O13dbe["dbe18"] = dbe18N1O13
            if eval(data[23]) == 19:
                dbe19N1O13 += eval(data[1])
                intensityN1O13dbe["dbe19"] = dbe19N1O13
            if eval(data[23]) == 20:
                dbe20N1O13 += eval(data[1])
                intensityN1O13dbe["dbe20"] = dbe20N1O13
    result_datas[0].append(dbe1N1O13)
    result_datas[1].append(dbe2N1O13)
    result_datas[2].append(dbe3N1O13)
    result_datas[3].append(dbe4N1O13)
    result_datas[4].append(dbe5N1O13)
    result_datas[5].append(dbe6N1O13)
    result_datas[6].append(dbe7N1O13)
    result_datas[7].append(dbe8N1O13)
    result_datas[8].append(dbe9N1O13)
    result_datas[9].append(dbe10N1O13)
    result_datas[10].append(dbe11N1O13)
    result_datas[11].append(dbe12N1O13)
    result_datas[12].append(dbe13N1O13)
    result_datas[13].append(dbe14N1O13)
    result_datas[14].append(dbe15N1O13)
    result_datas[15].append(dbe16N1O13)
    result_datas[16].append(dbe17N1O13)
    result_datas[17].append(dbe18N1O13)
    result_datas[18].append(dbe19N1O13)
    result_datas[19].append(dbe20N1O13)
    intensityN1O13 = dict_to_list(intensityN1O13dbe)
    add_to_csv([["N1O13类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityN1O13, resultFile)

    for data in datas:
        if eval(data[9]) == 1 and eval(data[10]) == 14:
            if eval(data[23]) == 1:
                dbe1N1O14 += eval(data[1])
                intensityN1O14dbe["dbe1"] = dbe1N1O14
            if eval(data[23]) == 2:
                dbe2N1O14 += eval(data[1])
                intensityN1O14dbe["dbe2"] = dbe2N1O14
            if eval(data[23]) == 3:
                dbe3N1O14 += eval(data[1])
                intensityN1O14dbe["dbe3"] = dbe3N1O14
            if eval(data[23]) == 4:
                dbe4N1O14 += eval(data[1])
                intensityN1O14dbe["dbe4"] = dbe4N1O14
            if eval(data[23]) == 5:
                dbe5N1O14 += eval(data[1])
                intensityN1O14dbe["dbe5"] = dbe5N1O14
            if eval(data[23]) == 6:
                dbe6N1O14 += eval(data[1])
                intensityN1O14dbe["dbe6"] = dbe6N1O14
            if eval(data[23]) == 7:
                dbe7N1O14 += eval(data[1])
                intensityN1O14dbe["dbe7"] = dbe7N1O14
            if eval(data[23]) == 8:
                dbe8N1O14 += eval(data[1])
                intensityN1O14dbe["dbe8"] = dbe8N1O14
            if eval(data[23]) == 9:
                dbe9N1O14 += eval(data[1])
                intensityN1O14dbe["dbe9"] = dbe9N1O14
            if eval(data[23]) == 10:
                dbe10N1O14 += eval(data[1])
                intensityN1O14dbe["dbe10"] = dbe10N1O14
            if eval(data[23]) == 11:
                dbe11N1O14 += eval(data[1])
                intensityN1O14dbe["dbe11"] = dbe11N1O14
            if eval(data[23]) == 12:
                dbe12N1O14 += eval(data[1])
                intensityN1O14dbe["dbe12"] = dbe12N1O14
            if eval(data[23]) == 13:
                dbe13N1O14 += eval(data[1])
                intensityN1O14dbe["dbe13"] = dbe13N1O14
            if eval(data[23]) == 14:
                dbe14N1O14 += eval(data[1])
                intensityN1O14dbe["dbe14"] = dbe14N1O14
            if eval(data[23]) == 15:
                dbe15N1O14 += eval(data[1])
                intensityN1O14dbe["dbe15"] = dbe15N1O14
            if eval(data[23]) == 16:
                dbe16N1O14 += eval(data[1])
                intensityN1O14dbe["dbe16"] = dbe16N1O14
            if eval(data[23]) == 17:
                dbe17N1O14 += eval(data[1])
                intensityN1O14dbe["dbe17"] = dbe17N1O14
            if eval(data[23]) == 18:
                dbe18N1O14 += eval(data[1])
                intensityN1O14dbe["dbe18"] = dbe18N1O14
            if eval(data[23]) == 19:
                dbe19N1O14 += eval(data[1])
                intensityN1O14dbe["dbe19"] = dbe19N1O14
            if eval(data[23]) == 20:
                dbe20N1O14 += eval(data[1])
                intensityN1O14dbe["dbe20"] = dbe20N1O14
    result_datas[0].append(dbe1N1O14)
    result_datas[1].append(dbe2N1O14)
    result_datas[2].append(dbe3N1O14)
    result_datas[3].append(dbe4N1O14)
    result_datas[4].append(dbe5N1O14)
    result_datas[5].append(dbe6N1O14)
    result_datas[6].append(dbe7N1O14)
    result_datas[7].append(dbe8N1O14)
    result_datas[8].append(dbe9N1O14)
    result_datas[9].append(dbe10N1O14)
    result_datas[10].append(dbe11N1O14)
    result_datas[11].append(dbe12N1O14)
    result_datas[12].append(dbe13N1O14)
    result_datas[13].append(dbe14N1O14)
    result_datas[14].append(dbe15N1O14)
    result_datas[15].append(dbe16N1O14)
    result_datas[16].append(dbe17N1O14)
    result_datas[17].append(dbe18N1O14)
    result_datas[18].append(dbe19N1O14)
    result_datas[19].append(dbe20N1O14)
    intensityN1O14 = dict_to_list(intensityN1O14dbe)
    add_to_csv([["N1O14类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityN1O14, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 3:
            if eval(data[23]) == 1:
                dbe1O3S1 += eval(data[1])
                intensityO3S1dbe["dbe1"] = dbe1O3S1
            if eval(data[23]) == 2:
                dbe2O3S1 += eval(data[1])
                intensityO3S1dbe["dbe2"] = dbe2O3S1
            if eval(data[23]) == 3:
                dbe3O3S1 += eval(data[1])
                intensityO3S1dbe["dbe3"] = dbe3O3S1
            if eval(data[23]) == 4:
                dbe4O3S1 += eval(data[1])
                intensityO3S1dbe["dbe4"] = dbe4O3S1
            if eval(data[23]) == 5:
                dbe5O3S1 += eval(data[1])
                intensityO3S1dbe["dbe5"] = dbe5O3S1
            if eval(data[23]) == 6:
                dbe6O3S1 += eval(data[1])
                intensityO3S1dbe["dbe6"] = dbe6O3S1
            if eval(data[23]) == 7:
                dbe7O3S1 += eval(data[1])
                intensityO3S1dbe["dbe7"] = dbe7O3S1
            if eval(data[23]) == 8:
                dbe8O3S1 += eval(data[1])
                intensityO3S1dbe["dbe8"] = dbe8O3S1
            if eval(data[23]) == 9:
                dbe9O3S1 += eval(data[1])
                intensityO3S1dbe["dbe9"] = dbe9O3S1
            if eval(data[23]) == 10:
                dbe10O3S1 += eval(data[1])
                intensityO3S1dbe["dbe10"] = dbe10O3S1
            if eval(data[23]) == 11:
                dbe11O3S1 += eval(data[1])
                intensityO3S1dbe["dbe11"] = dbe11O3S1
            if eval(data[23]) == 12:
                dbe12O3S1 += eval(data[1])
                intensityO3S1dbe["dbe12"] = dbe12O3S1
            if eval(data[23]) == 13:
                dbe13O3S1 += eval(data[1])
                intensityO3S1dbe["dbe13"] = dbe13O3S1
            if eval(data[23]) == 14:
                dbe14O3S1 += eval(data[1])
                intensityO3S1dbe["dbe14"] = dbe14O3S1
            if eval(data[23]) == 15:
                dbe15O3S1 += eval(data[1])
                intensityO3S1dbe["dbe15"] = dbe15O3S1
            if eval(data[23]) == 16:
                dbe16O3S1 += eval(data[1])
                intensityO3S1dbe["dbe16"] = dbe16O3S1
            if eval(data[23]) == 17:
                dbe17O3S1 += eval(data[1])
                intensityO3S1dbe["dbe17"] = dbe17O3S1
            if eval(data[23]) == 18:
                dbe18O3S1 += eval(data[1])
                intensityO3S1dbe["dbe18"] = dbe18O3S1
            if eval(data[23]) == 19:
                dbe19O3S1 += eval(data[1])
                intensityO3S1dbe["dbe19"] = dbe19O3S1
            if eval(data[23]) == 20:
                dbe20O3S1 += eval(data[1])
                intensityO3S1dbe["dbe20"] = dbe20O3S1
    result_datas[0].append(dbe1O3S1)
    result_datas[1].append(dbe2O3S1)
    result_datas[2].append(dbe3O3S1)
    result_datas[3].append(dbe4O3S1)
    result_datas[4].append(dbe5O3S1)
    result_datas[5].append(dbe6O3S1)
    result_datas[6].append(dbe7O3S1)
    result_datas[7].append(dbe8O3S1)
    result_datas[8].append(dbe9O3S1)
    result_datas[9].append(dbe10O3S1)
    result_datas[10].append(dbe11O3S1)
    result_datas[11].append(dbe12O3S1)
    result_datas[12].append(dbe13O3S1)
    result_datas[13].append(dbe14O3S1)
    result_datas[14].append(dbe15O3S1)
    result_datas[15].append(dbe16O3S1)
    result_datas[16].append(dbe17O3S1)
    result_datas[17].append(dbe18O3S1)
    result_datas[18].append(dbe19O3S1)
    result_datas[19].append(dbe20O3S1)
    intensityO3S1 = dict_to_list(intensityO3S1dbe)
    add_to_csv([["O3S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO3S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 4:
            if eval(data[23]) == 1:
                dbe1O4S1 += eval(data[1])
                intensityO4S1dbe["dbe1"] = dbe1O4S1
            if eval(data[23]) == 2:
                dbe2O4S1 += eval(data[1])
                intensityO4S1dbe["dbe2"] = dbe2O4S1
            if eval(data[23]) == 3:
                dbe3O4S1 += eval(data[1])
                intensityO4S1dbe["dbe3"] = dbe3O4S1
            if eval(data[23]) == 4:
                dbe4O4S1 += eval(data[1])
                intensityO4S1dbe["dbe4"] = dbe4O4S1
            if eval(data[23]) == 5:
                dbe5O4S1 += eval(data[1])
                intensityO4S1dbe["dbe5"] = dbe5O4S1
            if eval(data[23]) == 6:
                dbe6O4S1 += eval(data[1])
                intensityO4S1dbe["dbe6"] = dbe6O4S1
            if eval(data[23]) == 7:
                dbe7O4S1 += eval(data[1])
                intensityO4S1dbe["dbe7"] = dbe7O4S1
            if eval(data[23]) == 8:
                dbe8O4S1 += eval(data[1])
                intensityO4S1dbe["dbe8"] = dbe8O4S1
            if eval(data[23]) == 9:
                dbe9O4S1 += eval(data[1])
                intensityO4S1dbe["dbe9"] = dbe9O4S1
            if eval(data[23]) == 10:
                dbe10O4S1 += eval(data[1])
                intensityO4S1dbe["dbe10"] = dbe10O4S1
            if eval(data[23]) == 11:
                dbe11O4S1 += eval(data[1])
                intensityO4S1dbe["dbe11"] = dbe11O4S1
            if eval(data[23]) == 12:
                dbe12O4S1 += eval(data[1])
                intensityO4S1dbe["dbe12"] = dbe12O4S1
            if eval(data[23]) == 13:
                dbe13O4S1 += eval(data[1])
                intensityO4S1dbe["dbe13"] = dbe13O4S1
            if eval(data[23]) == 14:
                dbe14O4S1 += eval(data[1])
                intensityO4S1dbe["dbe14"] = dbe14O4S1
            if eval(data[23]) == 15:
                dbe15O4S1 += eval(data[1])
                intensityO4S1dbe["dbe15"] = dbe15O4S1
            if eval(data[23]) == 16:
                dbe16O4S1 += eval(data[1])
                intensityO4S1dbe["dbe16"] = dbe16O4S1
            if eval(data[23]) == 17:
                dbe17O4S1 += eval(data[1])
                intensityO4S1dbe["dbe17"] = dbe17O4S1
            if eval(data[23]) == 18:
                dbe18O4S1 += eval(data[1])
                intensityO4S1dbe["dbe18"] = dbe18O4S1
            if eval(data[23]) == 19:
                dbe19O4S1 += eval(data[1])
                intensityO4S1dbe["dbe19"] = dbe19O4S1
            if eval(data[23]) == 20:
                dbe20O4S1 += eval(data[1])
                intensityO4S1dbe["dbe20"] = dbe20O4S1
    result_datas[0].append(dbe1O4S1)
    result_datas[1].append(dbe2O4S1)
    result_datas[2].append(dbe3O4S1)
    result_datas[3].append(dbe4O4S1)
    result_datas[4].append(dbe5O4S1)
    result_datas[5].append(dbe6O4S1)
    result_datas[6].append(dbe7O4S1)
    result_datas[7].append(dbe8O4S1)
    result_datas[8].append(dbe9O4S1)
    result_datas[9].append(dbe10O4S1)
    result_datas[10].append(dbe11O4S1)
    result_datas[11].append(dbe12O4S1)
    result_datas[12].append(dbe13O4S1)
    result_datas[13].append(dbe14O4S1)
    result_datas[14].append(dbe15O4S1)
    result_datas[15].append(dbe16O4S1)
    result_datas[16].append(dbe17O4S1)
    result_datas[17].append(dbe18O4S1)
    result_datas[18].append(dbe19O4S1)
    result_datas[19].append(dbe20O4S1)
    intensityO4S1 = dict_to_list(intensityO4S1dbe)
    add_to_csv([["O4S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO4S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 5:
            if eval(data[23]) == 1:
                dbe1O5S1 += eval(data[1])
                intensityO5S1dbe["dbe1"] = dbe1O5S1
            if eval(data[23]) == 2:
                dbe2O5S1 += eval(data[1])
                intensityO5S1dbe["dbe2"] = dbe2O5S1
            if eval(data[23]) == 3:
                dbe3O5S1 += eval(data[1])
                intensityO5S1dbe["dbe3"] = dbe3O5S1
            if eval(data[23]) == 4:
                dbe4O5S1 += eval(data[1])
                intensityO5S1dbe["dbe4"] = dbe4O5S1
            if eval(data[23]) == 5:
                dbe5O5S1 += eval(data[1])
                intensityO5S1dbe["dbe5"] = dbe5O5S1
            if eval(data[23]) == 6:
                dbe6O5S1 += eval(data[1])
                intensityO5S1dbe["dbe6"] = dbe6O5S1
            if eval(data[23]) == 7:
                dbe7O5S1 += eval(data[1])
                intensityO5S1dbe["dbe7"] = dbe7O5S1
            if eval(data[23]) == 8:
                dbe8O5S1 += eval(data[1])
                intensityO5S1dbe["dbe8"] = dbe8O5S1
            if eval(data[23]) == 9:
                dbe9O5S1 += eval(data[1])
                intensityO5S1dbe["dbe9"] = dbe9O5S1
            if eval(data[23]) == 10:
                dbe10O5S1 += eval(data[1])
                intensityO5S1dbe["dbe10"] = dbe10O5S1
            if eval(data[23]) == 11:
                dbe11O5S1 += eval(data[1])
                intensityO5S1dbe["dbe11"] = dbe11O5S1
            if eval(data[23]) == 12:
                dbe12O5S1 += eval(data[1])
                intensityO5S1dbe["dbe12"] = dbe12O5S1
            if eval(data[23]) == 13:
                dbe13O5S1 += eval(data[1])
                intensityO5S1dbe["dbe13"] = dbe13O5S1
            if eval(data[23]) == 14:
                dbe14O5S1 += eval(data[1])
                intensityO5S1dbe["dbe14"] = dbe14O5S1
            if eval(data[23]) == 15:
                dbe15O5S1 += eval(data[1])
                intensityO5S1dbe["dbe15"] = dbe15O5S1
            if eval(data[23]) == 16:
                dbe16O5S1 += eval(data[1])
                intensityO5S1dbe["dbe16"] = dbe16O5S1
            if eval(data[23]) == 17:
                dbe17O5S1 += eval(data[1])
                intensityO5S1dbe["dbe17"] = dbe17O5S1
            if eval(data[23]) == 18:
                dbe18O5S1 += eval(data[1])
                intensityO5S1dbe["dbe18"] = dbe18O5S1
            if eval(data[23]) == 19:
                dbe19O5S1 += eval(data[1])
                intensityO5S1dbe["dbe19"] = dbe19O5S1
            if eval(data[23]) == 20:
                dbe20O5S1 += eval(data[1])
                intensityO5S1dbe["dbe20"] = dbe20O5S1
    result_datas[0].append(dbe1O5S1)
    result_datas[1].append(dbe2O5S1)
    result_datas[2].append(dbe3O5S1)
    result_datas[3].append(dbe4O5S1)
    result_datas[4].append(dbe5O5S1)
    result_datas[5].append(dbe6O5S1)
    result_datas[6].append(dbe7O5S1)
    result_datas[7].append(dbe8O5S1)
    result_datas[8].append(dbe9O5S1)
    result_datas[9].append(dbe10O5S1)
    result_datas[10].append(dbe11O5S1)
    result_datas[11].append(dbe12O5S1)
    result_datas[12].append(dbe13O5S1)
    result_datas[13].append(dbe14O5S1)
    result_datas[14].append(dbe15O5S1)
    result_datas[15].append(dbe16O5S1)
    result_datas[16].append(dbe17O5S1)
    result_datas[17].append(dbe18O5S1)
    result_datas[18].append(dbe19O5S1)
    result_datas[19].append(dbe20O5S1)
    intensityO5S1 = dict_to_list(intensityO5S1dbe)
    add_to_csv([["O5S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO5S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 6:
            if eval(data[23]) == 1:
                dbe1O6S1 += eval(data[1])
                intensityO6S1dbe["dbe1"] = dbe1O6S1
            if eval(data[23]) == 2:
                dbe2O6S1 += eval(data[1])
                intensityO6S1dbe["dbe2"] = dbe2O6S1
            if eval(data[23]) == 3:
                dbe3O6S1 += eval(data[1])
                intensityO6S1dbe["dbe3"] = dbe3O6S1
            if eval(data[23]) == 4:
                dbe4O6S1 += eval(data[1])
                intensityO6S1dbe["dbe4"] = dbe4O6S1
            if eval(data[23]) == 5:
                dbe5O6S1 += eval(data[1])
                intensityO6S1dbe["dbe5"] = dbe5O6S1
            if eval(data[23]) == 6:
                dbe6O6S1 += eval(data[1])
                intensityO6S1dbe["dbe6"] = dbe6O6S1
            if eval(data[23]) == 7:
                dbe7O6S1 += eval(data[1])
                intensityO6S1dbe["dbe7"] = dbe7O6S1
            if eval(data[23]) == 8:
                dbe8O6S1 += eval(data[1])
                intensityO6S1dbe["dbe8"] = dbe8O6S1
            if eval(data[23]) == 9:
                dbe9O6S1 += eval(data[1])
                intensityO6S1dbe["dbe9"] = dbe9O6S1
            if eval(data[23]) == 10:
                dbe10O6S1 += eval(data[1])
                intensityO6S1dbe["dbe10"] = dbe10O6S1
            if eval(data[23]) == 11:
                dbe11O6S1 += eval(data[1])
                intensityO6S1dbe["dbe11"] = dbe11O6S1
            if eval(data[23]) == 12:
                dbe12O6S1 += eval(data[1])
                intensityO6S1dbe["dbe12"] = dbe12O6S1
            if eval(data[23]) == 13:
                dbe13O6S1 += eval(data[1])
                intensityO6S1dbe["dbe13"] = dbe13O6S1
            if eval(data[23]) == 14:
                dbe14O6S1 += eval(data[1])
                intensityO6S1dbe["dbe14"] = dbe14O6S1
            if eval(data[23]) == 15:
                dbe15O6S1 += eval(data[1])
                intensityO6S1dbe["dbe15"] = dbe15O6S1
            if eval(data[23]) == 16:
                dbe16O6S1 += eval(data[1])
                intensityO6S1dbe["dbe16"] = dbe16O6S1
            if eval(data[23]) == 17:
                dbe17O6S1 += eval(data[1])
                intensityO6S1dbe["dbe17"] = dbe17O6S1
            if eval(data[23]) == 18:
                dbe18O6S1 += eval(data[1])
                intensityO6S1dbe["dbe18"] = dbe18O6S1
            if eval(data[23]) == 19:
                dbe19O6S1 += eval(data[1])
                intensityO6S1dbe["dbe19"] = dbe19O6S1
            if eval(data[23]) == 20:
                dbe20O6S1 += eval(data[1])
                intensityO6S1dbe["dbe20"] = dbe20O6S1
    result_datas[0].append(dbe1O6S1)
    result_datas[1].append(dbe2O6S1)
    result_datas[2].append(dbe3O6S1)
    result_datas[3].append(dbe4O6S1)
    result_datas[4].append(dbe5O6S1)
    result_datas[5].append(dbe6O6S1)
    result_datas[6].append(dbe7O6S1)
    result_datas[7].append(dbe8O6S1)
    result_datas[8].append(dbe9O6S1)
    result_datas[9].append(dbe10O6S1)
    result_datas[10].append(dbe11O6S1)
    result_datas[11].append(dbe12O6S1)
    result_datas[12].append(dbe13O6S1)
    result_datas[13].append(dbe14O6S1)
    result_datas[14].append(dbe15O6S1)
    result_datas[15].append(dbe16O6S1)
    result_datas[16].append(dbe17O6S1)
    result_datas[17].append(dbe18O6S1)
    result_datas[18].append(dbe19O6S1)
    result_datas[19].append(dbe20O6S1)
    intensityO6S1 = dict_to_list(intensityO6S1dbe)
    add_to_csv([["O6S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO6S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 7:
            if eval(data[23]) == 1:
                dbe1O7S1 += eval(data[1])
                intensityO7S1dbe["dbe1"] = dbe1O7S1
            if eval(data[23]) == 2:
                dbe2O7S1 += eval(data[1])
                intensityO7S1dbe["dbe2"] = dbe2O7S1
            if eval(data[23]) == 3:
                dbe3O7S1 += eval(data[1])
                intensityO7S1dbe["dbe3"] = dbe3O7S1
            if eval(data[23]) == 4:
                dbe4O7S1 += eval(data[1])
                intensityO7S1dbe["dbe4"] = dbe4O7S1
            if eval(data[23]) == 5:
                dbe5O7S1 += eval(data[1])
                intensityO7S1dbe["dbe5"] = dbe5O7S1
            if eval(data[23]) == 6:
                dbe6O7S1 += eval(data[1])
                intensityO7S1dbe["dbe6"] = dbe6O7S1
            if eval(data[23]) == 7:
                dbe7O7S1 += eval(data[1])
                intensityO7S1dbe["dbe7"] = dbe7O7S1
            if eval(data[23]) == 8:
                dbe8O7S1 += eval(data[1])
                intensityO7S1dbe["dbe8"] = dbe8O7S1
            if eval(data[23]) == 9:
                dbe9O7S1 += eval(data[1])
                intensityO7S1dbe["dbe9"] = dbe9O7S1
            if eval(data[23]) == 10:
                dbe10O7S1 += eval(data[1])
                intensityO7S1dbe["dbe10"] = dbe10O7S1
            if eval(data[23]) == 11:
                dbe11O7S1 += eval(data[1])
                intensityO7S1dbe["dbe11"] = dbe11O7S1
            if eval(data[23]) == 12:
                dbe12O7S1 += eval(data[1])
                intensityO7S1dbe["dbe12"] = dbe12O7S1
            if eval(data[23]) == 13:
                dbe13O7S1 += eval(data[1])
                intensityO7S1dbe["dbe13"] = dbe13O7S1
            if eval(data[23]) == 14:
                dbe14O7S1 += eval(data[1])
                intensityO7S1dbe["dbe14"] = dbe14O7S1
            if eval(data[23]) == 15:
                dbe15O7S1 += eval(data[1])
                intensityO7S1dbe["dbe15"] = dbe15O7S1
            if eval(data[23]) == 16:
                dbe16O7S1 += eval(data[1])
                intensityO7S1dbe["dbe16"] = dbe16O7S1
            if eval(data[23]) == 17:
                dbe17O7S1 += eval(data[1])
                intensityO7S1dbe["dbe17"] = dbe17O7S1
            if eval(data[23]) == 18:
                dbe18O7S1 += eval(data[1])
                intensityO7S1dbe["dbe18"] = dbe18O7S1
            if eval(data[23]) == 19:
                dbe19O7S1 += eval(data[1])
                intensityO7S1dbe["dbe19"] = dbe19O7S1
            if eval(data[23]) == 20:
                dbe20O7S1 += eval(data[1])
                intensityO7S1dbe["dbe20"] = dbe20O7S1
    result_datas[0].append(dbe1O7S1)
    result_datas[1].append(dbe2O7S1)
    result_datas[2].append(dbe3O7S1)
    result_datas[3].append(dbe4O7S1)
    result_datas[4].append(dbe5O7S1)
    result_datas[5].append(dbe6O7S1)
    result_datas[6].append(dbe7O7S1)
    result_datas[7].append(dbe8O7S1)
    result_datas[8].append(dbe9O7S1)
    result_datas[9].append(dbe10O7S1)
    result_datas[10].append(dbe11O7S1)
    result_datas[11].append(dbe12O7S1)
    result_datas[12].append(dbe13O7S1)
    result_datas[13].append(dbe14O7S1)
    result_datas[14].append(dbe15O7S1)
    result_datas[15].append(dbe16O7S1)
    result_datas[16].append(dbe17O7S1)
    result_datas[17].append(dbe18O7S1)
    result_datas[18].append(dbe19O7S1)
    result_datas[19].append(dbe20O7S1)
    intensityO7S1 = dict_to_list(intensityO7S1dbe)
    add_to_csv([["O7S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO7S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 8:
            if eval(data[23]) == 1:
                dbe1O8S1 += eval(data[1])
                intensityO8S1dbe["dbe1"] = dbe1O8S1
            if eval(data[23]) == 2:
                dbe2O8S1 += eval(data[1])
                intensityO8S1dbe["dbe2"] = dbe2O8S1
            if eval(data[23]) == 3:
                dbe3O8S1 += eval(data[1])
                intensityO8S1dbe["dbe3"] = dbe3O8S1
            if eval(data[23]) == 4:
                dbe4O8S1 += eval(data[1])
                intensityO8S1dbe["dbe4"] = dbe4O8S1
            if eval(data[23]) == 5:
                dbe5O8S1 += eval(data[1])
                intensityO8S1dbe["dbe5"] = dbe5O8S1
            if eval(data[23]) == 6:
                dbe6O8S1 += eval(data[1])
                intensityO8S1dbe["dbe6"] = dbe6O8S1
            if eval(data[23]) == 7:
                dbe7O8S1 += eval(data[1])
                intensityO8S1dbe["dbe7"] = dbe7O8S1
            if eval(data[23]) == 8:
                dbe8O8S1 += eval(data[1])
                intensityO8S1dbe["dbe8"] = dbe8O8S1
            if eval(data[23]) == 9:
                dbe9O8S1 += eval(data[1])
                intensityO8S1dbe["dbe9"] = dbe9O8S1
            if eval(data[23]) == 10:
                dbe10O8S1 += eval(data[1])
                intensityO8S1dbe["dbe10"] = dbe10O8S1
            if eval(data[23]) == 11:
                dbe11O8S1 += eval(data[1])
                intensityO8S1dbe["dbe11"] = dbe11O8S1
            if eval(data[23]) == 12:
                dbe12O8S1 += eval(data[1])
                intensityO8S1dbe["dbe12"] = dbe12O8S1
            if eval(data[23]) == 13:
                dbe13O8S1 += eval(data[1])
                intensityO8S1dbe["dbe13"] = dbe13O8S1
            if eval(data[23]) == 14:
                dbe14O8S1 += eval(data[1])
                intensityO8S1dbe["dbe14"] = dbe14O8S1
            if eval(data[23]) == 15:
                dbe15O8S1 += eval(data[1])
                intensityO8S1dbe["dbe15"] = dbe15O8S1
            if eval(data[23]) == 16:
                dbe16O8S1 += eval(data[1])
                intensityO8S1dbe["dbe16"] = dbe16O8S1
            if eval(data[23]) == 17:
                dbe17O8S1 += eval(data[1])
                intensityO8S1dbe["dbe17"] = dbe17O8S1
            if eval(data[23]) == 18:
                dbe18O8S1 += eval(data[1])
                intensityO8S1dbe["dbe18"] = dbe18O8S1
            if eval(data[23]) == 19:
                dbe19O8S1 += eval(data[1])
                intensityO8S1dbe["dbe19"] = dbe19O8S1
            if eval(data[23]) == 20:
                dbe20O8S1 += eval(data[1])
                intensityO8S1dbe["dbe20"] = dbe20O8S1
    result_datas[0].append(dbe1O8S1)
    result_datas[1].append(dbe2O8S1)
    result_datas[2].append(dbe3O8S1)
    result_datas[3].append(dbe4O8S1)
    result_datas[4].append(dbe5O8S1)
    result_datas[5].append(dbe6O8S1)
    result_datas[6].append(dbe7O8S1)
    result_datas[7].append(dbe8O8S1)
    result_datas[8].append(dbe9O8S1)
    result_datas[9].append(dbe10O8S1)
    result_datas[10].append(dbe11O8S1)
    result_datas[11].append(dbe12O8S1)
    result_datas[12].append(dbe13O8S1)
    result_datas[13].append(dbe14O8S1)
    result_datas[14].append(dbe15O8S1)
    result_datas[15].append(dbe16O8S1)
    result_datas[16].append(dbe17O8S1)
    result_datas[17].append(dbe18O8S1)
    result_datas[18].append(dbe19O8S1)
    result_datas[19].append(dbe20O8S1)
    intensityO8S1 = dict_to_list(intensityO8S1dbe)
    add_to_csv([["O8S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO8S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 9:
            if eval(data[23]) == 1:
                dbe1O9S1 += eval(data[1])
                intensityO9S1dbe["dbe1"] = dbe1O9S1
            if eval(data[23]) == 2:
                dbe2O9S1 += eval(data[1])
                intensityO9S1dbe["dbe2"] = dbe2O9S1
            if eval(data[23]) == 3:
                dbe3O9S1 += eval(data[1])
                intensityO9S1dbe["dbe3"] = dbe3O9S1
            if eval(data[23]) == 4:
                dbe4O9S1 += eval(data[1])
                intensityO9S1dbe["dbe4"] = dbe4O9S1
            if eval(data[23]) == 5:
                dbe5O9S1 += eval(data[1])
                intensityO9S1dbe["dbe5"] = dbe5O9S1
            if eval(data[23]) == 6:
                dbe6O9S1 += eval(data[1])
                intensityO9S1dbe["dbe6"] = dbe6O9S1
            if eval(data[23]) == 7:
                dbe7O9S1 += eval(data[1])
                intensityO9S1dbe["dbe7"] = dbe7O9S1
            if eval(data[23]) == 8:
                dbe8O9S1 += eval(data[1])
                intensityO9S1dbe["dbe8"] = dbe8O9S1
            if eval(data[23]) == 9:
                dbe9O9S1 += eval(data[1])
                intensityO9S1dbe["dbe9"] = dbe9O9S1
            if eval(data[23]) == 10:
                dbe10O9S1 += eval(data[1])
                intensityO9S1dbe["dbe10"] = dbe10O9S1
            if eval(data[23]) == 11:
                dbe11O9S1 += eval(data[1])
                intensityO9S1dbe["dbe11"] = dbe11O9S1
            if eval(data[23]) == 12:
                dbe12O9S1 += eval(data[1])
                intensityO9S1dbe["dbe12"] = dbe12O9S1
            if eval(data[23]) == 13:
                dbe13O9S1 += eval(data[1])
                intensityO9S1dbe["dbe13"] = dbe13O9S1
            if eval(data[23]) == 14:
                dbe14O9S1 += eval(data[1])
                intensityO9S1dbe["dbe14"] = dbe14O9S1
            if eval(data[23]) == 15:
                dbe15O9S1 += eval(data[1])
                intensityO9S1dbe["dbe15"] = dbe15O9S1
            if eval(data[23]) == 16:
                dbe16O9S1 += eval(data[1])
                intensityO9S1dbe["dbe16"] = dbe16O9S1
            if eval(data[23]) == 17:
                dbe17O9S1 += eval(data[1])
                intensityO9S1dbe["dbe17"] = dbe17O9S1
            if eval(data[23]) == 18:
                dbe18O9S1 += eval(data[1])
                intensityO9S1dbe["dbe18"] = dbe18O9S1
            if eval(data[23]) == 19:
                dbe19O9S1 += eval(data[1])
                intensityO9S1dbe["dbe19"] = dbe19O9S1
            if eval(data[23]) == 20:
                dbe20O9S1 += eval(data[1])
                intensityO9S1dbe["dbe20"] = dbe20O9S1
    result_datas[0].append(dbe1O9S1)
    result_datas[1].append(dbe2O9S1)
    result_datas[2].append(dbe3O9S1)
    result_datas[3].append(dbe4O9S1)
    result_datas[4].append(dbe5O9S1)
    result_datas[5].append(dbe6O9S1)
    result_datas[6].append(dbe7O9S1)
    result_datas[7].append(dbe8O9S1)
    result_datas[8].append(dbe9O9S1)
    result_datas[9].append(dbe10O9S1)
    result_datas[10].append(dbe11O9S1)
    result_datas[11].append(dbe12O9S1)
    result_datas[12].append(dbe13O9S1)
    result_datas[13].append(dbe14O9S1)
    result_datas[14].append(dbe15O9S1)
    result_datas[15].append(dbe16O9S1)
    result_datas[16].append(dbe17O9S1)
    result_datas[17].append(dbe18O9S1)
    result_datas[18].append(dbe19O9S1)
    result_datas[19].append(dbe20O9S1)
    intensityO9S1 = dict_to_list(intensityO9S1dbe)
    add_to_csv([["O9S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO9S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 10:
            if eval(data[23]) == 1:
                dbe1O10S1 += eval(data[1])
                intensityO10S1dbe["dbe1"] = dbe1O10S1
            if eval(data[23]) == 2:
                dbe2O10S1 += eval(data[1])
                intensityO10S1dbe["dbe2"] = dbe2O10S1
            if eval(data[23]) == 3:
                dbe3O10S1 += eval(data[1])
                intensityO10S1dbe["dbe3"] = dbe3O10S1
            if eval(data[23]) == 4:
                dbe4O10S1 += eval(data[1])
                intensityO10S1dbe["dbe4"] = dbe4O10S1
            if eval(data[23]) == 5:
                dbe5O10S1 += eval(data[1])
                intensityO10S1dbe["dbe5"] = dbe5O10S1
            if eval(data[23]) == 6:
                dbe6O10S1 += eval(data[1])
                intensityO10S1dbe["dbe6"] = dbe6O10S1
            if eval(data[23]) == 7:
                dbe7O10S1 += eval(data[1])
                intensityO10S1dbe["dbe7"] = dbe7O10S1
            if eval(data[23]) == 8:
                dbe8O10S1 += eval(data[1])
                intensityO10S1dbe["dbe8"] = dbe8O10S1
            if eval(data[23]) == 9:
                dbe9O10S1 += eval(data[1])
                intensityO10S1dbe["dbe9"] = dbe9O10S1
            if eval(data[23]) == 10:
                dbe10O10S1 += eval(data[1])
                intensityO10S1dbe["dbe10"] = dbe10O10S1
            if eval(data[23]) == 11:
                dbe11O10S1 += eval(data[1])
                intensityO10S1dbe["dbe11"] = dbe11O10S1
            if eval(data[23]) == 12:
                dbe12O10S1 += eval(data[1])
                intensityO10S1dbe["dbe12"] = dbe12O10S1
            if eval(data[23]) == 13:
                dbe13O10S1 += eval(data[1])
                intensityO10S1dbe["dbe13"] = dbe13O10S1
            if eval(data[23]) == 14:
                dbe14O10S1 += eval(data[1])
                intensityO10S1dbe["dbe14"] = dbe14O10S1
            if eval(data[23]) == 15:
                dbe15O10S1 += eval(data[1])
                intensityO10S1dbe["dbe15"] = dbe15O10S1
            if eval(data[23]) == 16:
                dbe16O10S1 += eval(data[1])
                intensityO10S1dbe["dbe16"] = dbe16O10S1
            if eval(data[23]) == 17:
                dbe17O10S1 += eval(data[1])
                intensityO10S1dbe["dbe17"] = dbe17O10S1
            if eval(data[23]) == 18:
                dbe18O10S1 += eval(data[1])
                intensityO10S1dbe["dbe18"] = dbe18O10S1
            if eval(data[23]) == 19:
                dbe19O10S1 += eval(data[1])
                intensityO10S1dbe["dbe19"] = dbe19O10S1
            if eval(data[23]) == 20:
                dbe20O10S1 += eval(data[1])
                intensityO10S1dbe["dbe20"] = dbe20O10S1
    result_datas[0].append(dbe1O10S1)
    result_datas[1].append(dbe2O10S1)
    result_datas[2].append(dbe3O10S1)
    result_datas[3].append(dbe4O10S1)
    result_datas[4].append(dbe5O10S1)
    result_datas[5].append(dbe6O10S1)
    result_datas[6].append(dbe7O10S1)
    result_datas[7].append(dbe8O10S1)
    result_datas[8].append(dbe9O10S1)
    result_datas[9].append(dbe10O10S1)
    result_datas[10].append(dbe11O10S1)
    result_datas[11].append(dbe12O10S1)
    result_datas[12].append(dbe13O10S1)
    result_datas[13].append(dbe14O10S1)
    result_datas[14].append(dbe15O10S1)
    result_datas[15].append(dbe16O10S1)
    result_datas[16].append(dbe17O10S1)
    result_datas[17].append(dbe18O10S1)
    result_datas[18].append(dbe19O10S1)
    result_datas[19].append(dbe20O10S1)
    intensityO10S1 = dict_to_list(intensityO10S1dbe)
    add_to_csv([["O10S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO10S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 11:
            if eval(data[23]) == 1:
                dbe1O11S1 += eval(data[1])
                intensityO11S1dbe["dbe1"] = dbe1O11S1
            if eval(data[23]) == 2:
                dbe2O11S1 += eval(data[1])
                intensityO11S1dbe["dbe2"] = dbe2O11S1
            if eval(data[23]) == 3:
                dbe3O11S1 += eval(data[1])
                intensityO11S1dbe["dbe3"] = dbe3O11S1
            if eval(data[23]) == 4:
                dbe4O11S1 += eval(data[1])
                intensityO11S1dbe["dbe4"] = dbe4O11S1
            if eval(data[23]) == 5:
                dbe5O11S1 += eval(data[1])
                intensityO11S1dbe["dbe5"] = dbe5O11S1
            if eval(data[23]) == 6:
                dbe6O11S1 += eval(data[1])
                intensityO11S1dbe["dbe6"] = dbe6O11S1
            if eval(data[23]) == 7:
                dbe7O11S1 += eval(data[1])
                intensityO11S1dbe["dbe7"] = dbe7O11S1
            if eval(data[23]) == 8:
                dbe8O11S1 += eval(data[1])
                intensityO11S1dbe["dbe8"] = dbe8O11S1
            if eval(data[23]) == 9:
                dbe9O11S1 += eval(data[1])
                intensityO11S1dbe["dbe9"] = dbe9O11S1
            if eval(data[23]) == 10:
                dbe10O11S1 += eval(data[1])
                intensityO11S1dbe["dbe10"] = dbe10O11S1
            if eval(data[23]) == 11:
                dbe11O11S1 += eval(data[1])
                intensityO11S1dbe["dbe11"] = dbe11O11S1
            if eval(data[23]) == 12:
                dbe12O11S1 += eval(data[1])
                intensityO11S1dbe["dbe12"] = dbe12O11S1
            if eval(data[23]) == 13:
                dbe13O11S1 += eval(data[1])
                intensityO11S1dbe["dbe13"] = dbe13O11S1
            if eval(data[23]) == 14:
                dbe14O11S1 += eval(data[1])
                intensityO11S1dbe["dbe14"] = dbe14O11S1
            if eval(data[23]) == 15:
                dbe15O11S1 += eval(data[1])
                intensityO11S1dbe["dbe15"] = dbe15O11S1
            if eval(data[23]) == 16:
                dbe16O11S1 += eval(data[1])
                intensityO11S1dbe["dbe16"] = dbe16O11S1
            if eval(data[23]) == 17:
                dbe17O11S1 += eval(data[1])
                intensityO11S1dbe["dbe17"] = dbe17O11S1
            if eval(data[23]) == 18:
                dbe18O11S1 += eval(data[1])
                intensityO11S1dbe["dbe18"] = dbe18O11S1
            if eval(data[23]) == 19:
                dbe19O11S1 += eval(data[1])
                intensityO11S1dbe["dbe19"] = dbe19O11S1
            if eval(data[23]) == 20:
                dbe20O11S1 += eval(data[1])
                intensityO11S1dbe["dbe20"] = dbe20O11S1
    result_datas[0].append(dbe1O11S1)
    result_datas[1].append(dbe2O11S1)
    result_datas[2].append(dbe3O11S1)
    result_datas[3].append(dbe4O11S1)
    result_datas[4].append(dbe5O11S1)
    result_datas[5].append(dbe6O11S1)
    result_datas[6].append(dbe7O11S1)
    result_datas[7].append(dbe8O11S1)
    result_datas[8].append(dbe9O11S1)
    result_datas[9].append(dbe10O11S1)
    result_datas[10].append(dbe11O11S1)
    result_datas[11].append(dbe12O11S1)
    result_datas[12].append(dbe13O11S1)
    result_datas[13].append(dbe14O11S1)
    result_datas[14].append(dbe15O11S1)
    result_datas[15].append(dbe16O11S1)
    result_datas[16].append(dbe17O11S1)
    result_datas[17].append(dbe18O11S1)
    result_datas[18].append(dbe19O11S1)
    result_datas[19].append(dbe20O11S1)
    intensityO11S1 = dict_to_list(intensityO11S1dbe)
    add_to_csv([["O11S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO11S1, resultFile)

    for data in datas:
        if eval(data[11]) == 1 and eval(data[10]) == 12:
            if eval(data[23]) == 1:
                dbe1O12S1 += eval(data[1])
                intensityO12S1dbe["dbe1"] = dbe1O12S1
            if eval(data[23]) == 2:
                dbe2O12S1 += eval(data[1])
                intensityO12S1dbe["dbe2"] = dbe2O12S1
            if eval(data[23]) == 3:
                dbe3O12S1 += eval(data[1])
                intensityO12S1dbe["dbe3"] = dbe3O12S1
            if eval(data[23]) == 4:
                dbe4O12S1 += eval(data[1])
                intensityO12S1dbe["dbe4"] = dbe4O12S1
            if eval(data[23]) == 5:
                dbe5O12S1 += eval(data[1])
                intensityO12S1dbe["dbe5"] = dbe5O12S1
            if eval(data[23]) == 6:
                dbe6O12S1 += eval(data[1])
                intensityO12S1dbe["dbe6"] = dbe6O12S1
            if eval(data[23]) == 7:
                dbe7O12S1 += eval(data[1])
                intensityO12S1dbe["dbe7"] = dbe7O12S1
            if eval(data[23]) == 8:
                dbe8O12S1 += eval(data[1])
                intensityO12S1dbe["dbe8"] = dbe8O12S1
            if eval(data[23]) == 9:
                dbe9O12S1 += eval(data[1])
                intensityO12S1dbe["dbe9"] = dbe9O12S1
            if eval(data[23]) == 10:
                dbe10O12S1 += eval(data[1])
                intensityO12S1dbe["dbe10"] = dbe10O12S1
            if eval(data[23]) == 11:
                dbe11O12S1 += eval(data[1])
                intensityO12S1dbe["dbe11"] = dbe11O12S1
            if eval(data[23]) == 12:
                dbe12O12S1 += eval(data[1])
                intensityO12S1dbe["dbe12"] = dbe12O12S1
            if eval(data[23]) == 13:
                dbe13O12S1 += eval(data[1])
                intensityO12S1dbe["dbe13"] = dbe13O12S1
            if eval(data[23]) == 14:
                dbe14O12S1 += eval(data[1])
                intensityO12S1dbe["dbe14"] = dbe14O12S1
            if eval(data[23]) == 15:
                dbe15O12S1 += eval(data[1])
                intensityO12S1dbe["dbe15"] = dbe15O12S1
            if eval(data[23]) == 16:
                dbe16O12S1 += eval(data[1])
                intensityO12S1dbe["dbe16"] = dbe16O12S1
            if eval(data[23]) == 17:
                dbe17O12S1 += eval(data[1])
                intensityO12S1dbe["dbe17"] = dbe17O12S1
            if eval(data[23]) == 18:
                dbe18O12S1 += eval(data[1])
                intensityO12S1dbe["dbe18"] = dbe18O12S1
            if eval(data[23]) == 19:
                dbe19O12S1 += eval(data[1])
                intensityO12S1dbe["dbe19"] = dbe19O12S1
            if eval(data[23]) == 20:
                dbe20O12S1 += eval(data[1])
                intensityO12S1dbe["dbe20"] = dbe20O12S1
    result_datas[0].append(dbe1O12S1)
    result_datas[1].append(dbe2O12S1)
    result_datas[2].append(dbe3O12S1)
    result_datas[3].append(dbe4O12S1)
    result_datas[4].append(dbe5O12S1)
    result_datas[5].append(dbe6O12S1)
    result_datas[6].append(dbe7O12S1)
    result_datas[7].append(dbe8O12S1)
    result_datas[8].append(dbe9O12S1)
    result_datas[9].append(dbe10O12S1)
    result_datas[10].append(dbe11O12S1)
    result_datas[11].append(dbe12O12S1)
    result_datas[12].append(dbe13O12S1)
    result_datas[13].append(dbe14O12S1)
    result_datas[14].append(dbe15O12S1)
    result_datas[15].append(dbe16O12S1)
    result_datas[16].append(dbe17O12S1)
    result_datas[17].append(dbe18O12S1)
    result_datas[18].append(dbe19O12S1)
    result_datas[19].append(dbe20O12S1)
    header_dbe = [" ","O2","O3","O4","O5","O6","O7","O8","O9","O10","O11","O12","O13","O14","O15","O16",
                  "N1O3","N1O4","N1O5","N1O6","N1O7","N1O8","N1O9","N1O10","N1O11","N1O12","N1O13","N1O14",
                  "O3S1","O4S1","O5S1","O6S1","O7S1","O8S1","O9S1","O10S1","O11S1","O12S1"]
    write_to_csv(result_datas, header_dbe, "result/dbeInensity.csv")
    intensityO12S1 = dict_to_list(intensityO12S1dbe)
    add_to_csv([["O12S1类中各dbe强度之和为："]], resultFile)
    add_to_csv(intensityO12S1, resultFile)
    print("over!")


if __name__ == '__main__':
    main()