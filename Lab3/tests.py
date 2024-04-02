import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from Algorithms import ExploreDFS, ExploreBFS
import pandas as pd
from networkx import erdos_renyi_graph

nodeCounts = [4, 8, 16, 32, 64, 128, 256, 512]
dfsDurations = []
bfsDurations = []

# Testing DFS
for count in nodeCounts:
    randomGraph = erdos_renyi_graph(count, 0.5)
    explorer = ExploreDFS()
    for edge in randomGraph.edges:
        explorer.linkNodes(*edge)
    startTime = time.perf_counter()
    explorer.traverse(0)
    endTime = time.perf_counter()
    dfsDurations.append(endTime - startTime)

# Plotting DFS Results
plt.plot(nodeCounts, dfsDurations, label="Depth First Search")
plt.xlabel('Nodes Count')
plt.ylabel('Duration (seconds)')
plt.title('DFS Performance')
plt.legend()
plt.show()

# Testing BFS
for count in nodeCounts:
    randomGraph = erdos_renyi_graph(count, 0.5)
    explorer = ExploreBFS()
    for edge in randomGraph.edges:
        explorer.connect(*edge)
    startTime = time.perf_counter()
    explorer.traverseFrom(0)
    endTime = time.perf_counter()
    bfsDurations.append(endTime - startTime)

# Plotting BFS Results
plt.plot(nodeCounts, bfsDurations, label="Breadth First Search")
plt.xlabel('Nodes Count')
plt.ylabel('Duration (seconds)')
plt.title('BFS Performance')
plt.legend()
plt.show()

# Combined Plot
plt.plot(nodeCounts, dfsDurations, label="DFS")
plt.plot(nodeCounts, bfsDurations, label="BFS")
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Traversal Performance Comparison')
plt.legend()
plt.show()

# Data Presentation
comparisonData = [[n, dfs, bfs] for n, dfs, bfs in zip(nodeCounts, dfsDurations, bfsDurations)]
comparisonDf = pd.DataFrame(comparisonData, columns=["Node Count", "DFS Time", "BFS Time"])
print(comparisonDf)
