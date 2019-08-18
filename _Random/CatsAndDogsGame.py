print("Welcome to the cats and dogs game!")
x="1038"
y=str(input("Guess the 4 digit number: "))
cats=0
dogs=0
while cats<=4:
    cats=0
    dogs=0
    for i in x:
        for j in y:
            if i==j and x.index(i)==y.index(j):#for a variable we don't need to put the index value in "" like x.index("i")
                cats+=1
            elif i==j and x.index(i)!=y.index(j):
                dogs+=1
    if cats==4:
        print("you found the number")
        break       
    print('You have :',cats,"cats and",dogs,"dogs")
    y=input("Guess the 4 digit number: ")
    
        
