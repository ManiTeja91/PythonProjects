import random

def play():
    
    user = input("Enter your choice, 'r' for Rock, 'p' for Paper, 's' for Scissors :\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It's a Tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"
    

#r>s,s>p,p>r

def is_win(player, opponent):
    #r>s,s>p,p>r
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
       or (player == 'p' and opponent == 'r'):
           return True
           
           
print(play())