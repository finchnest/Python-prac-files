#using dictionaries
wordlist=(input("Enter a sentence : ")).split()
dict1={'numbers':0,'SmallLetters':0,'CapitalLetters':0}
for i in wordlist:
    print(i)
    for j in i:
        if 57>=ord(j)>=48:
            dict1["numbers"]=+1
        elif 122>=ord(j)>=97:
            dict1['SmallLetters']+=1
        elif 90>=ord(j)>=65:
            dict1['CapitalLetters']+=1
for k,v in dict1.items():
    print(k,v)
###############################################
wordlist=(input("Enter a sentence : ")).split()
letters=0;numbers=0
for i in wordlist:
    print(i)
    for j in i:
        if 48<=ord(j)<=57:
            numbers+=1
        elif 97<=ord(j)<=122 or 65<=ord(j)<=90:
            letters+=1
print('letters: ',letters);print('numbers: ',numbers)





