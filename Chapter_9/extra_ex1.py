'''

Author: Meri
Date: Dec. 20, 2023
Modified: N/A

The following is an extra excersise generated by Chat GPT.

Improvments will include making file follow single responsibility principle. 


Objective: Write a program to read through the mail log and figure out the distribution of email messages by hour of the day. Build a histogram to count how many messages have timestamps for each hour of the day (regardless of the date the message was sent).

Steps:

    Read through the file line by line.
    Look for lines that start with "From" (similar to your previous exercise).
    For these lines, extract the time and then the hour from the time.
    Count how often each hour appears and store it in a histogram (dictionary).

Expected Output: A dictionary where each key is an hour (00, 01, 02, ..., 23) and each value is the number of emails sent during that hour.

This exercise will help you practice parsing strings and working with dictionaries in Python. It adds an extra layer of complexity in terms of string manipulation, as you'll need to extract and work with specific parts of the strings.

'''

def test() :
    try:
        fhand = open('../Chapter_7/mbox_short.txt')
    except FileNotFoundError:
        print("File not found, please correct path or choose new file")
        exit()

    histogram = dict()

    for lines in fhand :
        if lines.startswith('From ') :
            line = lines.split()
            target_text = line[5]
            hour_of_day = target_text[:2]
            if len(hour_of_day) > 1 :
                histogram[hour_of_day] = histogram.get(hour_of_day, 0) +1

    print(histogram)



test()
