def IsPalindrome(text):
    lowerText=text.lower()
    if len(text)<=1:
        return True
    else:
        return lowerText[0]==lowerText[-1] and IsPalindrome(text[1:-1])

print(IsPalindrome("kk"))
        
