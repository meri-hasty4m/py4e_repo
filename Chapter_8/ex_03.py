'''
Author: Meri
Date: Dec. 9, 2023
Modified: N/A

Exercise 6: Rewrite the program that prompts the user for a list of numbers
and prints out the maximum and minimum of the numbers at the end when the user
enters "done". Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum numbers
 after the loop completes.

'''

# need to catch for if  a user quits program before numbers are entered
number_list = []

while True :
    user_input = input('Number please: ')

    if user_input.lower() == 'done' or user_input.lower() == 'd' :
        print(max(number_list))
        print(min(number_list))
        break

    try:
        number_list.append(int(user_input))
    except ValueError as v:
        print("From Developer: please enter a valid interger")
        print("From python: ", v)
        continue
