class Question:
    ''' This class is used to create question objects. 
        It has three attributes: text, answer and explanation. 
        The text attribute: is a string that holds the question text.
        The answer attribute: is a string that holds the correct answer.
        The explanation attribute: is a string that holds the explanation of the answer.
        '''

    def __init__(self, q_text, q_answer, q_explanation):
        self.text = q_text
        self.answer = q_answer
        self.explanation = q_explanation
