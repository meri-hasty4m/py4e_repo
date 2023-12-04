'''
Counting lines in a file

'''
count = 0
fhand = open('read_file.py')
for line in fhand :
    count = count + 1
print("Line count: ", count)


'''
Reading the whole file

'''

fhand = open('read_file.py')
inp = fhand.read()
print("Chars in file: ", len(inp))


'''
Searching through a read_file

'''

fhand = open("read_file.py")
for line in fhand :
    if line.startswith('count') :
        print("Line starts with, ", line)
