def ramanujanNums(N,numsRange):
    ramlist=[]
    numslist=[]
    for w in range(numsRange):
        for x in range(numsRange):
            for y in range(numsRange):
                for z in range(numsRange):
                    if w*w*w+x*x*x==y*y*y+z*z*z:
                        if w==x or w==y or w==z or x==y or x==z or y==z:
                            continue
                        else:

                            if(w*w*w+x*x*x)<=N:
                                if (w*w*w+x*x*x) in ramlist:
                                    continue
                                else:
                                    ramlist.append(w*w*w+x*x*x)
                                if (w,x,y,z) in numslist:
                                    continue
                                else:
                                    numslist.append(w)
                                    numslist.append(x)
                                    numslist.append(y)
                                    numslist.append(z)
    return ((ramlist),(numslist))
                                 
                                
print(ramanujanNums(5000,20))
        

