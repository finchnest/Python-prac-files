number=int(input("Enter a number\n"))
total=0
while number>0:
    total=total+number%10
    number=number//10
print("The sum of the digits in ur number is ", total)
