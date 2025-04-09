
"""This program has the user answer various trivia questions about Māori words and place names, tracking score and correcting the user if they get a question wrong more than once."""
import easygui
TITLE = "Māori Quiz"
MIN_AGE = 14
MAX_AGE = 19
# Defines the variables and constants for the quiz, the title of the quiz, and the minimum and maximum age for the quiz
questions = [
    "Which of these words means 'under' in te reo?",
    "What is an English word for 'pukapuka'?",
    "Which te reo word could mean either 'clock' or 'orange' in English?",
    "Which of the following means 'island' in te reo?",
    "Sometimes used to describe items such as 'whare', what does the word 'nui' mean?",
    "Which of these terms in te reo means 'Excellent'?",
    "Where is Te Wairere?",
    "Where would you commonly find a 'manu'?"]
# Defines the questions for the quiz, and organizes them into a list
answers = [
    ["a) runga", "b) raro", "c) roto", "d) waho"],
    ["a) book", "b) table", "c) clock", "d) wall"],
    ["a) kikorangi", "b) karaka", "c) pango", "d) whero"],
    ["a) rohe", "b) whenua", "c) moutere", "d) iwi"],
    [" a) long", "b) wide", "c) small", "d) big"],
    [" a)kaha", "b) manaaki", "c) rawe", "d) pai"],
    [" a) Alexandra", "b) Clyde", "c) Bannockburn", "d) Cromwell"],
    ["a) sky", "b) pre-school", "c) swimming pool", "d) classroom"]]
# Defines the answers for the questions, and organizes them into a list
correct_answers = [
    "b) raro",
    "a) book",
    "b) karaka",
    "c) moutere",
    "d) big",
    "c) rawe",
    "d) Cromwell",
    "a) sky"]
# Defines the correct answers for the questions, and organizes them into a list
easygui.msgbox("Welcome to the Māori Trivia Game!", TITLE)
name = easygui.enterbox("What is your name?", TITLE)
if name == "":
    easygui.msgbox("You must enter a name to play.", TITLE)
    quit()
elif name.isdigit():
    easygui.msgbox("You must enter a name to play.", TITLE)
    quit()
    # Checks if the user enters a integer value, the program will detect it and quit the quiz.
easygui.msgbox(f"Welcome to the Māori Trivia Game {name}. This quiz tests your understanding of Māori words", TITLE)
age = easygui.integerbox("How old are you? This quiz is only open to 15-18 year olds, so we have to verify whether you are in the right age range to play ", TITLE)

if age < MAX_AGE and age > MIN_AGE:
    easygui.msgbox("You are in the right age range to play.", TITLE)
elif age > MAX_AGE:
    easygui.msgbox("You are too old to play.", TITLE)
    quit()
elif age < MIN_AGE:
    easygui.msgbox("You are too young to play.", TITLE)
    quit()
elif age == "":
    easygui.msgbox("You must enter an age to play.", TITLE)
    quit()
# Welcomes the user to the quiz, asks the user for their name and age, and then checks if they are in the right age range to play. The code also checks if the user has entered a name or age, and if they have not, it will quit the quiz.
while True:
    easygui.msgbox("You will be asked a series of multiple choice questions. If you get a question correct, you will gain 1 point. If you get a question wrong, you will get one more chance to select the correct answer. If you fail this second chance, you will lose a point. You will have a total of 8 questions.", TITLE)
    # Informs the user of the rules of the quiz, and explains how they will be scored.
    player_ready = easygui.buttonbox(f"Are you ready to begin, {name}?", TITLE, choices=["Yes", "No"])
    if player_ready == "Yes":
        easygui.msgbox("Great, lets get started", TITLE)
    elif player_ready == "No":
        easygui.msgbox("Okay, come back later.", TITLE)
        quit()

    q_num = 1
    score = 0
    user_answers = []
    easygui.msgbox(f"Question {q_num}", TITLE)
    for i in range(len(questions)):
        user_answer = easygui.buttonbox(questions[i], TITLE, choices=answers[i])
        user_answers.append(user_answer)
        if user_answer == correct_answers[i]:
            score += 1
            easygui.msgbox(f"Correct! Your score is {score}", TITLE)
            q_num += 1
        else:
            easygui.msgbox("Incorrect. Have another go!", TITLE)
            user_answer = easygui.buttonbox(questions[i], TITLE, choices=answers[i])
            user_answers[i] = user_answer  # Updates the previous answer with the second attempt
            if user_answer == correct_answers[i]:
                score += 1
                easygui.msgbox(f"Correct! Your score is {score}", TITLE)
                q_num += 1
            else:
                score -= 1
                if score < 0:
                    score = 0
                easygui.msgbox(f"Incorrect. The correct answer was {correct_answers[i]}. You have lost 1 point. Your score is {score}", TITLE)
                q_num += 1
# Asks the user the questions, and checks if they got the question correct. If they do, it will add 1 to the user's score, and move on to the next question. If they get the question wrong, it will ask them the question again, and if they get it correct, it will add 1 to the user's score, and move on to the next question. If they get the question wrong again, it will tell them the correct answer, and move on to the next question. It will also keep track of the user's answers, and display them at the end of the quiz.
    easygui.msgbox(f"Congratulations, {name}! You have completed the quiz. Your final score is {score}.", TITLE)
    easygui.msgbox(f"Your answers were: {user_answers}", TITLE)
    # Tells the user their final score, and congratulates them for completing the quiz.
    play_again = easygui.buttonbox(f"Would you like to play again, {name}?", TITLE, choices=["Yes", "No"])
    if play_again == "No":
        easygui.msgbox(f"Goodbye, {name}.", TITLE)
        break
    # Asks the user if they would like to play again, and if they do, the quiz will restart. If they don't, the quiz will end.
