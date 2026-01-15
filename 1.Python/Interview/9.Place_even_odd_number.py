"""
Write a program to place even number in even index and odd number in odd index
"""
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def arrange_number(lst):
    n = len(lst)
    even_numbers = [i for i in lst if i % 2 == 0]
    odd_numbers = [j for j in lst if j % 2 != 0]
    
    even_index = 0
    odd_index = 1
    final = [None]*n
    
    for i in even_numbers:
        final[even_index] = i
        even_index += 2
    
    for j in odd_numbers:
        final[odd_index] = j
        odd_index += 2
    print(final)


arrange_number(input_list)