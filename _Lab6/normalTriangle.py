def starPattern(row):
    k=row
    for x in range (1,row+1):
        
        for y in range(1,k):
            print(end=" ")
        k-=1
        for y in range (1,x+1):
            print("*", end=" ")
        print() 
print(starPattern(5))
      
                
'''
                *
              *   *
            *   *   *
          *   *   *   *
        *   *   *   *   *
'''
