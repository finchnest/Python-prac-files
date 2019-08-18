def wordCounter(lyrics):
    mydict={}
    for letter in lyrics:
        if letter in mydict:
            mydict[letter]+=1
        else:
            mydict[letter]=1
    return mydict
lyrics=" where we can go your soul, i know a place where mercy  than snow"

print(wordCounter(lyrics))
