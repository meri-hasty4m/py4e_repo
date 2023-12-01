word = 'bs'

def check_word (word_to_check) :
    try:
        word_to_check = word_to_check.lower()
        if word_to_check < word :
            print('greater')
        elif word_to_check == word :
            print('same')
        else :
            print('less')
    except ValueError as e:
        print("you didn't enter a valid value ")



check_word("Bs")
