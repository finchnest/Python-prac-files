def gcd(n1,n2):
    div2=[]
    for d in range(1,n1+1):
        for e in range(1,n2+1):
            if n1%d==0 and n2%e==0 and d==e:
                div2.append(d)
    return max(div2)
print(gcd(17,51))
            
