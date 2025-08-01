def run_merge_sort(arr):
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

    sub_arr1 = run_merge_sort(arr[:len(arr)//2])
    sub_arr2 = run_merge_sort(arr[len(arr)//2:])
    return merge(sub_arr1, sub_arr2)


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


print(run_merge_sort([1, 9, 14, -9]))