import random

actions = ['ROCK','PAPER','SCISSOR']

while True:
    turn = random.choice(actions)
    n = input("Enter the action:")
    n = n.upper()

    # If Input is Rock

    if n == 'ROCK' and turn == 'PAPER':
        print('You Lose')
        print('---------------------------------')
        
    elif n == 'ROCK' and turn == 'SCISSOR':
        print('You Win')
        print('---------------------------------')
        
    elif n == 'ROCK' and turn == 'ROCK':
        print('Draw')
        print('---------------------------------')
        
    
    #If Input is Paper

    if n == 'PAPER' and turn == 'SCISSOR':
        print('You Lose')
        print('---------------------------------')
        
        elif a == 'YES':
            continue
            
    elif n == 'PAPER' and turn == 'ROCK':
        print('You Win')
        print('---------------------------------')
        
        elif a == 'YES':
            continue
    elif n == 'PAPER' and turn == 'PAPER':
        print('Draw')
        print('---------------------------------')
        
        elif a == 'YES':
            continue 

    #If input is Scissor

    elif n == 'SCISSOR' and turn == 'ROCK':
        print('You Lose')
        print('---------------------------------')
        
    elif n == 'SCISSOR' and turn == 'PAPER':
        print('You Win')
        print('---------------------------------')
        

    else:
        print('Draw')
        print('---------------------------------')

    a = input('Do You Want to Continue?:')
        if a == 'NO':
            break