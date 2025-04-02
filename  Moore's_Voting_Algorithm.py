# Moore's Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)


# def majorityElement(nums):
#     count = 0
#     candidate = None
#     for i in nums:
#         if count == 0:
#             candidate = i
#         if i == candidate:
#             count += 1
#         else:
#             count -= 1
#     return candidate

arr = [2,2,1,1,1,2,2]
# print(majorityElement(arr))

#changes

freq = 0
ans = 0

for i in arr:
    if freq == 0:
        ans = i
    if i == ans:
        freq += 1
    else:
        freq -= 1
print(ans)