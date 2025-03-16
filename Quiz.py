import easygui
score = 0
MIN_AGE = 14
MAX_AGE = 19
q_num = 1

questions  = [
  "Which of these words means “under” in te reo?"
  "What is an English word for “pukapuka”?"
  "Which te reo word could mean either 'clock' or 'orange' in English?"
  "Which of the following means 'island' in te reo?"
  "Sometimes used to describe items such as 'whare', what does the word 'nui' mean?"
  "Which of these terms in te reo means 'Excellent'?"
  "Where is Te Wairere?"
  "Where would you commonly find a ‘manu’?"
]

answers = [
  
]

easygui.msgbox("Welcome to the Maori Trivia Game!")
name = easygui.enterbox("What is your name?")
easygui.msgbox(f"Welcome to the Maori Trivia Game {name}")
age = easygui.integerbox("How old are you?")
if age < MAX_AGE and age > MIN_AGE:
  easygui.msgbox("You are in the right age range to play.")
elif age > MAX_AGE:
  easygui.msgbox("You are too old to play.")
  quit()
elif age < MIN_AGE:
  easygui.msgbox("You are too young to play.")
  quit()
easygui.msgbox("Great, lets get started")
      
easygui.msgbox("You will be asked a series of multiple choice questions. If you get a question correct, you will gain 1 point. If you get a question wrong, you will get one more chance to select the correct answer. If you fail this second chance, you will lose a point. You will have a total of 10 questions.")

easygui.msgbox(f"Question {q_num}")
