import random

Score = 0
Lives = 5
HighScore = 0

while(True):
    s = int(random.randrange(0,100))
    n = int(input("Guess the Number:"))
    if Lives == 0:
        print("You have no lives left! ")
        print("Score:",Score)
        print("High Score:",HighScore)
        break
        
    if n == s:
        print("'That's Correct!!")
        print("+1")
        q = input("Do you want to Continue?:")
        if Score > HighScore:
            HighScore = Score
            print("Congratulations!! You Beated your HighScore")
        if q == "No" or q =="no":
            break
            print("Score:",Score)
            print("High Score:",HighScore)
    elif n > s:
        print("This Number is Greater !")
        print("One Life Deducted")
        Lives -=1
        q = input("Do you want to Continue?:")
        if q == "No" or q =="no":
            break
            print("Score:",Score)
            print("High Score:",HighScore)
    else:
        print("This Number is Smaller !!")
        print("One Life Deducted")
        Lives -=1
        q = input("Do you want to Continue?:")
        if q == "No" or q =="no":
            break
            print("Score:",Score)
            print("High Score:",HighScore)


