"""
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
"""

def twosum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]
            
print(twosum([2,7,11,15], 9))       #[0,1]
print(twosum([3,2,4], 6))           #[1,2]
print(twosum([3,3], 6))             #[0,1]

def twosum_fast(nums, target):
    d = {}
    for i, num in enumerate(nums):
        d[num] = i
    
    for i, num in enumerate(nums):
        desired = target - num
        if (desired in d) and (d[desired] != i):
            return [i, d[desired]]
            
print(twosum_fast([2,7,11,15], 9))       #[0,1]
print(twosum_fast([3,2,4], 6))           #[1,2]
print(twosum_fast([3,3], 6))             #[0,1]