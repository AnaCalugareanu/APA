import time
import random
import matplotlib
matplotlib.use('TkAgg')  # Use an appropriate backend for your system
import matplotlib.pyplot as plt

# Sorting Algorithms
def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def mergesort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Measure performance
def measure_performance(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())
    end_time = time.time()
    return end_time - start_time

# Main function to run the analysis
def main():
    sizes = [100, 1000, 10000, 20000]  # Adjusted for practical runtime considerations
    algorithms = {
        'QuickSort': quicksort,
        'MergeSort': mergesort,
        'HeapSort': heapsort,
        'InsertionSort': insertion_sort
    }
    results = {name: [] for name in algorithms}

    for size in sizes:
        array = [random.randint(1, size) for _ in range(size)]  # Only random arrays

        for name, sort_function in algorithms.items():
            time_taken = measure_performance(sort_function, array)
            results[name].append(time_taken)
            print(f'{name} with random array of size {size}: {time_taken:.5f} seconds')

    # Plotting the results
    plt.figure(figsize=[12, 8])
    markers = ['o', '^', 's', 'D']  # Different markers for different algorithms
    for (name, marker) in zip(algorithms.keys(), markers):
        plt.plot(sizes, results[name], marker=marker, label=name)

    plt.title('Sorting Algorithm Performance Comparison (Random Arrays)')
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    main()
