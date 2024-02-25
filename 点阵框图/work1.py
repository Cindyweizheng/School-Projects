import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    print("work start!")
    datas = np.array(pd.read_excel("副本副本原数.xlsx", "Sheet1"))
    arr_datas = np.array(pd.read_excel("副本副本原数.xlsx", "Sheet2"))
    datas = np.delete(datas, 0, axis=0)
    datas = np.delete(datas, 0, axis=0)
    datas = datas.T
    datas_P = [(datas[0], datas[1], 'r'), (datas[2], datas[3], 'g'), (datas[4], datas[5], 'b'), (datas[6], datas[7], 'y')]
    for x, y, color in datas_P:
        plt.scatter(x, y, color=color, s=1)
    arr_datas = np.delete(arr_datas, 0, axis=0)
    arr_datas = np.delete(arr_datas, 0, axis=0)
    arr_datas = arr_datas.T
    arr_P = [(arr_datas[0], arr_datas[1], 'r'), (arr_datas[2], arr_datas[3], 'g'), (arr_datas[4], arr_datas[5], 'c'), (arr_datas[6], arr_datas[7], 'c'), 
             (arr_datas[8], arr_datas[9], 'm'), (arr_datas[10], arr_datas[11], 'y'), (arr_datas[12], arr_datas[13], 'lightyellow'), (arr_datas[14], arr_datas[15], 'lightgrey')]
    for x, y, color in arr_P:
        plt.fill(x, y, color, alpha=0.5)
    plt.title("work1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()