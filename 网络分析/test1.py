from collections import Counter

import igraph as ig
import csv


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


def dict_to_list(data):
    datas = []
    for key, value in data.items():
        datas.append([key, value])
    return datas


def write_to_csv(data, file):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        count = 1
        for da in data:
            writer.writerow(da)
            percent = int(count / len(data) * 50)
            print(f'\r[{"#"*percent}{"."*(50-percent)}]\t{count}/{len(data)}', end=".")
            count += 1
        print()
        f.close()


if __name__ == "__main__":
    datas = read_from_csv("边.csv")
    # datas = read_from_csv("node.csv")
    datas_for_graph = []
    datas_total = []
    for data in datas:
        datas_for_graph.append((data[0], data[1]))
        datas_total.append(data[0])
        datas_total.append(data[1])

    datas_count = Counter(datas_total)
    datas_count = dict_to_list(datas_count)
    datas_temp = []
    for data in datas_count:
        if data[1] >= 9:
            datas_temp.append(data)
    datas_temp.insert(0, ["节点名", "连接的度数"])
    write_to_csv(datas_temp, "result.csv")

    datas_total = list(set(datas_total))
    g = ig.Graph()
    g.add_vertices(datas_total)
    g.vs['label'] = datas_total
    g.add_edges(datas_for_graph)

    layout = g.layout_fruchterman_reingold()
    ig.plot(g, layout=layout, target="test1.png")

    print("度", end=':')
    print(g.degree())
    ebs = g.edge_betweenness()
    print("中介中心性", end=':')
    print(ebs)
    max_eb = max(ebs)
    print("中介中心性较高的边", end=":")
    print([g.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb])
