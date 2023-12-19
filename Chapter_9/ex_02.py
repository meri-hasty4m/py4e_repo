'''
Author: Meri
Date : Dec. 19, 2023
Modified: N/A

Write a program that categorizes each mail message by which
day of the week the commit was done. To do this look for
lines that start with "From", then look for the third word
and keep a running count of each of the days of the week.
At the end of the program print out the contents of your
dictionary (order does not matter).

'''
try:
    fhand = open('../Chapter_7/mbox_short.txt')
except FileNotFoundError:
    print("File not Found. Please check the file path")
    exit()

days_of_week_count = dict()

for lines in fhand :
    if lines.startswith("From") and not lines.startswith("From:"):
        line = lines.split()
        if len(line) > 2:
            day = line[2]
            days_of_week_count[day] = days_of_week_count.get(day, 0) + 1

print(days_of_week_count)
