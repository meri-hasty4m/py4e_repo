'''
Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Author: Meri
Date: Dec. 19, 2023
Modified: N/A

'''

histogram = dict()

try:
    fhand = open("../Chapter_7/mbox_short.txt")
except FileNotFoundError:
    print("File not found, please check the filename")
    exit()

for lines in fhand :
    if lines.startswith("From ") :
        line = lines.split()
        if len(line) > 1 :
            email = line[1]
            histogram[email] = histogram.get(email, 0) + 1

print(histogram)
