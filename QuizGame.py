# QUIZ GAME

print("Hey! Welcome to Quiz Game")
a = input("Are you Ready? ")
if a == "yes":
    b = input("Enter your name: ")
    starting_list = [3,2,1,'Lets Start!!']

    for item in starting_list:
        print(item)
print()
print("Categories:   1)PYTHON    2)GK    3)Programming")
category = input("Enter Category : ").lower()
if category == "python":
    def new_game():

        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("-------------------------")
            print(key)
            for i in options[question_num-1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1

        display_score(correct_guesses, guesses)

    # -------------------------
    def check_answer(answer, guess):

        if answer == guess:
            print("CORRECT!")
            return 1
        else:
            print("WRONG!")
            return 0

    # -------------------------
    def display_score(correct_guesses, guesses):
        print("-------------------------")
        print("RESULTS")
        print("-------------------------")

        print("Answers: ", end="")
        for i in questions:
            print(questions.get(i), end=" ")
        print()

        print("Guesses: ", end="")
        for i in guesses:
            print(i, end=" ")
        print()

        score = int((correct_guesses/len(questions))*100)
        print("Congratulations " + b +"! Your score is: "+str(score)+"%")
        print()

    # -------------------------
    def play_again():

        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            return True
        else:
            return False
    # -------------------------


    questions = {
     "Who created Python?: ": "A",
     "What year was Python created?: ": "B",
     "Python is tributed to which comedy group?: ": "C",
     "Is the Earth round?: ": "A"
    }

    options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
              ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
              ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
              ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

    new_game()

    while play_again():
        new_game()

    print("Byeeeeee!")
elif category == "gk":
    questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                       ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                       ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                       ("A. 206", "B. 207", "C. 208", "D. 209"),
                       ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    answers = ("C", "D", "A", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print("Congratulations " + b + f"! Your score is: {score}%")

elif category == "programming":
    questions = ("A program which translates a high-level language program into a machine language program is called?",
                       "A sequence of instructions in a computer language to get the desired result is known as: ",
                       "Which type of errors are flagged by Compilers ?",
                       "An algorithm is best described as : ",
                       "The language understood by a computer with out translation is called : ")

    options = (("A. Compiler", "B. Interpreter", "C. Both a & b", "D. none of these"),
                       ("A. an algorithm", "B. a decision table", "C. a program", "D. none of these"),
                       ("A. logical error", "B. syntax error", "C. both a & b", "D. none of these"),
                       ("A. A Computer language", "B. A step by step procedure for solving a problem", "C. A branch of mathematics", "D. None of these"),
                       ("A. Command language", "B. High-level language", "C. Assembly language", "D. Machine language"))

    answers = ("C", "C", "B", "B", "D")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print("Congratulations "+ b + "! Your score is: {score}%")