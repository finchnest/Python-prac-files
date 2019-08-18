def starPattern(row):
    k=0
    for x in range (1,row+1):
        
        for y in range(1,k+1):
            print(end=" ")
        k+=2
        for y in range (1,row+1):
            print("*", end=" ")
        print()
        row=row-1
print(starPattern(5))


