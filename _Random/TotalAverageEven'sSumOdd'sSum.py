number=input('Enter numbers you want to add up: ')
mynums=[]
while number!="stop":
    mynums.append(number)
    number=input('Add another one: ')

    
myupdate=[]
for i in mynums:
    i=int (i)
    myupdate.append(i)
print("\n\nThe numbers u entered are ", myupdate)
counter1=0                                       #the whole point of this block is to get rid of floating points because
total1=0                                                #soon we're gonna be working with even and odd numbers
for j in myupdate:
    total1+=j
    counter1+=1
print('The avarage is: ',total1/counter1)
print('The sum of the list is: ',total1)


evens=[]
for i in myupdate:
    if i%2==0:
        evens.append(i)
print("The evens are: ",evens)                   #operations on even numbers
total2=0
counter2=0
for j in evens:
    total2+=j
    counter2+=1
print('The avarage of the even numbers is: ',total2/counter2)
print('The sum of the even list is: ',total2)


odds=[]
for i in myupdate:
    if i%2!=0:
        odds.append(i)
print("The odds are: ",odds)                 #operation on odd numbers
total3=0
counter3=0
for j in odds:
    total3+=j
    counter3+=1
print('The avarage of the odds  is: ',total3/counter3)
print('The sum of the odds list is: ',total3)
c=input()















        
    
    
    
