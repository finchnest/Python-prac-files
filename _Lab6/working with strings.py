num=str(input("Enter a three digit number such that the hundreds and one's digit difer by two\n"))
num0=int(num)
num2=(int(num[::-1]))
print("The reverse of ", num," is ",num2)
difer=abs(num0-num2)
print("The difference between ", num, " and", num2, " is ", difer)
num3=int(str(difer)[::-1])
print("The reverse of the difference is ", num3)
difer2=abs(num3+difer)
print("The sum of ",num3," and ",difer," is ",difer2 )

