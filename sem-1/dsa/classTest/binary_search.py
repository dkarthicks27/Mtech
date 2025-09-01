def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    
    return -1


arr = [-5, 3, 17, 19, 23, 25, 26]
print(binary_search(arr, 26))

