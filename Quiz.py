import easygui
score = 0
TITLE = "Maori Quiz"
MIN_AGE = 14
MAX_AGE = 19
q_num = 1

questions  = [
  "Which of these words means “under” in te reo?",
  "What is an English word for “pukapuka”?",
  "Which te reo word could mean either 'clock' or 'orange' in English?",
  "Which of the following means 'island' in te reo?",
  "Sometimes used to describe items such as 'whare', what does the word 'nui' mean?",
  "Which of these terms in te reo means 'Excellent'?"
  "Where is Te Wairere?",
  "Where would you commonly find a ‘manu’?"]

answers = [["a) runga, b) raro, c) roto, d) waho"], 
  [" a) book, b) table, c) clock, d) wall"] , 
  ["a) kikorangi, b) karaka, c) pango, d) whero"], 
  ["a) rohe, b) whenua, c) moutere, d) iwi"], 
  [" a) long, b) wide, c) small, d) big"], 
  [" a)kaha, b) manaaki, c) rawe, d) pai"], 
  [" a) Alexandra, b) Clyde, c) Bannockburn, d) Cromwell"], 
[" a) sky, b) pre-school, c) swimming pool, d) classroom"]]

correct_answers = [ 
"b",
"a",
"b",
"c", 
"d",
"c",
"d",
"a"]

easygui.msgbox("Welcome to the Maori Trivia Game!" , TITLE)
name = easygui.enterbox("What is your name?" )
easygui.msgbox(f"Welcome to the Maori Trivia Game {name}" , TITLE)
age = easygui.integerbox("How old are you?")
if age < MAX_AGE and age > MIN_AGE:
  easygui.msgbox("You are in the right age range to play.")
elif age > MAX_AGE:
  easygui.msgbox("You are too old to play.")
  quit()
elif age < MIN_AGE:
  easygui.msgbox("You are too young to play.")
  quit()
      
easygui.msgbox("You will be asked a series of multiple choice questions. If you get a question correct, you will gain 1 point. If you get a question wrong, you will get one more chance to select the correct answer. If you fail this second chance, you will lose a point. You will have a total of 10 questions.")

PLAYER_READY = easygui.buttonbox(f"Are you ready to begin, {name}?" , choices = ["Yes" , "No"])
if PLAYER_READY == "Yes":
  easygui.msgbox("Great, lets get started")
elif PLAYER_READY == "No":
  easygui.msgbox("Okay, come back later.")
  quit()
  

easygui.msgbox(f"Question {q_num}")
for i in range(len(questions)):
  answer = easygui.buttonbox(questions[i], choices = answers[i])

