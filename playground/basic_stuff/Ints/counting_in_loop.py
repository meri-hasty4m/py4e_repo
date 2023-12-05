"""
Looping thru set, getting index and counting total items in set

Author: Meri
Date: Nov. 21, 2023
Modified: N/A
"""

myList = [9, 41, 12, 3, 74, 15]
count = 0

print('Before-------')
for num in myList :
    if count == 3 :
        break
    count = count + 1
    print(count, num)
print('After-------')
print(myList.index(12))


"""
Finding average in the set

Author: Meri
Date: Nov. 21, 2023
Modified: N/A
"""


mySet = [ 4, 2, 34, 245, 54, 3]
sum = 0
count = 0

for num in mySet :
    count = count + 1
    sum = num + sum
average = sum / count
print(average)
