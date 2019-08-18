def starPattern(row):
    y=0
    while row>0:
        for v in range(1,y+1):
            print(end=" ")
        y+=1
        for x in range (1,row+1):
            print("*", end=" ")
        print()
        row=row-1
print(starPattern(5))     
                

'''
        * * * * *
         * * * *
          * * *   
           * *
            *
'''

        
        
