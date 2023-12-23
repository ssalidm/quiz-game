class QuizBrain:
    '''This class is responsible for keeping track of the score and questions
    and checking if the user got the answer right.    
    '''

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.num_of_questions = len(self.question_list)

    def still_has_questions(self):
        '''Returns True if there are still questions left to ask, False otherwise.
        returns: bool
        '''
        return self.question_number < self.num_of_questions
    
    
    def next_question(self):
        '''Asks the next question in the question_list. 
        returns: None
        '''
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ")
        print('-'*90)
        correct_answer = current_question.answer
        explanation = current_question.explanation
        self.check_answer(user_answer, correct_answer, explanation)
        

    def check_answer(self, user_answer, correct_answer, explanation):
        '''Checks if the user got the answer right.
        user_answer: str
        correct_answer: str
        explanation: str
        returns: None
        '''
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print(f"✅ You got it right! The correct answer was: {correct_answer}.")
        else:
            print(f"❌ That's wrong. The correct answer was: {correct_answer}.")
        if explanation:
            print(f"💡 {explanation}")
        print(f"🎯 Your current score is: {self.score}/{self.question_number}\n")


    def get_result(self):
        '''Prints the final score.
        returns: None
        '''
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}")




        