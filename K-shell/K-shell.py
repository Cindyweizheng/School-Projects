import igraph as ig
import csv

def calculate_ks(graph):
    return graph.shell_index()

def calculate_ki_ni(graph):
    ki = {}
    ni = {}
    for node in range(graph.vcount()):
        neighbors = graph.neighbors(node)
        ki[node] = len(neighbors)
        two_step_neighbors = set(neighbors)
        for neighbor in neighbors:
            two_step_neighbors.update(graph.neighbors(neighbor))
        # Remove the node itself from the count if present
        two_step_neighbors.discard(node)
        ni[node] = len(two_step_neighbors)
    return ki, ni

def calculate_influence_coefficients(ki, ni):
    return {node: ki[node] * ni[node] for node in ki}

def calculate_di(ki, ni):
    return {node: ni[node] - ki[node] for node in ki}

def calculate_ci(ki, mi, di):
    return {node: ki[node] + mi[node] * di[node] for node in ki}

def kbknr_algorithm(graph):
    ks = calculate_ks(graph)
    ki, ni = calculate_ki_ni(graph)
    mi = calculate_influence_coefficients(ki, ni)
    di = calculate_di(ki, ni)
    ci = calculate_ci(ki, mi, di)

    # 为了进一步区分同层节点的重要性，按照C(i)值排序
    sorted_nodes = sorted(range(len(ci)), key=lambda x: (ks[x], ci[x]), reverse=True)
    return sorted_nodes

def read_graph_from_csv(input_file):
    edges = []
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        node_map = {}  # 用于存储节点名称和节点ID的映射关系
        for row in reader:
            source = row[0]
            target = row[1]
            if source not in node_map:
                node_map[source] = len(node_map)
            if target not in node_map:
                node_map[target] = len(node_map)
            edges.append((node_map[source], node_map[target]))
    graph = ig.Graph.TupleList(edges, directed=False)
    return graph, node_map

def save_to_csv(important_nodes, node_map, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Node'])
        for node_id in important_nodes:
            for name, id_ in node_map.items():
                if id_ == node_id:
                    writer.writerow([name])
                    break

if __name__ == "__main__":
    input_file = "data/0.csv"
    output_file = "result/0.csv"

    # 从CSV文件中读取图
    G, node_map = read_graph_from_csv(input_file)

    # 运行KBKNR算法
    important_nodes = kbknr_algorithm(G)

    # 将结果保存为CSV文件
    save_to_csv(important_nodes, node_map, output_file)
    print(f"Key nodes saved to {output_file}")
