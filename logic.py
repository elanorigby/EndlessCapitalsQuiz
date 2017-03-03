from sys import exit
from random import choice
from data import list_of_tups


class Data:

    def __init__(self):
        self.TUPS = list_of_tups

    def __len__(self):
        return len(self.TUPS)

    def grow_pair(self):
        """ Pick a random capital and country pair from TUPS """
        return choice(self.TUPS)

    def capitals(self):
        """ Assign the country to hint and the capital to correct_answer """
        hint, correct_answer = self.grow_pair()
        return correct_answer, hint

    def countries(self):
        """ Assign the country to correct_answer and the capital to hint """
        correct_answer, hint = self.grow_pair()
        return correct_answer, hint


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


class GuessLoop:

    def __init__(self, debug=False):
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


class CapitalsQuiz(GuessLoop):

    def __init__(self):
        super(CapitalsQuiz, self).__init__()
        self.data = Data()
        self.correct_answer, self.hint = self.data.capitals()
        self.printout = PrintOut(capital=self.correct_answer, country=self.hint)
        self.question = self.printout.capitals_q()


class CountriesQuiz(GuessLoop):

    def __init__(self):
        super(CountriesQuiz, self).__init__()
        self.data = Data()
        self.correct_answer, self.hint = self.data.countries()
        self.printout = PrintOut(capital=self.hint, country=self.correct_answer)
        self.question = self.printout.countries_q()


class Quiz:

    @staticmethod
    def quit():
        print("Ta ta for now!")
        exit()

    def get_kind(self):
        kind = input('Type 1 for capitals, 2 for countries, or Q to quit\n> ').strip().lower()
        if kind == 'q':
            self.quit()
        elif kind == '1':
            return CapitalsQuiz
        elif kind == '2':
            return CountriesQuiz
        else:
            print("Sorry, didn't catch that.")
            self.get_kind()

    def quiz_loop(self):
        PrintOut.welcome()
        quiz_kind = self.get_kind()
        while True:
            quiz = quiz_kind()
            quiz.guess_loop()


if __name__ == '__main__':
    test = Quiz()
    test.quiz_loop()
