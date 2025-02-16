def find_kth_closest(arr, target, k):
    selected = k - 1  
    return quick_select(arr, 0, len(arr) - 1, selected, target)

def quick_select(arr, start, end, k, target):
    if start == end:
        return arr[start]
    pivot_index = partition(arr, start, end, target)

    if pivot_index == k:
        return arr[pivot_index]
    elif pivot_index < k:
        return quick_select(arr, pivot_index + 1, end, k, target)
    else:
        return quick_select(arr, start, pivot_index - 1, k, target)

def partition(arr, start, end, target):
    pivot_value = abs(arr[end] - target)  
    pivot_element = arr[end]  
    store_index = start
    for i in range(start, end):
        if abs(arr[i] - target) < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[end] = arr[end], arr[store_index]
    return store_index

readings = [72, 75, 68, 80, 74]
target = 73
k = 2
print("Kth Closest Temperature:", find_kth_closest(readings, target, k))  