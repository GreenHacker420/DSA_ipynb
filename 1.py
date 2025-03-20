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


"""You are managing a multi-level queue scheduling system in an operating system, where processes are assigned to five priority queues based on their importance and urgency.

Let X be a discrete random variable representing the queue to which a randomly chosen process belongs. The probability mass function (PMF) of X, denoted as P(X = i), gives the probability that a process is assigned to Queue i:

Critical Priority (Queue 1): Reserved for critical system tasks, executed immediately with very low waiting time.
High Priority (Queue 2): For high-priority user processes that require fast execution.
Medium Priority (Queue 3): Balanced execution speed and waiting time for most user processes.
Low Priority (Queue 4): For background tasks that are less important but still need attention.
Idle Queue (Queue 5): For processes that can wait indefinitely, such as backups or maintenance tasks.
Each queue also has an average waiting time Wi (in milliseconds) for a process in that queue.

    P(X = i) = pi,  where  i ∈ {1, 2, 3, 4, 5}
    ∑ pi = 1  (i.e., the total probability must sum to 1
Your task is to calculate the expected waiting time E[W] for a randomly chosen process in the system, given by:
              E[W] = ∑ pi Wi

Given values for pi and Wi, compute the expected waiting time E[W].

Input
First line contains an integer n: the number of queues (always 5 in this case).

A list of n tuples, where each tuple contains:  
 - A float p(0≤p≤1): the probability of a process being chosen from that queue.(rounded upto 2 decimals)
 - An integer 
w
w: the average waiting time (in milliseconds) for processes in that queue.
Output
Print the expected waiting time for a process in the system, rounded upto 
2
2 decimal places.

Print -1 when probabilities of being executed doesn't add up to 
1.0
1.0.

Note while checking total probabilities equal to 1.0 please round them upto 2 decimal places (using round())
input
5
0.20 2
0.30 5
0.25 10
0.15 20
0.10 50"""


def merge_sort(n, arr):
    if n == 1:
        return arr  

    mid = n // 2  
    left_half = merge_sort(mid, arr[:mid]) 
    right_half = merge_sort(n - mid, arr[mid:])

    return merge(left_half, right_half) 

def merge(first, second):
    i, j = 0, 0
    sorted_arr = []  

    while i < len(first) and j < len(second):  
        if first[i] < second[j]:  
            sorted_arr.append(first[i])
            i += 1
        else:
            sorted_arr.append(second[j])
            j += 1

    sorted_arr.extend(first[i:])
    sorted_arr.extend(second[j:])

    return sorted_arr

n = int(input())
arr = list(map(int,input().split()))
print(" ".join(map(str, merge_sort(n, arr))))

