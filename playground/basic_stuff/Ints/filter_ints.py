"""
Given a set of integers, write a Python program to filter for a certain number

Author: Meri
Date: Nov. 24, 2023
Modified: Nov. 24, 2023
"""

listOfInts = [ 1, 2, 3, 3, 4, 5]
found = False

def filter_ints(list) :
    for int in list :
        if int == 3 :
            found = True
            print(found, int)
        else :
            found = False
            print(found , int)


filter_ints(listOfInts)
