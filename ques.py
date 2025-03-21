"""Thala's favorite number is 7. Given an integer array a, he wants you to count and print the number of integers that are
divisible by 7 in the array a."""
def divby7(a):
    return sum(1 for i in a if i%7==0)


"""Q2.
K pass in Bubble Sort

Given an integer array a of n elements and an integer k, you need to perform k passes in the Bubble Sort algorithm and print the array after these passes.

Definition of a single pass in Bubble Sort:- 
In a single pass iterate through the entire array form left to right (beginning to end). Compare each element with the next one, and if the current element is greater than the next, swap them.

Read the output and its explanation for the sample testcases for better understanding."""
def bubbleSort(a, n, k):
    for i in range(k):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a


"""Q3.
Power Modulo Expedition
medium
You are given three integers a, b and c. Your task is to compute a<sup>b</sup> % c.

Note:
You are not allowed to use any python built-in functions like pow.
This problem has partial marking, 10% for each test case will be given.
 
Subtask-1 (30% weightage):
1 <= a <= 10<sup>5</sup>
0 <= b <= 10<sup>5</sup>
2 <= c <= 10<sup>5</sup>

Subtask-2 (70% weightage):
1 <= a <= 10<sup>18</sup>
0 <= b <= 10<sup>18</sup>
2 <= c <= 10<sup>18</sup>
"""
def powerMod(a, b, c):
    ans = 1
    a = a % c
    while b > 0:
        if b % 2 == 1:
            ans = (ans * a) % c
        a = (a * a) % c 
        b //= 2 
    return ans



"""Q4.
Seek the Peak
medium
You are given an array arr[] of size N and an integer K, where 1 ≤ K ≤ N. Your task is to find the maximum sum of a subarray of length K.
A subarray is a contiguous segment of the array. The goal is to find the sum of elements in each subarray of length K and return the maximum sum.

Note: Partial marks will be given for suboptimal solutions, Each testcase has 10% weightage.
 

Subtask-1 (50% weightage):
1 <= N <= 10<sup>3</sup>
1 <= K <= 10<sup>3</sup>
 

Subtask-2 (50% weightage):
1 <= N <= 10<sup>5</sup>
1<= K <= 10<sup>5</sup>"""

def maxSum(arr, N, K):
    if N < K:
        return 0 

    current_sum = sum(arr[:K])
    max_sum = current_sum

    for i in range(K, N):
        current_sum += arr[i] - arr[i - K]
        max_sum = max(max_sum, current_sum)

    return max_sum


"""Q5.
RangeQuest
hard
You are given a sorted array arr of N integers. Your task is to complete the given function <code>def count_in_range(arr, L, R)</code> that calculates the count of numbers within a given range [L, R] (inclusive) and return that count.
The array is sorted in non-decreasing order, and you need to determine how many numbers fall between L and R (both inclusive) i.e. numbers which are less than or equal to R and greater than equal to L.

Since this is a functional problem, you just need to complete the function  <code>def count_in_range(arr, L, R)</code> and return the answer.

Note: You need to solve this problem in O(log(n)).’]"""
def lower_bound(arr, target):
    #Finds the first position where arr[i] >= target
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    #Finds the first position where arr[i] > target
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def count_in_range(arr, L, R):
    return upper_bound(arr, R) - lower_bound(arr, L)
