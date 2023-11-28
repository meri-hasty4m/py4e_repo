"""
Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
 Once "done" is entered, print out the total, count, and average of the numbers. If the user
 enters anything other than a number, detect their mistake using try and except and print
 an error message and skip to the next number.

"""
total = 0
count = 0
avg = 0

while True :
    user_input = input("Enter a number: ")

    if user_input.lower() == 'done'  or user_input.lower() == 'd' :
        break

    try:
        value = int(user_input)
        count = count + 1
        total = value + total
    except Exception as e:
        print("please enter a number")
        continue

    if total != 0 and count != 0 :
        avg = total / count


print("Total: ", total)
print("Count: ", count)
print("Avg: ", avg)
