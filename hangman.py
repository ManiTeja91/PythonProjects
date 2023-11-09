from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word = word.upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    #get user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print("You have", lives, "lives left to use", "\nYou have used these letters"," ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current Word", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
            
        elif user_letter in used_letters:
            print("You have used the letter !, Please try again")
        else:
            print("Invalid character")
    if lives == 0:
        print("You died!, sorry the word was", word)
    else:
        print("Congrats!!, You guessed the word", word)

hangman()



