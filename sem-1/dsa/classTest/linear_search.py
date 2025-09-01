def linear_search(arr, target):
    for i in range(0, len(arr)):
        print(f"Index pos: {i}\tvalue is: {arr[i]}")
        if arr[i] == target:
            return i
        
    return -1

arr = [-5, 3, 17, 19, 23, 25, 26]

print(linear_search(arr, 26))