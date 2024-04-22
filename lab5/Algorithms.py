import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = w

class Algorithms:
    def kruskal(self, graph):
        result = []
        graph_edges = self.get_edges(graph)
        graph_edges.sort(key=lambda x: x[2])  # Sort edges by weight
        parent = {node: node for node in graph}

        for u, v, w in graph_edges:
            if self.find(parent, u) != self.find(parent, v):
                result.append([u, v, w])
                self.union(parent, u, v)

        return result

    def prim(self, graph):
        mst = []
        keys = {node: float('inf') for node in graph}
        keys[0] = 0
        parent = {node: None for node in graph}

        while keys:
            u = min(keys, key=keys.get)
            del keys[u]

            for v in graph[u]:
                if v in keys and graph[u][v] < keys[v]:
                    keys[v] = graph[u][v]
                    parent[v] = u

        for v, p in parent.items():
            if p is not None:
                mst.append([p, v, graph[p][v]])

        return mst

    def get_edges(self, graph):
        edges = []
        for u in graph:
            for v, w in graph[u].items():
                edges.append((u, v, w))
        return edges

    def union(self, parent, u, v):
        p1 = self.find(parent, u)
        p2 = self.find(parent, v)
        parent[p2] = p1

    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def generate_dense_graph(self, nodes):
        graph = {i: {j: random.randint(1, 10) for j in range(nodes) if j != i} for i in range(nodes)}
        return graph

    def generate_sparse_graph(self, nodes, edges):
        graph = {i: {} for i in range(nodes)}
        for _ in range(edges):
            node1, node2 = random.sample(range(nodes), 2)
            weight = random.randint(1, 10)
            graph[node1][node2] = weight
            graph[node2][node1] = weight
        return graph