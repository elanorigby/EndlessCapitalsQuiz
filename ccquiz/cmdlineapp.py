from sys import exit

from ccquiz.logic import Quiz


def intro():
    kind = input("What kind of quiz u want? Capitals, Countries, or Random? \n Q to quit, h for a hint (the answer)").lower().strip()

    if kind not in 'capitals countries random q':
        raise ValueError("not a valid quiz type")

    def structure():
        quiz = Quiz(kind)

        debug = False

        if debug:
            print('ans: ' + quiz.ans)
            # print('  hint: ' + quiz.hint, end=' ')
            # print('  kind: ' + quiz.kind, end='\n')

        if quiz.kind == 'q':
            exit()

        if quiz.kind == 'capitals':
            question = "What is the capital of {}?"

        if quiz.kind == 'countries':
            question = "{} is the capital of what country?"

        def loop():
            guess = input(question.format(quiz.hint)).lower().strip()

            if guess == 'q':
                exit()

            if guess == 'h':
                print(quiz.ans)
                loop()

            if quiz.is_correct(guess):
                print("Yes")
                structure()
            else:
                print("Try again")
                loop()

        loop()

    structure()

intro()
