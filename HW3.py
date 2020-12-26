import random
import string
import time

words=["patates","kelime","ev","araba","kopek","gitar","ceket"]
name=input("Your name: ")
time.sleep(1)
print("Welcome to our Hangman Game ",name,"!")
time.sleep(2)
print("In our game, words will be given in Turkish.")
time.sleep(2)
input("Press Enter to continue...")

word = random.choice(words)
word = word.upper()
word_letters = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set()
lives = 8

while len(word_letters) > 0 and lives > 0:
    print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print("--------------------------")
        else:
            lives-=1
            print("--------------------------")
            print('Your letter,', user_letter, 'is not in the word.')
    elif user_letter in used_letters:
        print('\nYou have already used that letter. Guess another letter.')
    else:
        print('\nThat is not a valid letter.')

if lives == 0:
    print('You lost the game. The word was', word)
else:
    print('Congratulations! You guessed the word', word, '!')
