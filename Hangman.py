import random

wordlist = ['PYTHON','JAVA','C','C#','C++','SWIFT','JAVASCRIPT','HTML','XML','CSS','REACT','ANGULAR','PYTORCH','TENSORFLOW','RUBY']

Score = 0
HighScore = 0

while True:
    word = random.choice(wordlist)
    idx1 = random.randrange(0,len(word))
    idx2 = random.randrange(0,len(word))
    Lives = int(len(word)+2)
    if idx1 == idx2:
        continue
    else:
        displaytxt1 = word.replace(word[idx1],'_')
        displaytxt2 = displaytxt1.replace(displaytxt1[idx2],'_')
        print(displaytxt2)
        break

while True:
    inp = input('Complete the Given Word:')
    inp = inp.upper()
    if Lives == 0:
        print('Game Over!!')
        print('Score',Score)
        print('High Score:',HighScore)
        Score = 0
        break

    if inp == word:
        print("Yes!! +1")
        Score+=1
        if Score > HighScore:
            HighScore = Score
            while True:
                word = random.choice(wordlist)
                idx1 = random.randrange(0,len(word))
                idx2 = random.randrange(0,len(word))

                if idx1 == idx2:
                    continue
                else:
                    displaytxt1 = word.replace(word[idx1],'_')
                    displaytxt2 = displaytxt1.replace(displaytxt1[idx2],'_')
                    print(displaytxt2)
                    break
    else:
        Lives-=1
        print("You only have",Lives,'lives Remaining!!')
            

