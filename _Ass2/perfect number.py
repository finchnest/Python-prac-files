num=int(input("Enter a number\n"))
divisor=1
total=0
while divisor<num:
    if num%divisor==0:
        total=total+divisor
    divisor+=1
if num==total:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
    
