arr = [23, 17, 16, -2, 91, 0]

def bubble_sort(arr):
    for i in range(len(arr)):
        print(f"Iteration No: {i+1}")
        for j in range(len(arr) - i - 1):
            print(arr)
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1] 
                arr[j + 1] = arr[j]
                arr[j] = temp
        print(arr)
        print("\n\n")

bubble_sort(arr)