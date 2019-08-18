def hold(money):
        if money%10<5:
                print(money%10," ones")
        elif money%10==5:
                print("1 fives")
        else:
                print((money%10)%5," ones")
                print("1 fives")
        if ((money//10)%10)<5:
                print((money//10)%10," tens")
        elif ((money//10)%10)==5:
                print("1 fifties")
        else:
                print(((money//10)%10)%5," tens")
                print("1 fifties")
        print(money//100," hundreds")
print(hold(1796)) 

