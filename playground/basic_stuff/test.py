"""
Looping thru string and printing each letter in given word


"""


my_string = 'Facts'

def loop_string(str) :
    i = 0
    for letter in str :
         letter = str[i]
         i = i + 1
         print(i, letter)


loop_string(my_string)
