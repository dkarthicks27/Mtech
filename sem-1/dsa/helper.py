from random import randint, sample
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

li = [randint(-49999, 49990) for _ in range(30000)]

def plotRunTime(arr, fn):
    plot_arr = {}

    for i in tqdm([10, 100, 500, 1000, 2000, 5000, 8000, 10000, 15000, 20000, 25000, 30000]):
        sample_arr = randomise_arr(arr, i)
        timing = fn(sample_arr)
        plot_arr[i] = timing
        print(f"sample-size: {i}\ttiming: {timing}")

    return plot_arr

def randomise_arr(arr, size=None):
    if not size:
        size = len(arr)
    return sample(arr, size)

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