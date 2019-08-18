def ramanujanNums(N,numsRange):
    for w in range(numsRange):
        for x in range(numsRange):
            for y in range(numsRange):
                for z in range(numsRange):
                    if w*w*w+x*x*x==y*y*y+z*z*z:
                        if w==x or w==y or w==z or x==y or x==z or y==z:
                            continue
                        else:

                            if(w*w*w+x*x*x)<=N:
                                print("The ramanujan numbers upto ",N," are/is ", w*w*w+x*x*x)
                                print("The first pairs are: ",w," and ",x," and the second pairs are: ",y," and ",z)
                            
                               
                                
print(ramanujanNums(5000,30))
        
