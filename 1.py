# #printing all subarrays of an array

# def subarrays(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i,n):
#             print(arr[i:j+1] , end = " ")
#         print()            
# arr = [1,2,3,4]
# subarrays(arr)



# #finding the sum of all subarrays of an array brute force approach

# def sum_subarrays(arr):
#     n = len(arr)
#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum += arr[j]
#             print(sum , end = " ")
#         print()
# arr = [1,2,3,4]
# sum_subarrays(arr)
