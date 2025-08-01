from random import randint, sample
from stqdm import stqdm
AVG = 'average'
BEST = 'best'
WORST = 'worst'

def randomise_arr(arr, size=None):
    if not size:
        size = len(arr)
    return sample(arr, size)

def chartRunTime(arr, algo, step_arr):
    plot_arr = {AVG: {}, BEST: {}, WORST: {}}

    # Average case
    for i in stqdm(step_arr, desc="Running Average case.."):
        sample_arr = randomise_arr(arr, i)
        timing = algo(sample_arr)
        plot_arr[AVG][i] = timing
    
    # Best case
    arr.sort()
    for i in stqdm(step_arr, desc="Running Best case.."):
        sample_arr = arr[:i]
        timing = algo(sample_arr)
        plot_arr[BEST][i] = timing

    # worst case
    arr = arr[::-1]
    for i in stqdm(step_arr, desc="Running Worst case.."):
        sample_arr = arr[:i]
        timing = algo(sample_arr)
        plot_arr[WORST][i] = timing
    return plot_arr