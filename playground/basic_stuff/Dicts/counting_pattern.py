'''
Author: Meri
Date: Dec. 9, 2023
Modified: Dec. 9, 2023

Purpose: This script is designed to count the frequency of each word entered by a user.
It takes a line of text as input and uses a dictionary to tally the occurrences of each word.
Words are counted in a case-insensitive manner.
'''



counts = dict()
line = input('Enter a line of text: ')
words = line.lower().split()



for word in words :
    if word in words :
        counts[word] = counts.get(word, 0) + 1

print("Words", words)
print('Count: ', counts)


## duplicate data
