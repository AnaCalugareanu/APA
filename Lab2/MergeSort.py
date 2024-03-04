import time
import random
import matplotlib
matplotlib.use('TkAgg')  # Use an appropriate backend for your system
import matplotlib.pyplot as plt

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

def analyze_input_data(array):
    size = len(array)
    min_value = min(array)
    max_value = max(array)
    has_duplicates = len(array) != len(set(array))
    if array == sorted(array):
        initial_order = "sorted"
    elif array == sorted(array, reverse=True):
        initial_order = "reverse-sorted"
    else:
        initial_order = "random"
    return {
        "size": size,
        "range": (min_value, max_value),
        "has_duplicates": has_duplicates,
        "initial_order": initial_order
    }

def measure_performance(array):
    start_time = time.time()
    sorted_array = mergesort(array.copy())
    end_time = time.time()
    time_taken = end_time - start_time
    return {
        "time_taken": time_taken,
        "sorted_array": sorted_array
    }

def main():
    sizes = [1000, 10000, 100000, 1000000]
    orders = ['sorted', 'reverse-sorted', 'random']
    results = {order: [] for order in orders}

    for size in sizes:
        for order in orders:
            if order == 'sorted':
                array = list(range(1, size + 1))
            elif order == 'reverse-sorted':
                array = list(range(size, 0, -1))
            else:  # 'random'
                array = [random.randint(1, size) for _ in range(size)]

            performance = measure_performance(array)
            results[order].append(performance['time_taken'])

    plt.figure(figsize=[10, 6])
    for order in orders:
        plt.plot(sizes, results[order], label=f'{order} order', marker='o')

    plt.title('MergeSort Performance Analysis')
    plt.xlabel('Array Size')
    plt.ylabel('Time taken (seconds)')
    plt.legend()
    plt.xlim(left=1000)  # Adjust based on your sizes if needed
    plt.xticks(sizes)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    main()
