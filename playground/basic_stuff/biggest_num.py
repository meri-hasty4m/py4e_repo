"""
Getting biggest number in an set of numbers.

Author: Meri
Date: Nov. 20, 2023
Modified: Nov. 27, 2023
    - Added Smallest Num
"""

import random
import math

##for i in range(10):
##    x = random.random()
##    print(x)

##def print_twice(a, b):
##    print(a + math.pi, b)
#    print(a + math.pi, b)

#print_twice(3 * 2, 4)

ints = [ 3, 4, 93, 94, 22]

biggest_num = None
def largest_so_far(set):
    global biggest_num
    for num in ints :
        if biggest_num is None :
            biggest_num = num
        elif num > biggest_num :
            biggest_num = num
    print('Biggest: ', biggest_num)

def smallest_so_far(set):
    smallest_num = None
    for num in ints :
        if smallest_num is None :
            smallest_num = num
        elif num < smallest_num :
            smallest_num = num
    print('Smallest ', smallest_num)

largest_so_far(ints)
smallest_so_far(ints)
