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


if __name__ == "__main__":
    # datas = read_from_csv("边.csv")
    datas = read_from_csv("node.csv")
    datas_for_graph = []
    datas_total = []
    for data in datas:
        datas_for_graph.append((data[0], data[1]))
        datas_total.append(data[0])
        datas_total.append(data[1])
    datas_total = list(set(datas_total))
    g = ig.Graph()
    g.add_vertices(datas_total)
    g.vs['label'] = datas_total
    g.add_edges(datas_for_graph)
    layout = g.layout_fruchterman_reingold()
    ig.plot(g, layout=layout, target="test2.png")
