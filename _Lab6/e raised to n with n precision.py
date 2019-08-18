def eComputer(terms,power):
    total=1
    for x in range(1,terms+1):
        factor=1
        numer=power**x
        while x>0:
            factor=factor*x
            x-=1
        total=total+(numer)/factor
    return total
print(eComputer(50,4))
    
