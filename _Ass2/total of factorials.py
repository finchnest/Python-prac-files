num=eval(input("Enter a number "))
total=0
for x in range(1,num+1):
    factor=1
    while x>0:
        factor=factor*x
        x-=1
    total=total+factor
print(total)

    
