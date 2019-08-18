num=int(input("Enter a number"))
prime=0
counter=1
while prime <= num:
    factors=0
    d=1
    while d<=counter:
        if counter%d==0:
            factors=factors+1
        d+=1
    if factors==2:
        print(counter)
        prime+=1
    counter+=1
