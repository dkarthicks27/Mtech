import time
from tqdm import tqdm
from helper import li, randomise_arr, plot_graph

def plotRunTime(arr):
    plot_arr = {}

    for i in tqdm([10, 100, 500, 1000, 2000, 5000, 8000, 10000, 15000, 20000, 25000, 30000]):
        sample_arr = randomise_arr(arr, i)
        timing = selection_sort(sample_arr)
        plot_arr[i] = timing
        print(f"sample-size: {i}\ttiming: {timing}")
    
    return plot_arr

def selection_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min_pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp


    return round((time.time() - start_time) * 1000, 4)


report = plotRunTime(li)
plot_graph(report)