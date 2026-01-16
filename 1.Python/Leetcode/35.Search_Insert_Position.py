"""
Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

nums = [1,3,5,6]
target = 5
nums1 = [1,3,5,6]
target1 = 2
nums2 = [1,3,5,6]
target2 = 7

"""
This is not O(log n) complexity
"""
def searchInsert(target, nums):
    if target in nums:
        return nums.index(target)
    else:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            for i in range(len(nums)-1):
                if target > nums[i] and target < nums[i+1]:
                    return i+1
            
        
print(searchInsert(target, nums))       #2
print(searchInsert(target1, nums1))     #1
print(searchInsert(target2, nums2))     #4

"""
This is O(log n) Time complexity. Binary Search Algorithm used to achieve O(log n) Time Complexity.
"""
print("Binary Search used. Time Complexity O(log n) for below answers")
def searchInsert_BS(target, nums):
    firstIndex = 0
    lastIndex = len(nums) -1
    
    while firstIndex <= lastIndex:
        midIndex = (firstIndex + lastIndex) // 2
        if nums[midIndex] == target:
            return midIndex
        elif nums[midIndex] > target:
            lastIndex = midIndex - 1
        else:
            firstIndex = midIndex + 1
    return firstIndex
        
print(searchInsert_BS(target, nums))       #2
print(searchInsert_BS(target1, nums1))     #1
print(searchInsert_BS(target2, nums2))     #4