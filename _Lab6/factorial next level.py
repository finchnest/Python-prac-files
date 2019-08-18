def factor(n):
    if n==1:
        return 1
    return n*factor(n-1)

def users(x,y,z):
    return factor(x),factor(y),factor(z)
print(users(4,5,6))



