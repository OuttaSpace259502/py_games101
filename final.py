#!/usr/bin/env python3
"""
Code in Place 2021
Final Project: Memory Training Program
The program helps the user train memory and memorize items. 
It can be used for vocabulars, random numbers, words, mix etc. or personalized inputs (i.e. to learn for exams)
It creates helpful Madlibs for the user with those items to increase memorization.
Madlibs will help user to visualize and create a story with those items thus helping them keeping it long-term.
"""

import random, sys, time


def word_list():
    word_list = [
        "graphic processing unit",
        "central processing unit",
        "algorithm",
        "Massachusetts",
        "python",
        "software engineer",
        "eloquent",
        "monotheism",
        "nirvana",
        "memory",
        "default",
        "motivation",
        "courage",
        "drive",
        "express",
        "social media",
        "concentration",
        "animal lover",
        "ruthless",
        "maniac",
        "hemisphere",
        "horizon",
        "artificial intelligence",
        "inferior",
        "success",
        "happiness",
        "protection",
        "wild life",
        "podcast",
        "manipulation",
        "storyline",
        "whole foods",
        "persistence",
        "strength",
        "challenge",
        "blockchain",
        "future",
        "loyalty",
        "cravings",
        "healthy lifestyle",
    ]
    return word_list


def main():
    greeting()
    options()
    interval()


def greeting():
    print("Welcome to the Memory Training Program!")
    print("We will help you memorize everything you need.\nLet's get started!")


# User chooses between computer generated material and personal input
def options():
    print(
        "Would you like to enter learning materials yourself or would you like the computer to generate items for you?"
    )
    automated_or_input = input("Enter computer or personal: ").lower().strip()
    if automated_or_input == "computer":
        computer_option()
    if automated_or_input == "personal":
        personal_option()


# User can choose between 2 diff. input styles. Default works the same way as pc generated words() only with words chosen by user
# Vocab will be flashcards style. Ideal for learning new vocabulars or for question => answer style
def personal_option():
    choice = input("Choose between default and vocab: ").lower().strip()
    if choice == "default":
        default()
    if choice == "vocab":
        vocab()


# User chooses between 3 different computer generated options
def computer_option():
    pick_option = input("Choose between numbers, words or mixed: ").lower().strip()
    if pick_option == "numbers":
        numbers()
    elif pick_option == "words":
        words()
    elif pick_option == "mixed":
        mixed()


# This option only exists for computer generated option.
# Depending on the difficulty level more or less words/numbers will be shown.
def difficulty_level():
    print(
        "Choose a difficulty level. Depending on the difficulty level more or less words/numbers will be shown."
    )
    difficulty = input("Enter easy, moderate, advanced or pro: ").strip().lower()
    if difficulty == "easy":
        level = random.randint(6, 11)
    if difficulty == "moderate":
        level = random.randint(10, 16)
    if difficulty == "advanced":
        level = random.randint(17, 26)
    if difficulty == "pro":
        level = random.randint(27, 40)
    return level


# User chooses the pace every time a new word/number will appear on the screen
def interval():
    print("In what pace would you like every item to appear on screen?")
    interval_option = input("Enter fast, medium or slow: ").lower().strip()
    if interval_option == "fast":
        sleep = time.sleep(3)
    elif interval_option == "medium":
        sleep = time.sleep(6)
    elif interval_option == "slow":
        sleep = time.sleep(10)
    return sleep


# Generates a random list of numbers for user to memorize
def numbers():
    random_numbers = []
    for num in range(
        difficulty_level()
    ):  # Length of list is determined by difficulty level
        number_generator = random.randint(1, 101)
        random_numbers.append(number_generator)
    print(random_numbers)
    return random_numbers


# Generates a random list of words for user to memorize
def words():
    random_words = []
    for num in range(difficulty_level()):
        add_word = random.choice(word_list())
        random_words.append(add_word)
    print(random_words)
    return random_words


# Generates a random mixed list of numbers and words for user to memorize
def mixed():
    random_mixed = []
    list_of_words = (
        word_list()
    )  # Creates new word_list to not alter original since it is needed for word() as well
    list_of_words += list(
        range(50, 101)
    )  # Appends numbers to list_of_words list to randomly generated mixed list of both numbers and list_of_words
    for num in range(difficulty_level()):
        add_mixed = random.choice(list_of_words)
        random_mixed.append(add_mixed)
    print(random_mixed)
    return random_mixed


# Creates a list of words or numbers based on user input for user to memorize.
def default():
    users_list = []
    print(
        "Please enter your words one by one followed by 'enter'.\nWhen finished press 'enter' instead of new word to complete your list."
    )
    while True:
        user_input = input("Enter your word: ").strip().lower()
        if user_input == "":
            break
        else:
            users_list.append(user_input)
    print(users_list)
    return users_list


# Creates flashcards (dicionary style) based on user input for user to study. Functionality is described in print.
def vocab():
    vocabs = {}
    print(
        "Please enter your keyword followed by 'enter.\nNext enter your definition/answer followed by 'enter' when finished. Separate multiple definition values with a comma.\nLeave keyword blank and press 'enter' to complete your flashcards."
    )
    while True:
        keyword = input("Enter your keyword: ").lower().strip()
        if keyword == "":
            break
        value = input("Enter your definition to keyword: ").lower().strip()
        if "," in value:
            value.split(",")  # For multiple values
        vocabs[keyword] = [value]
    print(vocabs)
    return vocabs


if __name__ == "__main__":
    main()
