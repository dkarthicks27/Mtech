def run_quick_sort(arr):
    if len(arr) == 1:
        return arr

    last = arr[-1]
    i = -1
    j = 0

    while j != len(arr) - 1:
        print(f"start: i = {i}\t j = {j}\t arr={arr}")
        if arr[j] < last:
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            j += 1
        else:
            j += 1
        print(f"end: i = {i}\t j = {j}\t arr={arr}", end="\n\n")

    temp = arr[i + 1]
    arr[i + 1] = last
    arr[-1] = temp
    print(f"Current - i = {i}\t j = {j}\t arr={arr}")
    return run_quick_sort(arr[:i]) + [last] + run_quick_sort(arr[i:])


run_quick_sort([7, 2, 1, 8, 6, 3, 5, 4])