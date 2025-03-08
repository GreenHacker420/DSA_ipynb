#printing all subarrays of an array

def subarrays(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1] , end = " ")
        print()            
arr = [1,2,3,4]
subarrays(arr)
