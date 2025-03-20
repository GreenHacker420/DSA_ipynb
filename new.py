# """A sequence is defined as follows:

# The first two terms of the sequence are:

# 1st term = 1
# 2nd term = 1
# For 3rd term and beyond:
# For i >= 3:
# i<sup>th</sup> term = ((i-1)<sup>th</sup> term) + 3 x ((i-2)<sup>th</sup> term)

# Given an integer n, determine the nth term of the sequence.

# <b>Note: </b> This is a functional problem, you don't have to take any input. You just have to complete the function find(n) and return the required value."""

# def find(n):
#     if n == 1 or n == 2:
#         return 1
#     a=1
#     b=1
#     for i in range(3,n+1):
#         c=a+3*b
#         a=b
#         b=c
#     return c


# """You are given a string of length 𝑁 consisting of only the characters 'a' and 'b'. 
# Your task is to determine whether the count of 'a' in the string is strictly greater than the count of 'b'."""


# def countA(s):
#     return s.count('a')>s.count('b')
# s = input()
# print(countA(s))


# """You are given a sorted array arr of size n, sorted in non-decreasing order and an integer target. Your task is to find the count of 
# elements in the array that are less than or equal to the target.

# Note:

# The target always exists in the array.
# There can be duplicate elements as well.
# <code> This is a functional problem, you don't have to take any input or print any output. Just complete the given function and return the required. </code>"""


# def countElements(arr, target):
#     l, r = 0, len(arr)-1
#     while l<r:
#         mid = (l+r)//2
#         if arr[mid]<=target:
#             l = mid+1
#         else:
#             r = mid
#     return l
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 5
# print(countElements(arr, target))



# """You are given an array of integers. Your task is to find the number of subsequences in the array such that the sum of the 
# elements in the subsequence is odd.

# A subsequence is defined as any sequence derived from the array by deleting some or no elements, without changing the order of the 
# remaining elements."""


# def count_odd_sum_subsequences(arr):
#     MOD = 10**9 + 7
#     n = len(arr)
    
#     odd_count = sum(1 for x in arr if x % 2 != 0)
    
#     if odd_count == 0:
#         return 0  # If no odd numbers, no odd sum subsequences
    
#     total_subsequences = pow(2, n, MOD) - 1
#     return total_subsequences // 2



# # """Given an array of n integers representing the workloads of n tasks, and an integer k representing the number of workgroups, 
# # you need to divide the array into k contiguous subarrays (workgroups). Your goal is to minimize the maximum sum of workloads in any of these subarrays.

# # In other words, you are asked to determine the optimal way to split the tasks into k contiguous parts, such that the largest sum of any subarray 
# # (workgroup) is as small as possible."""

# # def min_max_workload(workloads, k):
# #     def is_possible(max_sum):
# #         count = 1
# #         current_sum = 0
# #         for workload in workloads:
# #             if current_sum + workload <= max_sum:
# #                 current_sum += workload
# #             else:
# #                 count += 1
# #                 current_sum = workload
# #         return count <= k
    
# #     l, r = max(workloads), sum(workloads)
# #     while l < r:
# #         mid = (l + r) // 2
# #         if is_possible(mid):
# #             r = mid
# #         else:
# #             l = mid + 1
# #     return l

# """You are given an integer array nums. The absolute sum of a subarray numsl, numsl + 1, ..., numsr - 1, numsr is abs(numsl + numsl + 1 +  ... + numsr - 1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note: abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x."""


# def maxAbsoluteSum(nums):
#     max_sum = 0
#     min_sum = 0
#     current_sum = 0
#     for num in nums:
#         current_sum += num
#         max_sum = max(max_sum, current_sum)
#         min_sum = min(min_sum, current_sum)
#     return max_sum - min_sum


# """You are given a sorted array arr of size n, sorted in non-decreasing order and an integer target. 
# Your task is to find the count of elements in the array that are greater than or equal to the target."""

# def count_greater_or_equal(arr, target):
#     l , r = 0, len(arr)-1
#     while l<r:
#         mid = (l+r)//2
#         if arr[mid]>=target:
#             r = mid
#         else:
#             l = mid+1
#     return len(arr)-l


    