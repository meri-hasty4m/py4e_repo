"""
Given a set of integers, write a Python program to filter for a certain number

Author: Meri
Date: Nov. 24, 2023
Modified: N/A
"""

listOfInts = [ 1, 2, 3, 3, 4, 5]

def filter_ints(list) :
    for int in list :
        if int == 3 :
            print('True', int)
        else :
            print('False', int)


filter_ints(listOfInts)
