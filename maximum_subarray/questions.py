#Leetcode -->  169. Majority Element

"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""

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
    
# more optimized solution
def majorityElement(nums):
        nums.sort()
        return nums[len(nums)//2]
    
    
    

"""return a pair in sorrte array whose sum is equal to target"""

def twoSum(numbers, target):
        j = len(numbers)-1
        for i in range(len(numbers)):
            while j > i and numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [arr[i], arr[j]]
        return -1
    
# more optimized solution


def twoSum(numbers, target):
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [arr[i], arr[j]]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return -1
    
arr = [2,7,11,15]
target = 9
print(twoSum(arr, target))