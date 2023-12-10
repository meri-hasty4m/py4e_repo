'''
Author: Meri 
Date: Dec 9, 2023
Modified: N/A

Purpose: This script is designed to count the frequency of each word entered by a user.
It takes a line of text as input and uses a dictionary to tally the occurrences of each word.
Words are counted in a case-insensitive manner.
'''



counts = dict()
line = input('Enter a line of text: ')
words = line.lower().split()

print("Words", words)

for word in words :
    if word in words :
        counts[word] = counts.get(word, 0) + 1
print('Count: ', counts)
