"""
Write a program to find the second largest number in a list.
"""

a_list = [12, 35, 1, 10, 34, 1]

def second_largest_number(num_list):
    unique_list = list(set(num_list))
    sort_unique_list = sorted(unique_list)
    return sort_unique_list[-2]

print(second_largest_number(a_list))

"""
Write a program to find the second largest number in a list without using inbuilding functions.
bubble sort -- assending
"""

def bubble_sort_asc(numbList):
    n = len(numbList)

    for i in range(n):
        for j in range(0, n-i-1):
            if numbList[j] > numbList[j+1]:
                numbList[j], numbList[j+1] = numbList[j+1], numbList[j]
    return numbList

sorted_list = bubble_sort_asc(a_list)
print(sorted_list[-2])

"""
Write a program to find the second largest number in a list without using inbuilding functions.
bubble sort -- desending
"""
def bubble_sort_dsc(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

sorted_dsc = bubble_sort_dsc(a_list)
print(f"second largest number in the list is  :- {sorted_dsc[1]}")