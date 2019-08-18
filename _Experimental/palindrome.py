def IsPalindrome(text):
    def firstPhase(text):
        lowerText=text.lower()
        pure=''
        for x in lowerText:
            if x in "abcdefghijklmnopqrstuvwxyz":
                pure+=x
        return pure
    def checker(text):
        if len(text)<1:
            return True
        else:
            return text[0]==text[-1] and checker(text[1:-1])
    return checker(firstPhase(text))
print(IsPalindrome("leveln"))
        
