num=int(input("how many fibonacci numbers want u see "))
def uptoWhat(N):
    for x in range(1,N+1):
        def fibon(x):
            if x<=1:
                return 1
            return fibon(x-1)+ fibon(x-2)

        print(fibon(x))
print(uptoWhat(num))  
