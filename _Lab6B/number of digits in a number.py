def digits(x):
    counter=0
    while x>0:
        x=x//10
        counter+=1
    return counter


print(digits(110730))

