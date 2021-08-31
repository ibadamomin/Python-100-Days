class QuizBrain:
    def __init__(self, g_list):
        self.question_number = 0
        self.question_list = g_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q. {self.question_number}: {current_question.text} (True/False): ').lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("That's right!")
            self.score += 1
            print(f"Score: {self.score}/{self.question_number}")
            print('\n')
        else:
            print("Incorrect!")