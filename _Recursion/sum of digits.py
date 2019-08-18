def summer(num):
    if num==0:
        return 0
    else: 
        return num%10+summer(num//10)
print(summer(2907))

################


num=int(input())
total=0
while num>0:
    total+=num%10
    num//=10
print(total)
