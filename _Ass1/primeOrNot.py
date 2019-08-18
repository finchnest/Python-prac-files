num=int(input("Enter a number\n"))
factors=0
d=1
while d<=num:
    if num%d==0:
        factors=factors+1
    d+=1
if factors==2:
    print("It is a prime number")
else:
    print("It is not a prime number")
    
