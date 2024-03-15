def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid+1
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
print(binary_search(arr, target, 0, len(arr) - 1))