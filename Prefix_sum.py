def prefix_sum(arr):
    n = len(arr)
    pre = [0]*n
    pre[0] = arr[0]
    for i in range(1,n):
        pre[i] = pre[i-1] + arr[i]
    return pre