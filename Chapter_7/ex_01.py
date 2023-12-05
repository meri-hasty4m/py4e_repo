"""
Exercise 1: Write a program to read through a file and print
 the contents of the file (line by line) all in upper case.

 Author: Meri
 Date: Dec. 4, 2023
 Modified: N/A

 """


filename = ("mbox_short.txt")
fhand = open(filename)
for line in fhand :
    print(line.upper().strip())
