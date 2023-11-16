"""
Redo the pay exersise ex_03.py from Chapter 1, but with overtime calculated at 1.5x

Author: Meri
Date: Nov. 14, 2023
"""

gross_pay_username = input('What is your name?: ')
hourly_pay = input('Okay ' + gross_pay_username + ' What is your hourly pay?:')
hourly_rate = input('And how many hours do you usually work?:')
hourly_pay = float(hourly_pay)
hourly_rate = float(hourly_rate)
standard_pay = hourly_rate * hourly_pay

if hourly_rate < 40:
    print('Regular')
    print(standard_pay)

else :
    print ('Overtime')
    overtime_hours = (hourly_rate - 40) * 1.5
    overtime_pay = standard_pay + overtime_hours
    print(overtime_pay)


##gross_pay = float(hourly_rate) * float(hourly_pay)
##formatted_pay = "{:.2f}".format(gross_pay)
##print('Pay:', formatted_pay)
