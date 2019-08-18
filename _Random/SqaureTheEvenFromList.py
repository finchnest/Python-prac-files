num=input('Enter comma separated numbers\n')
num1=num.split(",")
num2=[]
for a in num1:
   a=int(a)
   num2.append(a)
square=[b*b for b in num2 if b%2==0]
print(square)
d=input()
