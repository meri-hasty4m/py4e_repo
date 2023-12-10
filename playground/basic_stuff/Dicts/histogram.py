
llamo = {}
list_of_names = ['Sally', 'Suzie', 'Samantha', 'Shawn', 'Sheldon', 'Sheldon', "Suzie", "Shane"]

for name in list_of_names :
    if name not in llamo :
        llamo[name] = 1
    else :
        llamo[name] = llamo[name] + 1

print(llamo["Sally"])
