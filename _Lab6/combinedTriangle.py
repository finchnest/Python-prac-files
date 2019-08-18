def starPattern(row):
    k=row
    for x in range (1,row+1):
        
        for y in range(1,k):
            print(end=" ")
        k-=1
        for y in range (1,x+1):
            print("*", end=" ")
        print()
    y=1
    while row>0:
        for y in range(1,y+1):
            print(end=" ")
        y+=1
        for x in range (1,row):
            print("*", end=" ")
        print()
        row=row-1
print(starPattern(30))
input()

