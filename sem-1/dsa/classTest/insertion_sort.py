def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = i

        while pos > 0 and temp < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
        
        arr[pos] = temp

    return arr


dummy_arr = [2, 7, 0, -2, 89, 70]

print(insertion_sort(dummy_arr))
