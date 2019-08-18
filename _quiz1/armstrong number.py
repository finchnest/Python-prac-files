for z in range(0,1000):
    if len(str(z))==3:
        n1=z%10
        n2=(z//10)%10
        n3=z//100
        if (n1**3+n2**3+n3**3)==z:
            print(z," is an armstrong number!")
            
