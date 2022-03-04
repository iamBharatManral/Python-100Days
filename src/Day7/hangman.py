from word_list import word_list
from hangman_art import hangman_stages

import random
import datetime

random.seed(datetime.datetime.now().microsecond)
word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)


def print_header():
    print("\n\t+====================================+")
    print("\tWelcome to a game of life: The Hangman")
    print("\t+====================================+\n")
    print("You have to guess all the characters of a word before the man gets hanged!")
    print(
        f"\nTo save the man, you have to guess {word_length} characters word.")
    print("And you have 6 lives to do that\n")


def modify_string(str, guess):
    return str[0:word_to_guess.index(guess)] + guess + str[word_to_guess.index(guess)+1:]


def print_str(str):
    for ch in str:
        print(f"\t{ch}", end="")
    print("\n")


def create_str(length):
    return "_" * length


def print_hangman(life):
    print(hangman_stages[life-1])


def game_over(result):
    if result == 'won':
        print("\nGAME OVER! You just saved a precious human life. 😌")
    else:
        print("\nGAME OVER! You couldn't save this man. So sorry! 😞")


def start_game():
    chances = 6
    str = create_str(word_length)
    life_used = 0
    right_guessed_chars = 0
    print_header()
    print_str(str)
    while life_used != chances and right_guessed_chars != word_length:
        user_guess = input("\nPlease guess the letter: ")
        if user_guess in word_to_guess:
            right_guessed_chars += 1
            str = modify_string(str, user_guess)
            print("\nYour guess is correct!")
            print_str(str)
        else:
            life_used += 1
            print(f"\nYour guess is not correct! You have lost {life_used} life/lives!")
            print_hangman(life_used)
            print_str(str)
    if life_used == chances:
        game_over("lost")
    else:
        game_over("won")


start_game()
