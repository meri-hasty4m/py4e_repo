fhand = open('../../../Chapter_8/romeo.txt')

# Initialize and emply dictionary to store word counts
counts = dict()

# Reading each line and spliting into individual words
for line in fhand :
    words = line.split()
# Count the occurence of each word and update the dictionary
# This is the histogram pattern, using 'get' to handle new words
    for word in words :
        counts[word] = counts.get(word, 0) + 1

## Identify the word that occurs the most in the file
bigCount = None
bigWord = None
for word,count in counts.items() :
    if bigCount is None or count > bigCount :
        bigCount = count
        bigWord = word

# Print the most frequent word and its count
print(bigCount, bigWord)
print(counts)
