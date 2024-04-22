import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import Algorithms as Algorithms
import pandas as pd

values = [4, 8, 16, 32, 64, 128, 256, 512]
timePrimSparse = []
timePrimDense = []
timeKruskalSparse = []
timeKruskalDense = []

Algorithms = Algorithms.Algorithms()
for i in values:
    graph = Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    Algorithms.prim(graph)
    end = time.perf_counter()
    timePrimSparse.append(end - start)

    start = time.perf_counter()
    Algorithms.kruskal(graph)
    end = time.perf_counter()
    timeKruskalSparse.append(end - start)

    graph = Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    Algorithms.prim(graph)
    end = time.perf_counter()
    timePrimDense.append(end - start)

    start = time.perf_counter()
    Algorithms.kruskal(graph)
    end = time.perf_counter()
    timeKruskalDense.append(end - start)

plt.plot(values, timePrimSparse, label="Prim Sparse")
plt.plot(values, timePrimDense, label="Prim Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Prim Algorithm')
plt.legend()  # Adding legend
plt.show()

plt.plot(values, timeKruskalSparse, label="Kruskal Sparse")
plt.plot(values, timeKruskalDense, label="Kruskal Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Kruskal Algorithm')
plt.legend()  # Adding legend
plt.show()

plt.plot(values, timePrimSparse, label="Prim Sparse")
plt.plot(values, timePrimDense, label="Prim Dense")
plt.plot(values, timeKruskalSparse, label="Kruskal Sparse")
plt.plot(values, timeKruskalDense, label="Kruskal Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Minimum Spanning Tree Algorithms')
plt.legend()  # Adding legend
plt.show()

data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timePrimSparse[i], timePrimDense[i], timeKruskalSparse[i], timeKruskalDense[i]])

df = pd.DataFrame(data, columns=["Nodes", "Prim Sparse", "Prim Dense", "Kruskal Sparse", "Kruskal Dense"])
print(df)