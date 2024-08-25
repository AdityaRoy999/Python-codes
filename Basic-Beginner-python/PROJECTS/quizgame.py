def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0  # Start from the first question
    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_ans(questions[key], guess)
        question_num += 1
    disp_score(questions, guesses, correct_guesses)


def check_ans(correct_ans, guess):
    if guess == correct_ans:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0


def disp_score(questions, guesses, correct_guesses):
    print("----------------")
    print("RESULTS")
    print("----------------")
    print("ANSWERS: ", end="")
    for key, value in questions.items():
        print(value, end=" ")
    print("\nYOUR GUESSES: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():
    response = input("Do You want to play again:? YES or No :").upper()
    if response == "YES":
        return True
    else:
        return False
    


questions = {
    "Who created Python?": "A",
    "What year was Python created?": "B",
    "Python is tributed to which comedy group?": "C",
    "Is the Earth round?": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()
while play_again():
    new_game()

print("Bye, Have a Nice Day")
