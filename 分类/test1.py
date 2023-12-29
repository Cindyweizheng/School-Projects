

def main():
    print("work start")
    datas = [["1"], ["2"], ["3"]]
    datas[0].append(0)
    new_data = datas
    datas[0][1] = 2
    new2_data = datas
    print(new_data)
    print(new2_data)


if __name__ == "__main__":
    main()