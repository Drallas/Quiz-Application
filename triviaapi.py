"""
Provides some arithmetic functions
"""

import logging

from trivia import trivia

logging.basicConfig(level=logging.INFO)
# Logging levels are DEBUG, INFO, WARNING, ERROR, CRITICAL
# Info: about logging https://realpython.com/python-logging/

# Response format
# [{
# 'category': 'Entertainment: Music',
# 'type': 'multiple',
# 'difficulty': 'hard',
# 'question': 'Which band is the longest active band
#  in the world with no breaks or line-up changes?',
# 'correct_answer': 'U2',
# 'incorrect_answers': ['Radiohead', 'Rush', 'Rolling Stones']
# },

# {'category': 'Entertainment: Music', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which of the following is NOT a real song from the band Thousand Foot Krutch?', 'correct_answer': 'Limitless Fury', 'incorrect_answers': ['Let The Sparks Fly', 'Down', 'Give Up The Ghost']},
# ]


question_category: dict = {
    0: "All Categories",
    1: "General Knowledge",
    2: "Entertainment: Books",
    3: "Entertainment: Film",
    4: "Entertainment: Music"
}

question_difficulty: dict = {
    0: "Any Difficulty",
    1: "Easy",
    2: "Medium",
    3: "Hard"
}


async def get_random_questions(
        questions_count: int,
        category_key: int,
        difficulty_value: str) -> dict:
    """
    Get a list of random questions from the Trivia API
    """

    logging.info("Getting random questions:")
    logging.info(f"Nr of Questions {questions_count}")
    logging.info(f"Catergory {category_key}")
    logging.info(f"Difficulty {difficulty_value}\n")

    # Return a string with difficulty, but a zero for any difficulty.
    def difficulty(): return difficulty_value.lower(
    ) if difficulty_value.lower() in ["easy", "medium", "hard"] else 0

    logging.info(f"Difficulty: {difficulty()}")

    questions = await trivia.question(
        amount=questions_count,
        category=category_key,
        difficulty=difficulty(),
        quizType='multiple'
    )

    logging.info(questions)
    return questions
