def find_word(sentence,word):
    splited=sentence.split()
    for w in splited:
        if w==word:
            return splited.index(w)
    return -1
def test():
    print(find_word("sees paramount green in the red", "paramount"))
test()
    
