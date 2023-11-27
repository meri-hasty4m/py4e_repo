"""
Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
 Once "done" is entered, print out the total, count, and average of the numbers. If the user
 enters anything other than a number, detect their mistake using try and except and print
 an error message and skip to the next number.

"""

total = 0
count = 0

while True :
    user_input = input("Give me a number, or type 'done' to finish: ")

#remember 'done' needs to be first to kill your program
    if user_input == "done" :
        break

    if user_input != None :
        try:
            value = int(user_input)
            count = count +1
            total = total + value
        except Exception as e:
            print("sorry you need to give me a number")
            continue
avg = total / count
print('Total: ', total)
print('Count: ', count)
print('Average: ', avg)
