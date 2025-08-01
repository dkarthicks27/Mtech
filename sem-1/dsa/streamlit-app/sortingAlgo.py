import time

def run_insertion_sort(arr):
    start_time = time.time()

    for i in range(1, len(arr)):
        temp = arr[i]
        pos = i
        
        while pos > 0 and temp < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = temp
    
    return round((time.time() - start_time) * 1000, 2)


def run_selection_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min_pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp


    return round((time.time() - start_time) * 1000, 2)

def run_merge_sort(arr):
    def perform_merge(arr):
        def merge(arr1, arr2):
            i = 0
            j = 0
            
            merged_arr = []
            k = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged_arr.append(arr1[i])
                    i += 1
                elif arr2[j] < arr1[i]:
                    merged_arr.append(arr2[j])
                    j += 1
                else:
                    merged_arr.append(arr1[i])
                    merged_arr.append(arr2[j])
                    i += 1
                    j += 1
            
            if i != len(arr1):
                merged_arr.extend(arr1[i:])
            elif j != len(arr2):
                merged_arr.extend(arr2[j:])
            return merged_arr
        
        if len(arr) == 1:
            return arr

        sub_arr1 = perform_merge(arr[:len(arr)//2])
        sub_arr2 = perform_merge(arr[len(arr)//2:])
        return merge(sub_arr1, sub_arr2)
    
    start_time = time.time()
    perform_merge(arr)
    return round((time.time() - start_time) * 1000, 2)

def run_quick_sort(arr):
    pass