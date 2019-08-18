num=1
num2=1
starCount=10
while starCount>0:
    for b in range (1,num+1):
        print(b, end=" ")
    num+=1
    for x in range (1,starCount):
        print("*", end=" ")
    starCount-=2
    for w in range (1,num2+1):
        print(num2-w+1,end=' ')
    num2+=1
    print()
    
    
       
