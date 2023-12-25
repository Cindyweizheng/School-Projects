import csv


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


def main():
    datas = read_from_csv("data/1.csv")
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
    write_to_csv(datas, [], "result/result_O.csv")


if __name__ == "__main__":
    main()
