from random import choice
from data import Data

class Quiz:
    def __init__(self, kind):
        if kind not in 'capitals countries random':
            raise ValueError("Not a valid quiz type")

        if kind == 'random':
            kind = choice(['capitals', 'countries'])

        self.kind = kind
        self.data = Data()
        self.ans, self.hint = self.data.gimmie(self.kind)

        if self.kind == 'capitals':
            self.question = "What is the capital of {}?".format(self.hint)

        if self.kind == 'countries':
            self.question = "{} is the capital of what country?".format(self.hint)


    def is_correct(self, guess):
        if guess == self.ans.lower():
            return True
        else:
            return False



