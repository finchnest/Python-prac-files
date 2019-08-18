def deciToBinar(dec):
    if dec>1:
        deciToBinar(dec//2)
    print(dec%2,end="")
print(deciToBinar(10))
