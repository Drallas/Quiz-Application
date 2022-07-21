from trivia import trivia


categories: dict = {
    0: "All Categories",
    1: "General Knowledge",
    2: "Entertainment: Books",
    3: "Entertainment: Film",
    4: "Entertainment: Music"
}

difficulties: dict = {
    0: "Any Difficulty",
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

# Get Random Quiz questions via the Trivia API
async def get_random_questions(
    questions_count: int,
    category_key: int,
    difficulty_value: str) -> dict:
    """
    Get a list of random questions from the Trivia API
    """

    # print the parameters
    print(f"questions {questions_count}")
    print(f"Catergory {category_key}")
    print(f"Difficulty {difficulty_value}")

    questions = await trivia.question(
        amount=questions_count,
        category=category_key,
        difficulty=difficulty_value.lower(),
        quizType='multiple'
    )
    
    print(questions)
