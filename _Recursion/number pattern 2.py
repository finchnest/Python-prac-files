def summing(num):
    if num==0:
        return 0
    else:
        return num/(2*num+1)+summing(num-1)
print(summing(3))
'''
3/7+ 2/5+ 1/3+ 0
'''
