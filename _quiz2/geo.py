def isGeometric(array):
     if len(array)==1:
        return True
     else:
        return array[1]/array[0]==array[-1]/array[-2]and isGeometric(array[1:])

print(isGeometric([1,2,4,8,16,32]))
print(isGeometric([1,4,9,27,81]))
