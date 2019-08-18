def series(num):
    if num==0:
        return 0
    else:
        return 1/num+series(num-1)
print(series(3))

'''
1+ 1/2+ 1/3+ 1/4
'''
