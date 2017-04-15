from random import choice
from data import Data


class Quiz:

    def __init__(self):
        self.data = Data()

    def is_right(self, user_answer):
        return user_answer == self.correct_answer.lower()


class CapitalsQuiz(Quiz):
    name = 'Capitals'

    def __init__(self):
        super(CapitalsQuiz, self).__init__()
        self.correct_answer, self.hint = self.data.capitals()


class CountriesQuiz(Quiz):
    name = 'Countries'

    def __init__(self):
        super(CountriesQuiz, self).__init__()
        self.correct_answer, self.hint = self.data.countries()


class RandomQuiz:

    def __init__(self, *choices):
        self.choices = choices

    def __len__(self):
        return len(self.choices)

    def choose(self):
        chosen = choice(self.choices)
        return chosen()

