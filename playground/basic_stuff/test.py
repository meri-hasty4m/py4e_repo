# Write a program that takes in user test scores prints average of scores.

'''
Author: Meri
Date: Dec. 6, 2023
Modified: N/A


'''

scores = list()

math = input('Math score: ')
scores.append(int(math))
english = input('English score: ')
scores.append(int(english))
science = input('Science score: ')
scores.append(int(science))

print(scores)

# replace the values with new values. Mupltiplying the scores by 2
# and printing out the list with the updated values 

for score in range(len(scores)) :
    scores[score] = scores[score] * 2
print(scores)
