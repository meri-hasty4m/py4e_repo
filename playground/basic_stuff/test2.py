word = 'bananas'

def check_word (word_to_check) :
    if word_to_check < word :
        print('greater')
    elif word_to_check == word :
        print('same')
    else :
        print('less')


check_word('Bananas')
