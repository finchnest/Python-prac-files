import random
Moves=["w","s","a","d"]

        #n by n matrix 
size=int(input("Enter the size of the game u wanna play "))
def matrixGenerator(size):
    matri=[]
    for y in range(size): #the elements in this loop are basically acting as place holders to 
        matri.append([0]*size)    #the elements in the nxt for loop...so the "0" doesnt have to be zero for that  
    #for x in range(size):
      #  matrix[x]=[0]*size          #adds a list within the list
    return matri
matrix=matrixGenerator(size)
starters=[2,2,2,2,4]    #we did this to favor 2 four times, in other words 80% more chance
matrix[random.choice(range(0,size))][random.choice(range(0,size))]=random.choice(starters)    #the game starts with two number(2 or 4) located at a random index  
matrix[random.choice(range(0,size))][random.choice(range(0,size))]=random.choice(starters)          #within the matrix 

#transpose for n by n matrix
def transpose(mati):
    """ this function takes a matrix and returns the transposed one"""
    mat=[]
    for y in range(0,len(mati)): 
        mat.append(0)    
    for x in range(0,len(mati)):      #the first 2 for loop are simply generating a matrix of size n of elements 0
        mat[x]=[0]*len(mati)
    for i in range(0,len(mati)):
        for j in range(0,len(mati)):
            if i==j:
                mat[i][j]=mati[i][j]       #this second loop takes advantage of the first 2 loops and simply applies
            else:                             #the property of matrix transpose
                mat[i][j]=mati[j][i]
    return mat   

#column swapper
def swapper(matrixx):
    for row in matrixx:
        i=0
        while i< (len(row)/2):              #the loop is gonna run  only half times the lenght of the row cause by that time all columns are swapped
            row[i],row[len(row)-1-i]=row[len(row)-1-i],row[i]
            i+=1
    return matrixx

#leftAdder for an n by n matrix
def leftAdder(matrixo):
    mat2=[]
    for row in matrixo:
        size=len(row)
        merged=[]
        for x in row:
            if x!=0:
                merged.append(x)
        p=0
        while p < (len(merged)-1):
            if merged[p]==merged[p+1]:
                merged[p]*=2
                del merged[p+1]
            p+=1
        while len(merged)<size:
            merged.append(0)
        mat2.append(merged)
    return mat2
def info():
    '''
the above function checks if a number is zero or not and then adds it to the list if
it ia not 0. Now if the resulting list has same successive elements, it adds them up
and puts the result in the lower index. When that loop is done it replaces all zeros
to the list until the length of the original list is achieved
'''
    pass
def checker(matri, user_dxn):
    '''
here we are defining all movements interms of left movement, transpose, and swaps
'''
    if user_dxn == "a":
        matr = leftAdder(matri)
    elif user_dxn == "d":
        matr = swapper(leftAdder(swapper(matri)))
    elif user_dxn == "w":                                         
        matr = transpose(leftAdder(transpose(matri)))
    elif user_dxn == "s":
        matr = transpose(swapper(leftAdder(swapper(transpose(matri))))) #the down movement is equivalent to the T of the matrix followed by the S of the resulting matrix
    return matr                                                           #follwed by leftAdder operation then swapping that result and finally transposing the result.

while True:
    for row in matrix:
        for columnValue in row:                 #this for loop prints the transformed matrix
            print(columnValue,end="    ")
        print()
    while True:
        user_dxn = str(input("Enter Direction: ")).lower()
        if user_dxn in Moves:
            break
        print("Invalid Movement")

    matrix=checker(matrix,user_dxn)     

    row_indexes_with_zero=[]    #these lists are resetted to zero in every loop(movement)
    column_indexes_with_zero=[]
    ctr = 0                                #the counter is incremented every time we find an index with 0
    for i in range(0,size):
        for j in range(0,size):
            if matrix[i][j]==0:
                ctr+=1                
                row_indexes_with_zero.append(i)
                column_indexes_with_zero.append(j)
            if matrix[i][j]==16:
                print("You Win")
                break
    if matrix[i][j]==16:
        break
    if ctr > 1:
        RandomIndex = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))  # its gonna choose a num from row_indexes_with_zero and then the index of that num
        matrix[row_indexes_with_zero[RandomIndex]][column_indexes_with_zero[RandomIndex]]=random.choice(starters) #in row_indexes_with_zero is stored
    elif ctr==1:
        matrix[row_indexes_with_zero[0]][column_indexes_with_zero[0]]=random.choice(starters)            #2 or 4 is randomly placed at a random index
    else:
        print ("Game over")
        break
    
