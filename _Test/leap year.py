print("Wanna check if some year is a leap year or not!")
def leapyear(year):
    if year%400==0:
        print("It's a leap year")
    elif year%400!=0:
        if year%100==0:
            print("It is not a leap year")
        elif year%4==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")

        
    
    
