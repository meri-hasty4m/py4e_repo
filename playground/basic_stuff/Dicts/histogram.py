
llamo = {}
list_of_names = ['Sally', 'Suzie', 'Samantha', 'Shawn', 'Sheldon', 'Sheldon', "Suzie", "Shane"]

'''
for name in list_of_names :
    if name not in llamo :
        llamo[name] = 1
    else :
        llamo[name] = llamo[name] + 1

'''
### The .get() is how you check to see if there is something
### and if not defaul the value to 0
for name in list_of_names :
    llamo[name] = llamo.get(name, 0) + 1
print(llamo)
