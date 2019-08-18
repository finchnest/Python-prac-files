mydic={}
for x in range(100):
    factors=0
    d=1
    while d<=x:
        if x%d==0:
            factors=factors+1
        d+=1
    mydic[x]=factors
for k,v in mydic.items():
    if v==max(mydic.values()):
        print(k," has ",v," factors")

   
    
