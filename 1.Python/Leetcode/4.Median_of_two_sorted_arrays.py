"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of 
the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

def findMedianSortedArrays(nums1, nums2):
    num = nums1 + nums2
    num = sorted(num)
        # print(num)

    n = len(num)
    if n%2 == 0:
            # print(n//2)
        mid = n//2
        return ((num[mid]+num[mid-1])/2)        
    else:
        return (num[n//2])
    
print(findMedianSortedArrays([1,3], [2]))       #2
print(findMedianSortedArrays([1,2], [3,4]))     #2.5