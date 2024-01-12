import csv
import igraph as ig


def read_from_csv(filename):
    csvfile = open(filename, "r")
    reader = csv.reader(csvfile)
    result = []
    for item in reader:
        if reader.line_num == 1:
            continue
        result.append(item)
    csvfile.close()
    return result


def main():
    datas = read_from_csv("result(node).csv")
    print(type(datas))
    del_datas = []
    for data in datas:
        del_datas.append(data[0])
        del_datas.append(data[1])
    datas_total = list(set(del_datas))
    g = ig.Graph()
    g.add_vertices(datas_total)
    g.vs['label'] = datas_total
    g.add_edges(datas)

    layout = g.layout_fruchterman_reingold()
    ig.plot(g, layout=layout, target="test1.png")


if __name__ == '__main__':
    main()
