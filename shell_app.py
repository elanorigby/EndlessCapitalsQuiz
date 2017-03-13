from sys import exit
from logic import CapitalsQuiz, CountriesQuiz, RandomQuiz


class Quit:

    @staticmethod
    def quit():
        print("Ta ta for now!")
        exit()


class Loop:

    def loop(self):
        user_answer = input('> ').strip().lower()
        if user_answer == 'q':
            Quit.quit()
        elif self.quiz.is_right(user_answer):
            print("Yes! {} is the capital of {}! \n".format(self.capital, self.country))
        else:
            print("Nope. Try again.")
            self.loop()

    def start(self, debug=False):
        print(self.question)
        if debug:
            print("psst it's {}".format(self.quiz.correct_answer))
        self.loop()


class Capitals(Loop):

    def __init__(self):
        super(Capitals, self).__init__()
        self.quiz = CapitalsQuiz()
        self.capital = self.quiz.correct_answer
        self.country = self.quiz.hint
        self.question = "What is the capital of {}?".format(self.country)


class Countries(Loop):

    def __init__(self):
        super(Countries, self).__init__()
        self.quiz = CountriesQuiz()
        self.capital = self.quiz.hint
        self.country = self.quiz.correct_answer
        self.question = "What country is {} the capital of?".format(self.capital)



def switchboard():
    quiz_kind = input("Welcome to the Endless Capitals Quiz! Type 1 for Capitals, 2 for Countries, 3 for random, and Q to quit.\n >").strip().lower()
    if quiz_kind == 'q':
        Quit.quit()
    elif quiz_kind == '1':
        return Capitals
    elif quiz_kind == '2':
        return Countries
    elif quiz_kind == '3':
        randomly = RandomQuiz(Capitals, Countries)
        return randomly.choose
    else:
        print("Sorry didn't catch that.")
        switchboard()

if __name__ == '__main__':
    kind = switchboard()
    while True:
        quiz = kind()
        quiz.start(debug=True)
