def GCD(m,n):
    if m%n==0:
        return n
    else:
        return GCD(n,m%n)
print(GCD(12,18))
