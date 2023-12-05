"""
Exercise 2: Write a program to prompt for a file name,
and then read through the file and look for lines of the form:


X-DSPAM-Confidence:0.8475

When you encounter a line that starts with
"X-DSPAM-Confidence:" pull apart the line to extract the
floating-point number on the line. Count these lines and
then compute the total of the spam confidence values
from these lines. When you reach the end of the file,
 print out the average spam confidence.

Author: Meri
Date: Dec. 4, 2023
Modified: N/A

"""
# - Meri
# 1. extract floating point number from target_string
# 2. Count the lines with this number
# 3. Compute the sum of spam confidence values
# 4. Print the average Span Confidence


filename = "mbox_short.txt"
fhand = open(filename)
count = 0
sum = 0


for line in fhand :
    if line.startswith('X-DSPAM-Confidence:') :
        target_text = line.find(':')
        try:
            number = float(line[target_text  + 1:].strip())
            count +=  1
            sum +=  number
        except ValueError as v:
            print("Error: ", v)
avg = sum / count
print("Average spam confidence: ", avg)
