from sys import exit
from random import choice
from data import Data

class PrintOut:

    def __init__(self, capital='capital', country='country'):
        self.capital = capital
        self.country = country

    def capitals_q(self):
        return "What is the capital of {}\n> ".format(self.country)

    def countries_q(self):
        return "{} is the capital of what country?\n> ".format(self.capital)

    def congrats(self):
        print("Yes! {} is the capital of {}!".format(self.capital, self.country))

    @staticmethod
    def wrong():
        print("Sorry, that's not correct.")

    @staticmethod
    def welcome():
        print("Welcome to the Endless Countries and Capitals Quiz! Respond with Q anytime to quit.")


class Quiz:

    def __init__(self, debug=True):
        self.debug = debug

    def print_ans(self):
        print(" psst {} is the answer".format(self.correct_answer))

    def guess_loop(self):
        if self.debug:
            self.print_ans()
        user_answer = input(self.question).strip().lower()
        if user_answer == 'q':
            Quiz.quit()
        elif user_answer == self.correct_answer.lower():
            self.printout.congrats()
        else:
            self.printout.wrong()
            self.guess_loop()


class CapitalsQuiz(Quiz):

    def __init__(self):
        super(CapitalsQuiz, self).__init__()
        self.data = Data()
        self.correct_answer, self.hint = self.data.capitals()
        self.printout = PrintOut(capital=self.correct_answer, country=self.hint)
        self.question = self.printout.capitals_q()


class CountriesQuiz(Quiz):

    def __init__(self):
        super(CountriesQuiz, self).__init__()
        self.data = Data()
        self.correct_answer, self.hint = self.data.countries()
        self.printout = PrintOut(capital=self.hint, country=self.correct_answer)
        self.question = self.printout.countries_q()


class Randomly:

    def __init__(self):
        self.choices = (CapitalsQuiz, CountriesQuiz)

    def __len__(self):
        return len(self.choices)

    def choose(self):
        chosen = choice(self.choices)
        return chosen()


class Kind:

    @staticmethod
    def get_kind():
        return input('Type 1 for capitals, 2 for countries, 3 for random, or Q to quit\n> ').strip().lower()

    def __init__(self):
        self.kind = self.get_kind()

    def switchboard(self):
        if self.kind == 'q':
            Quit.quit()
        elif self.kind == '1':
            return CapitalsQuiz
        elif self.kind == '2':
            return CountriesQuiz
        elif self.kind == '3':
            randomly = Randomly()
            return randomly.choose
        else:
            print("Sorry, didn't catch that.")
            self.kind = self.get_kind()
            return self.switchboard()



class Quit:

    @staticmethod
    def quit():
        print("Ta ta for now!")
        exit()



if __name__ == '__main__':
    PrintOut.welcome()
    kind = Kind()
    quiz_kind = kind.switchboard()
    while True:
        quiz = quiz_kind()
        quiz.guess_loop()
