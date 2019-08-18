def wordCounter(text):
    
    mydict={}
    for word in text:
        if word in mydict:
            mydict[word]+=1
        else:
            mydict[word]=1
    return mydict
lyrics="believe it and it will make AND you ehiter than snow"
lyrics=lyrics.lower()
wordlist=[]
for x in lyrics.split():
    wordlist.append(x)
print(wordCounter(wordlist))


########################## most frequent
def mostCommon(freq):
    most=max(freq.values())
    words=[]
    for k in freq:
        if freq[k]==most:
            words.append(k)
    return (words,most)
print(mostCommon(wordCounter(wordlist)))
