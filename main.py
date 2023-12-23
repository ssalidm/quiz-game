# 100 Days of Code - The Complete Python Pro Bootcamp for 2021
# Project 17/100 - Quiz Game
#
# Instructions:
# Create a quiz game using the data from the Open Trivia Database.
# The game should ask True/False questions from the data.
# The game should keep track of the user's score.
# The game should keep track of the user's progress.
# The game should give the user feedback on their answers.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print('-'*26)
print("Welcome to the Quiz Game!")
print('-'*26)

categories = ['Geography', 'Computer Science', 'Music', 'Sports']
cat_num = ['1', '2', '3', '4']
category = ''
while not category.isnumeric() or category not in cat_num:
    category = input("Pick a category number:\n1-Geography, 2-Computer Science, 3-Music, 4-Sports: ")
category = int(category)-1

print(f"\nYou picked {categories[category]}\n")

question_bank = [Question(question.get('question'), question.get('correct_answer'), question.get('explanation')) 
                 for question in question_data[category]]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
quiz.get_result()
print("Thanks for playing!\n")
