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



"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""


def majorityElement(nums):
    n = len(nums)
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] > n//2:
            return i
    return -1

