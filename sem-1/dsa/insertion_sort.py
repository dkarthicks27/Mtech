# Find execution time and plot the execution time of each algorithm, 
# capturing best case, worst case and average case
# Take an array, which is fully sorted - then randomize it, then reverse the original array.
# Calculate executing time and plot graph for all 3 scenarios for all 3 algorithms.

# arr = [13, 5, -2, 19, 21, 3]
from random import randint, sample
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

li = [randint(-49999, 49990) for _ in range(30000)]

def run_insertion_sort(arr):
    start_time = time.time()
    # print(f"Started insertion_sort: {id}")
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = i
        # print(f"Arr: {arr}")
        
        while pos > 0 and temp < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
            # print(f"\tInt Arr: {arr}\t temp is: {temp}")
        
        arr[pos] = temp
    return round((time.time() - start_time)*1000, 4)

# print(f"\n\nFinal arr: {arr}")

def randomise_arr(arr, size=None):
    if not size:
        size = len(arr)
    return sample(arr, size)


def plotRunTime(arr):
    plot_arr = {}

    for i in tqdm([10, 100, 500, 1000, 2000, 5000, 8000, 10000, 15000, 20000, 25000, 30000]):
        sample_arr = randomise_arr(arr, i)
        timing = run_insertion_sort(sample_arr, randint(-100, 100))
        plot_arr[i] = timing
        print(f"sample-size: {i}\ttiming: {timing}")

    return plot_arr


report = plotRunTime(li)
print(report)

def plot_graph(data: dict):
    plt.figure(figsize=(8, 5))
    sample_sizes = data.keys()
    timings = data.values()
    plt.plot(sample_sizes, timings, marker='o', linestyle='-')
    # plt.xscale('log')  # Optional: makes x-axis logarithmic for better visualization
    # plt.yscale('log')  # Optional: makes y-axis logarithmic if growth is exponential

    # Labels
    plt.title('Timing vs Sample Size')
    plt.xlabel('Sample Size')
    plt.ylabel('Timing (milliseconds)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.show()


plot_graph(report)