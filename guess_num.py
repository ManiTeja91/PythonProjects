import random

#user guesses the number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess  a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry Guess again, Too low")
        elif guess > random_number:
            print("Sorry Guess again, Too high")
            
    print(f"Yay, Congrats! You have guessed the number correctly {random_number}")

      
#guess(10)

#computer guesses the number
def computer_guess(x):
    low = 1
    high = x
    feedback = '' #gives feedback to computer whether the guess is too high or too low
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)").lower()
        if feedback == 'h':
            high = guess - 1
            #makes the guess-1 as the new high
        elif feedback == 'l':
            low  = guess + 1
            #makes the guess+1 as the new low
    
    print(f"Computer has guessed your number {guess} correctly!")
        
#computer_guess(10)