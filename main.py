question_data = [
    {"text": "The human eye can distinguish 10 million different colors.", "answer": "True"},
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "All the kings in a standard deck of cards have a mustache.", "answer": "False"},
    {"text": "The name of Batman’s butler is Albert.", "answer": "False"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True"},
    {"text": "The Atlantic Ocean is the biggest ocean on Earth", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Greenland is the largest island in the world.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "Most of the human brain is made of muscle", "answer": "False"},
    {"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"}
]


# -------------------------------------------------------------------------------------------------------------#

class Question:
    def __init__(self, text, answer):
        self.txt = text
        self.ans = answer


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.txt})True/False \n")
        self.check_answer(user_answer, current_question.ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right !")
        else:
            print("That's wrong ")
        print(f"current score is {self.score}/{self.question_number}")
        print("\n")


# -------------------------------------------------------------------------------------------------------------#
question_bank = []

for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()

print("Quiz completed !")
print(f"final score is {Quiz.score}/{len(question_bank)}")