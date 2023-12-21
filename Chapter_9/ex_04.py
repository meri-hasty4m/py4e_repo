'''
Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from
each email address, and print the dictionary.


Add code to the above program to figure out who has the most messages
in the file.

After all the data has been read and the dictionary has been created,
look through the dictionary using a maximum loop (see Section [maximumloop])
to find who has the most messages and print how many messages the person has.


Author: Meri
Date: Dec. 20, 2023
Modified N/A

Personal notes:
The [] after the histogram isn't finding the index, rather the value at the
specified key you pass into it
'''

try:
    fhand = open("../Chapter_7/mbox_short.txt")
except FileNotFoundError:
    print("File not found, please check the filename")
    exit()

histogram = dict()



for lines in fhand :
    if lines.startswith("From ") :
        line = lines.split()
        if len(line) > 2 :
            target_email = line[1]
            histogram[target_email] = histogram.get(target_email, 0) + 1


# Find the email with the most messages
'''
Exactly! When you use max(histogram, key=histogram.get), it indeed compares all
the keys in the histogram dictionary based on their associated values. The
key=histogram.get part tells the max() function to look at the values in the
dictionary for each key and find the key that has the highest value. So, the
function returns the key (in your case, an email address) that corresponds to
the largest value (number of messages) in the histogram.

'''
max_email = max(histogram, key=histogram.get)
print(max_email, histogram[max_email])
