import random

options = ['rock','paper','scissors']
comp = random.choice( options )
player = input("Enter your choice: ")

if player == comp:
    print("it is a tie")
else:
    if player == 'rock':
        if comp == 'paper':
            print("computer won, because it chose paper")
        else:
            print("player won because computer chose ",comp)

    elif player == 'paper':
        if comp == 'rock':
            print("player won because computer chose", comp)
        else:
            print("computer won, it chose scissors")

    elif player == 'scissors':
        if comp == 'rock':
            print("computer won, it chose rock")
        else:
            print("player won becouse computer chose", comp)
            
            
