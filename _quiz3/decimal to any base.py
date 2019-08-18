base=int(input("Enter base "))
def decToAny(deci):
    if deci>1:
        decToAny(deci//base)
    print(deci%base,end='')

    
