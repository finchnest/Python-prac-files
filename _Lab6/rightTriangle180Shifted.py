def starPattern(row):
    k=2*row-2
    for x in range (1,row+1):
        
        for y in range(1,k+1):
            print(end=" ")
        k-=2
        for o in range (1,x+1):
            print("*", end=" ")
        print() 
print(starPattern(5))
      
                
