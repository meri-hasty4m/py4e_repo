"""
Getting biggest number in an set of numbers.

Author: Meri
Date: Nov. 20, 2023
Modified: Nov. 27, 2023
    - Added Smallest Num
    - Consolidated if statement to have 'or'
"""

numbers = [ 3, 4, 93, 94, 22]


def largest_so_far(ints):
    biggest_num = None
    for num in ints :
        if biggest_num is None  or num > biggest_num:
            biggest_num = num
    print('Biggest: ', biggest_num)

def smallest_so_far(ints):
    smallest_num = None
    for num in ints :
        if smallest_num is None or num < smallest_num:
            smallest_num = num
    print('Smallest ', smallest_num)

largest_so_far(numbers)
smallest_so_far(numbers)
print(sum(numbers))
print(len(numbers))
print(min(numbers))
print(max(numbers))
