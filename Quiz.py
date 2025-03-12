import easygui
score = 0
MIN_AGE = 14
MAX_AGE = 19

questions  = [
  ""
]

easygui.msgbox("Welcome to the NZ Trivia Game")
name = easygui.enterbox("What is your name?")
easygui.msgbox("Welcome to the NZ Trivia Game" + name)
age = easygui.integerbox("How old are you?")
if age < MIN_AGE:
  easygui.msgbox("You are too young to play!")
if age > MAX_AGE:
  easygui.msgbox("You are too old to play!")
else:
  easygui.msgbox("You are the right age to play!")
  easygui.msgbox("You will be asked a series of multiple choice questions. If you get a question correct, you will gain 1 point. If you get a question wrong, you will get one more chance to select the correct answer. If you fail this second chance, you will lose a point. You will have a total of 10 questions.")
