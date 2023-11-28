"""
Exercise 2: Write another program that prompts for a list of numbers as
 last excersise (Ch5.ex1) and at the end prints out both the maximum and minimum of the numbers
 instead of the average.

Author: Meri
Date: Nov. 28, 2023
Modified: N/A
"""
total = 0
count = 0
avg = 0
value_list = []
list_min = None
list_max = None

while True :
    user_input = input("Enter a number: ")


    if user_input.lower() == 'done'  or user_input.lower() == 'd' :
        break

    try:
        value = int(user_input)
        count = count + 1
        total = value + total
        value_list.append(value)
    except Exception as e:
        print("please enter a number")
        continue

    if total != 0 and count != 0 :
        avg = total / count

    if value_list :
        list_min = min(value_list)
        list_max = max(value_list)

print('-----------')
print("Total: ", total)
print("Count: ", count)
print("Avg: ", avg)
print("List Min: ", list_min)
print("List max: ", list_max)
print('-----------')
print('madebymeri')
