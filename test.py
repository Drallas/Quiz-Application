import unittest

import triviaapi
import asyncio

class TestInput(unittest.TestCase):
    def test_trivia(self):
        # Test get_random_questions to return a list of questions from 1, 1, easy
        # Asseert  that get_random_questions return a dictionary with the questions
        # Assert that the dictionary has the correct number of questions.
        type(asyncio.run(triviaapi.get_random_questions(1, 1, "easy"))) == dict
