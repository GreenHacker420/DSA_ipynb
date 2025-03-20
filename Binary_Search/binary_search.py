def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#binary search using recursion

def binary_search_rec(arr, target, left, right):
    mid = left + (right - left) // 2
    if left <= right:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_rec(arr, target, mid+1, right)
        else:
            return binary_search_rec(arr, target, left, mid-1)
    return -1




