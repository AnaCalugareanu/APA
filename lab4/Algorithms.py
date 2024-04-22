import sys
import random


class Algorithms:
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(graph):
            current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])
            visited.add(current_node)

            for neighbor, weight in graph[current_node].items():
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        return distances

    def floyd_warshall(graph):
        dist = {i: {j: float('inf') for j in graph} for i in graph}
        for i in graph:
            dist[i][i] = 0
            for j, w in graph[i].items():
                dist[i][j] = w

        for k in graph:
            for i in graph:
                for j in graph:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def generate_sparse_graph(nodes, edges):
        graph = {i: {} for i in range(nodes)}
        for _ in range(edges):
            node1, node2 = random.sample(range(nodes), 2)
            weight = random.randint(1, 10)
            graph[node1][node2] = weight
            graph[node2][node1] = weight
        return graph

    def generate_dense_graph(nodes):
        graph = {i: {j: random.randint(1, 10) for j in range(nodes) if j != i} for i in range(nodes)}
        return graph