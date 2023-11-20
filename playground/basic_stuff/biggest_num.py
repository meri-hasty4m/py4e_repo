"""
Getting biggest number in an set of numbers.

Author: Meri
Date: Nov. 20, 2023
Modified: N/A
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

biggest_num = -1
def largest_so_far():
    global biggest_num
    for num in [ 3, 4, 93, 94, 22] :
        if num > biggest_num :
            biggest_num = num
    print(biggest_num)

largest_so_far()
