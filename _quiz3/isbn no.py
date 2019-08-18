def isbn(num):
    
    lis=[]
    for x in str(num):
        lis.append(int(x))
    counter=10
    n=0
    total=0
    while counter>1:
        total+=counter*lis[n]
        counter-=1
        n+=1
    for g in range(0,10):
        if (total+g)%11==0:
            return g,str(num)+str(g)
print(isbn("020131452"))
