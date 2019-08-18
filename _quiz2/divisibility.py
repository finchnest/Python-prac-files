def times(num):
    counter=0
    while num>1:
        num//=2
        counter+=1
    return counter
print(times(80))
