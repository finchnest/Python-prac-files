num=eval(input("Enter the number of terms u want to compute "))
e=1
for x in range(1,num):
    factor=1
    while x>0:
        factor=factor*x
        x-=1
    e=e+(1/factor)
print("Mathematical constant e = ",e)

    
