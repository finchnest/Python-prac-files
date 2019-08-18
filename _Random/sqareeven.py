def squareEvens(listy):
    evenquare=[]
    for x in (listy.split(",")):
        x=int(x)
        if  x%2==0:
            evenquare.append(x**2)
    return evenquare
print(squareEvens("1,2,3,4"))

