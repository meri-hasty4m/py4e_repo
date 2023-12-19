'''
Write a program that reads the words in a .txt file and stores them
as keys in a dictionary. It doesn't matter what the vales are. Then you
can use the 'in' operator as a fast way to check wheter a string is in
the dictinary

'''
fhand = open('../Chapter_8/romeo.txt')
counts = dict()

for lines in fhand :
    words = lines.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1


target_word = input('What word are you looking for? ')

if target_word in counts :
    print(True)
else : print(False)
