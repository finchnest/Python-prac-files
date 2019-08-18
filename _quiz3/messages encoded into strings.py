def hidden(array):
    dic={"a" : 1 ,"b" : 2 ,"c" : 3 ,"d" : 4 ,"e": 5 ,"f": 6 ,"g" : 7 ,"h" : 8 ,"i" : 9 ,"j" : 10 ,"k" : 11 ,"l" : 12 ,"m" : 13 ,"n" : 14 ,"o" : 15 ,"p" : 16 ,"q" : 17 ,"r" : 18 ,"s" : 19 ,"t" : 20 ,"u" : 21 ,"v" : 22 ,"w" : 23 ,"x" : 24 ,"y" : 25 ,"z" : 26}
    
    for x in array:##for such expressions use enhanced for loop in java
        total=0##if its like "for x in range(y)", use the normal for loop in java
        for r in x:
            for y in dic.keys():
                if r== y :
                    total+=dic[y]

        if total>26:
            total=total//26
        for o,s in dic.items():
            if total==s:
                print(o,end='')
    return ''
print(hidden(["abcb", "bab", "deab", "adbe", "abcde", "abcdecb", "edcbaf", "ba", 
"agaaa", "ad", "fff"]))


