
word = 'faneto'
length = len(word)
decramentor = 1
whole_word_reversed = []

while length > 0 :
    last = word[length - decramentor] #<-- gets last letter in string
    decramentor = decramentor + 1
    whole_word_reversed.append(last)
    print(last)
    if decramentor == length +1 :
        break
print(''.join(whole_word_reversed))
print(word[0:100])
