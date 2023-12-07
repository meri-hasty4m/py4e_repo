'''
Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is
not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.


Author: Meri
Date: Dec. 6, 2023
Modified: N/A
'''

fhand = open('romeo.txt')


new_list = list()

for lines in fhand :
    split_list = lines.split()
    for word in split_list :
        if word not in new_list :
            new_list.append(word.lower())
final_list = sorted(new_list)
print(final_list)
