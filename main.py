# Quiz Application
import asyncio

# Imports module triviaapi.py
from triviaapi import get_random_questions, question_category, question_difficulty


def collect_user_input():
    """
    Collect user input for the number of questions, category, and difficulty
    """

    # Ask the user for their name
    name: str = input("What is your name? ")

    # Ask the user to enter a number of questions
    number_of_questions = int(
        input("How many questions would you like to answer? "))

    # Ask the user to enter a category
    print("Categories:")
    for key, value in question_category.items():
        print(f"{key}: {value}")
    print("\n")
    category_nr = int(input("What category would you like to play?\n "))

    # Get the key from the dictionary
    category_key = list(question_category.keys())[list(
        question_category.values()).index(question_category[category_nr])]
    print(f"You are playing {question_category[category_nr]}")

    # Ask the user to enter a difficulty
    # Print the difficulties
    print("Difficulties:")
    for key, value in question_difficulty.items():
        print(f"{key}: {value}")
    print("\n")
    difficulty_nr = int(input("What difficulty would you like to play?\n"))

    difficulty = question_difficulty[difficulty_nr]

    return name, number_of_questions, category_key, difficulty


if __name__ == "__main__":
    result: tuple = collect_user_input()
    asyncio.run(get_random_questions(
        result[1], result[2], result[3]))

# Store a random selection of questions in a list

# Start a loop and ask the user to answer each question

# Keep track of the number of correct answers
