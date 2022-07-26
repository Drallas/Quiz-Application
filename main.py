"""
Real Python : Quiz Application
"""

import asyncio

# Imports module triviaapi.py
from triviaapi import get_random_questions, question_category, question_difficulty


def display_trivia_lists(trivia_lists):
    """Display the trivia lists"""
    print("\n".join(f"{key}: {value}" for key, value in trivia_lists.items()))


def validate_input(arg_input, list_input):
    """
    Validates user input.
    """
    if arg_input in range(len(list_input)):
        return True
    print("Invalid input")
    raise SystemExit(1)


def collect_user_input():
    """
    WIP : Collects user input and returns a dictionary with Trivia Questions.
    """
    player1: str = input("What is your name? : ")
    number_of_questions = int(input("How many questions would you like to answer? : "))

    print("\nPick a Category:")
    display_trivia_lists(question_category)
    category_nr = int(input("What category would you like to play? : "))
    validate_input(category_nr, question_category)
    # Get the key from the dictionary
    category_key = list(question_category.keys())[
        list(question_category.values()).index(question_category[category_nr])
    ]
    print(f"You are playing {question_category[category_nr]} \n")

    print("Pick a Difficulty:")
    display_trivia_lists(question_difficulty)
    difficulty: int = int(input("What difficulty would you like to play? : "))
    validate_input(difficulty, question_difficulty)
    difficulty_string: str = question_difficulty[difficulty]
    print(f"You are playing {difficulty_string} \n")

    return player1, number_of_questions, category_key, difficulty_string


if __name__ == "__main__":
    user_input: tuple = collect_user_input()

    # Get the questions from the API
    trivia_questions = asyncio.run(
        get_random_questions(user_input[1], user_input[2], user_input[3])
    )

    enumerate_questions = enumerate(trivia_questions, start=1)

    for question_nr, question in enumerate_questions:
        print(f"Question {question_nr} : {question['question']}")
        print("\n")
        # Ask the user to answer each question.
        # call the function answer_question()

    print(list(enumerate_questions))
