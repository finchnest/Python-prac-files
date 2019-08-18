def starPattern(row):
    while row>0:
        for x in range (1,row+1):
            print("*", end=" ")
        print()
        row=row-1
print(starPattern(5))        




 
