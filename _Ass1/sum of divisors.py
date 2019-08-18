num=int(input("Enter a number\n"))
divisor=1
total=0
while divisor<=num:
    if num%divisor==0:
        total=total+divisor
    divisor+=1
print("The sum of the divisors is ", total)
    
