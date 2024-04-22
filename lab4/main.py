import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import Algorithms
import pandas as pd

values = [4, 8, 16, 32, 64, 128, 256, 512]
timeDijkstraSparse = []
timeDijkstraDense = []
timeFloydWarshallSparse = []
timeFloydWarshallDense = []
for i in values:
    graph = Algorithms.Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    Algorithms.Algorithms.dijkstra(graph, 0)
    end = time.perf_counter()
    timeDijkstraSparse.append(end - start)

    graph = Algorithms.Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    Algorithms.Algorithms.dijkstra(graph, 0)
    end = time.perf_counter()
    timeDijkstraDense.append(end - start)

    graph = Algorithms.Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    Algorithms.Algorithms.floyd_warshall(graph)
    end = time.perf_counter()
    timeFloydWarshallSparse.append(end - start)

    graph = Algorithms.Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    Algorithms.Algorithms.floyd_warshall(graph)
    end = time.perf_counter()
    timeFloydWarshallDense.append(end - start)

plt.plot(values, timeDijkstraSparse, label="Dijkstra Sparse")
plt.plot(values, timeDijkstraDense, label="Dijkstra Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Dijkstra Algorithm')
plt.legend()  # Adding legend
plt.show()

plt.plot(values, timeFloydWarshallSparse, label="Floyd-Warshall Sparse")
plt.plot(values, timeFloydWarshallDense, label="Floyd-Warshall Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Floyd-Warshall Algorithm')
plt.legend()  # Adding legend
plt.show()

plt.plot(values, timeDijkstraSparse, label="Dijkstra Sparse")
plt.plot(values, timeDijkstraDense, label="Dijkstra Dense")
plt.plot(values, timeFloydWarshallSparse, label="Floyd-Warshall Sparse")
plt.plot(values, timeFloydWarshallDense, label="Floyd-Warshall Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Shortest Path Algorithms')
plt.legend()  # Adding legend
plt.show()

data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timeDijkstraSparse[i], timeDijkstraDense[i], timeFloydWarshallSparse[i], timeFloydWarshallDense[i]])
# Display results in a tables
headers = ["Input Size", 'Dijkstra Sparse', 'Dijkstra Dense', 'Floyd-Warshall Sparse', 'Floyd-Warshall Dense']
df = pd.DataFrame(data, columns=headers)
print(df)


