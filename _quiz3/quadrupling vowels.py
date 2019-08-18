def hell(string):
   
    newer=''
    for x in string:
       if x in "aeiou":
            newer+=x*4
       else:
            newer+=x
    return newer+"!"
print(hell("hello"))


