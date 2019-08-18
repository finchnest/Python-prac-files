import random
randomNum=random.randint(1,101)
guess=int(input("Guess a number in range of 100 "))
chance=1
while chance<=7:
    if guess==randomNum:
        print("You Win")
        break
    elif guess!=randomNum:
        if guess>randomNum:
            print("You guessed more than the random number, guess lower")
        else:
            print("You guessed lower than the random number, guess higher")
    
    chance +=1
    guess=int(input("Try again "))
if chance>7:
    print("GAME OVER")  

        
