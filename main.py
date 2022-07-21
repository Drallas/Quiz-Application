"""
Real Python : Quiz Application
"""

import asyncio

# Imports module triviaapi.py
from triviaapi import (get_random_questions, question_category,
                       question_difficulty)


def display_trivia_lists(trivia_lists):
    """ Display the trivia lists """
    print("\n".join(f"{key}: {value}" for key, value in trivia_lists.items()))


def validate_input(arg_input, list_input):
    """
    Validates user input.
    """
    if arg_input in range(len(list_input)):
        print("Valid input")
    else:
        print("Invalid input")
        raise SystemExit(1)


def collect_user_input():
    # TO DO: # Draft function needs to be refactored.
    """
    Collects user input and returns a dictionary with Trivia Questions.
    """
    player1: str = input("What is your name? : ")
    number_of_questions = int(
        input("How many questions would you like to answer? : "))

    print("\nPick a Category:")
    display_trivia_lists(question_category)
    category_nr = int(input("What category would you like to play? : "))
    validate_input(category_nr, question_category)
    # Get the key from the dictionary
    category_key = list(question_category.keys())[list(
        question_category.values()).index(question_category[category_nr])]
    print(f"You are playing {question_category[category_nr]} \n")

    print("Pick a Difficulty:")
    display_trivia_lists(question_difficulty)
    difficulty = question_difficulty[int(
        input("What difficulty would you like to play? : "))]
    print(f"You are playing {difficulty} \n")

    return player1, number_of_questions, category_key, difficulty


if __name__ == "__main__":
    user_input: tuple = collect_user_input()

    # Get the questions from the API
    trivia_questions = asyncio.run(get_random_questions(
        user_input[1], user_input[2], user_input[3]))

    print(f"Questions : {trivia_questions}")


# TO DO: Build the Quiz Application with data from the API.

# Show the user the questions, 1 at a time.
# Ask the user to answer each question.
# Keep track of the number of questions answered correctly.
# Keep track of the number of questions answered incorrectly.
# When the user has answered all the questions,
# show the number of questions answered correctly and incorrectly.
# When the user has answered all the questions, ask the user if they want to play again.
