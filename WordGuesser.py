import random

wordlist = ['PYTHON','JAVA','C','C#','C++','SWIFT','JAVASCRIPT','HTML','XML','CSS','REACT','ANUGLAR','PYTORCH','TENSORFLOW','RUBY']
Score = 0
HighScore = 0
Lives = 5


while True:
    if Score > HighScore:
        HighScore = Score
    if Lives == 0:
        print('Game Over!!')
        print('Score:',Score)
        print('High Score',HighScore)
        break
        Score = 0
    word = random.choice(wordlist)
    n = input('Enter the Word ("Hint: Its Programming Language or Used in developing programs):')
    n = n.upper()
    if n == word:
        Score+=1
        print("YES +1")
        print("Score:",Score)
    else:
        Lives-=1
        print('You Have',Lives,' Lives Remaining!!')

    