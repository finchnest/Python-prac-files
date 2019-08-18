def frequ(num,f):
    counter=0
    while num!=0:
        if (num%10==f):
            counter+=1
        num=num//10
    return counter

print(frequ(95299052,9))
        
