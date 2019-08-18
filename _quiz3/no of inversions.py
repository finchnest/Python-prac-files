def inversion(string):
    splited=[]
    for q in string:
        splited.append(q)
    n=0
    inver=0
    for splited[n] in splited:
        looper=1

        while looper<(len(splited)-n):
            
            if ord(splited[n])> ord(splited[n+looper]):
                inver+=1
            looper+=1
        n+=1
    return inver
    
print(inversion("ABBFHDCGc"))
