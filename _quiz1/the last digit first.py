def endUp(num):
    stringed=str(num)
    newNum=""
    newNum+=str(num)[-1]
    for x in range(0,len(str(num))-1):
        newNum+=str(num)[x]
    return int(newNum)

print(endUp(21036))#62103
