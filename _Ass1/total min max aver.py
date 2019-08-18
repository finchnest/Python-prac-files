number=int(input("Enter the numbers  "))
total=0
counter=0
maxi=number
mini=number
while number!="x":
    if number > maxi:
        maxi=number
    elif number < mini:
        mini=number
    total+=int(number)
    counter+=1
    number=input("Continue Entering  ")
print("The avarage is ",total/counter)
print("The total sum is ",total)
print("The max of the numbers is ", maxi)
print("The min of the numbers  is ", mini)
