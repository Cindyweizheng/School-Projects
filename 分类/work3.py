import csv
import os


def read_from_csv(filename):
    csvfile = open(filename, "r")
    reader = csv.reader(csvfile)
    result = []
    for item in reader:
        # if reader.line_num == 1:
        #     continue
        result.append(item)
    csvfile.close()
    return result


def write_to_csv(data, file):
    with open(file, "w", newline="")as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        count = 1
        for da in data:
            writer.writerow(da)
            percent = int(count/len(data)*50)
            print(f'\r[{"#"*percent}{"."*(50-percent)}]\t{count}/{len(data)}', end=".")
            count += 1
        print()
        f.close()


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def Count_data(datas):
    result = []
    for data in datas:
        sig = 0
        for res in result:
            if res[0] == data[35]:
                res.append(data)
                sig = 1
                break
        if sig == 1:
            continue
        result.append([data[35], data])
    return result


def result_get(datas):
    name_data = datas[0]
    datas.pop(0)
    result = [0]*20
    # result = [["dbe1"], ["dbe2"], ["dbe3"], ["dbe4"], ["dbe5"], ["dbe6"], ["dbe7"], ["dbe8"], ["dbe9"], ["dbe10"],
    #           ["dbe11"], ["dbe12"], ["dbe13"], ["dbe14"], ["dbe15"], ["dbe16"], ["dbe17"], ["dbe18"], ["dbe19"], ["dbe20"]]
    for data in datas:
        if eval(data[23]) == 1:
            result[0] += eval(data[1])
        elif eval(data[23]) == 2:
            result[1] += eval(data[1])
        elif eval(data[23]) == 3:
            result[2] += eval(data[1])
        elif eval(data[23]) == 4:
            result[3] += eval(data[1])
        elif eval(data[23]) == 5:
            result[4] += eval(data[1])
        elif eval(data[23]) == 6:
            result[5] += eval(data[1])
        elif eval(data[23]) == 7:
            result[6] += eval(data[1])
        elif eval(data[23]) == 8:
            result[7] += eval(data[1])
        elif eval(data[23]) == 9:
            result[8] += eval(data[1])
        elif eval(data[23]) == 10:
            result[9] += eval(data[1])
        elif eval(data[23]) == 11:
            result[10] += eval(data[1])
        elif eval(data[23]) == 12:
            result[11] += eval(data[1])
        elif eval(data[23]) == 13:
            result[12] += eval(data[1])
        elif eval(data[23]) == 14:
            result[13] += eval(data[1])
        elif eval(data[23]) == 15:
            result[14] += eval(data[1])
        elif eval(data[23]) == 16:
            result[15] += eval(data[1])
        elif eval(data[23]) == 17:
            result[16] += eval(data[1])
        elif eval(data[23]) == 18:
            result[17] += eval(data[1])
        elif eval(data[23]) == 19:
            result[18] += eval(data[1])
        elif eval(data[23]) == 20:
            result[19] += eval(data[1])
    result.insert(0, name_data)
    return result


def main(data_file, i):
    print("work start")
    datas = read_from_csv(data_file)
    header = datas[0]
    datas.pop(0)
    for data in datas:
        if eval(data[9]) != 0 and eval(data[11]) == 0:
            data.append(f"N{data[9]}O{data[10]}")
        elif eval(data[11]) != 0 and eval(data[9]) == 0:
            data.append(f"S{data[11]}O{data[10]}")
        elif data[9] == 0 and data[11] == 0 and data[10] != 0:
            data.append(f"O{data[10]}")
        else:
            data.append("others")
    # print(len(datas[0]))
    count_datas = Count_data(datas)
    result_all = []
    for cdata in count_datas:
        result_all.append(result_get(cdata))
    result_all.insert(0, ["", "dbe1", "dbe2", "dbe3", "dbe4", "dbe5", "dbe6", "dbe7", "dbe8", "dbe9", "dbe10",
              "dbe11", "dbe12", "dbe13", "dbe14", "dbe15", "dbe16", "dbe17", "dbe18", "dbe19", "dbe20"])
    mkdir(f"result/{i}")
    write_to_csv(result_all, f"result/{i}/dbe{i}.csv")
    datas.insert(0, header)
    write_to_csv(datas, f"result/{i}/result{i}.csv")


if __name__ == "__main__":
    n = 1
    for i in range(1, n+1):
        main(f"data/{i}.csv", i)