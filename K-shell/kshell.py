import networkx as nx


def calculate_ks(graph):
    # 计算并返回每个节点的K-shell值
    return nx.core_number(graph)


def calculate_ki_ni(graph):
    ki = {}
    ni = {}
    for node in graph.nodes:
        neighbors = list(nx.neighbors(graph, node))
        ki[node] = len(neighbors)
        two_step_neighbors = set(neighbors)
        for neighbor in neighbors:
            two_step_neighbors.update(nx.neighbors(graph, neighbor))
        # Remove the node itself from the count if present
        two_step_neighbors.discard(node)
        ni[node] = len(two_step_neighbors)
    return ki, ni


def calculate_influence_coefficients(ki, ni):
    # 根据公式μi=K(i)N(i)计算每个节点的影响系数
    return {node: ki[node] / ni[node] for node in ki}


def calculate_di(ki, ni):
    # 根据公式D(i)=N(i)−K(i)计算次邻居节点个数
    return {node: ni[node] - ki[node] for node in ki}


def calculate_ci(ki, mi, di):
    # 根据公式C(i)=K(i)+μiD(i)计算节点的综合度
    return {node: ki[node] + mi[node] * di[node] for node in ki}


def kbknr_algorithm(graph):
    ks = calculate_ks(graph)
    ki, ni = calculate_ki_ni(graph)
    mi = calculate_influence_coefficients(ki, ni)
    di = calculate_di(ki, ni)
    ci = calculate_ci(ki, mi, di)

    # 为了进一步区分同层节点的重要性，按照C(i)值排序
    sorted_nodes = sorted(ci.keys(), key=lambda x: (ks[x], ci[x]), reverse=True)
    return sorted_nodes


# 测试算法
if __name__ == "__main__":
    G = nx.Graph()
    edges = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7)]
    G.add_edges_from(edges)

    important_nodes = kbknr_algorithm(G)
    print("Nodes sorted by importance:", important_nodes)
