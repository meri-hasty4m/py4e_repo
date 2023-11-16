"""
Redo the pay exersise ex_03.py from Chapter 1, but with overtime calculated at 1.5x

Author: Meri
Date: Nov. 14, 2023
Modified: Nov. 16, 2023 
"""

hourly_pay = input(' What is your hourly pay?:')
hours_worked = input('And how many hours do you usually work?:')
hourly_pay = float(hourly_pay)
hours_worked = float(hours_worked)
standard_pay = hours_worked * hourly_pay

if hours_worked <= 40:
    print('Regular')
    print(standard_pay)
else :
    print ('Overtime')
    overtime_hours = hours_worked - 40
    overtime_rate = (hourly_pay * 1.5)
    total_with_overtime = (overtime_hours * overtime_rate) + (hourly_pay * 40)
    print(total_with_overtime)
