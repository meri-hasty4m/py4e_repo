"""
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F
~~~

Author: Meri
Date: Nov. 16, 2023
Modified: N/A
"""

name = input("What is your name?")
score = input(name + ' What is your score?')

try:
    score = float(score)
except :
    print('Error, please enter a numerical value.... exiting program')
    exit()

if score > 0.0 and score < 1.0:
    if score >= 0.9 :
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        pring('D')
    else :
        print('F')
else :
    print("Error, Please enter a value between 0.0 - 1.0")
