counter=1
while counter<=26:
    def decrypt(text,key):
        lowerText=text.lower()
        newer=''
        for x in lowerText:
            if x.isalpha() is True:
                newer+=chr(((ord(x)-97)+key)%26+97)
            else:
                newer+=x
        return newer
    print(decrypt("wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj",counter))
    counter+=1
#the key is 23
   
