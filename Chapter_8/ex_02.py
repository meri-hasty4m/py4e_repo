'''
Author: Meri
Date: Dec. 9, 2023
Modified: N/A

Exercise 5: Write a program to read through the mail box data and when you
find line that starts with "From", you will split the line into words using
the split function. We are interested in who sent the message, which is the
second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a
count at the end.



'''

fhand = open('../Chapter_7/mbox_short.txt')

count = 0

for line in fhand :
    if line.startswith('From') :
        count += 1
        single_line = line.split()
        target_text = single_line[1]
        print("Message sent from:", target_text)

print("Final count of email addresses:" , count)
