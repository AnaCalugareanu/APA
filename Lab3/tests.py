from Algorithms import NetworkMap
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import time
import graphviz

networks = []

for i in range(10):
    network = NetworkMap()
    for j in range(10):
        network.linkNodes(j, random.randint(0, 9))
    networks.append(network)

for i, network in enumerate(networks):
    graphVisual = graphviz.Digraph(comment='Network Visualization')
    for node in network.connections:
        for neighbor in network.connections[node]:
            graphVisual.edge(str(node), str(neighbor))
    graphVisual.render('network' + str(i))

executionTimeDFS = []
executionTimeBFS = []

for network in networks:
    start = time.perf_counter()
    network.traverseDFS(1)
    end = time.perf_counter()
    executionTimeDFS.append(end - start)

    start = time.perf_counter()
    network.traverseBFS(1)
    end = time.perf_counter()
    executionTimeBFS.append(end - start)

plt.plot(range(1, len(networks) + 1), executionTimeDFS, label="DFS Time")
plt.plot(range(1, len(networks) + 1), executionTimeBFS, label="BFS Time")
plt.xlabel('Network Instance')
plt.ylabel('Execution Time')
plt.title('Performance Analysis: DFS vs BFS')
plt.legend()
plt.show()
