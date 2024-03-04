import time
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quicksort(left) + middle + quicksort(right)

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
    sorted_array = quicksort(array.copy())
    end_time = time.time()
    time_taken = end_time - start_time
    return {
        "time_taken": time_taken,
        "sorted_array": sorted_array  # We keep this for potential future use, even if not displayed.
    }


def main():
    # Define different sizes for the analysis
    sizes = [1000, 10000, 100000, 1000000]
    orders = ['sorted', 'reverse-sorted', 'random']

    # Dictionary to store the results for plotting
    results = {order: [] for order in orders}  # Each order will have its own list of time_taken values

    for size in sizes:
        for order in orders:
            # Generate the array based on the order
            if order == 'sorted':
                array = list(range(1, size + 1))
            elif order == 'reverse-sorted':
                array = list(range(size, 0, -1))
            else:  # 'random'
                array = [random.randint(1, size) for _ in range(size)]

            # Measure the performance of the quicksort on this array
            start_time = time.time()
            quicksort(array.copy())  # Use array.copy() to avoid modifying the original array
            end_time = time.time()
            time_taken = end_time - start_time

            # Append the result for the current order
            results[order].append(time_taken)

    # Now, plotting the results
    plt.figure(figsize=[10, 6])  # Set a figure size for better readability

    for order in orders:
        plt.plot(sizes, results[order], label=f'{order} order',
                 marker='o')  # Plot each order's results with a different marker



    plt.title('QuickSort Performance Analysis')
    plt.xlabel('Array Size')
    plt.ylabel('Time taken (seconds)')
    plt.legend()

    plt.xlim(left=1000)  # This ensures that the x-axis starts from 100

    # Optionally, if you want to set specific ticks on the x-axis:
    plt.xticks(sizes)

    plt.xscale('log')  # Use logarithmic scale for better visibility with large size differences
    plt.yscale('log')  # Optional: Uncomment if the time differences are huge
    plt.grid(True, which="both", ls="--")  # Add grid for better readability
    plt.show()
# Run the main function
if __name__ == "__main__":
    main()


# Run the main function
if __name__ == "__main__":
    main()
