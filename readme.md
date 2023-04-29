# Quiz Application
This is a simple quiz application that asks True or False questions from a list of questions.

## Usage
The quiz questions are provided as a list of dictionaries, where each dictionary contains a question and its corresponding answer. The questions are then converted into `Question` objects and stored in a list. 

The `QuizBrain` class is used to manage the quiz. It takes in the list of `Question` objects as input and keeps track of the current question number and the user's score. The `still_has_questions()` method checks if there are any more questions left to ask, and the `next_question()` method displays the current question and prompts the user to enter their answer. The `check_answer()` method compares the user's answer with the correct answer and updates the user's score.

The quiz is run by creating an instance of the `QuizBrain` class with the list of `Question` objects, and calling the `next_question()` method until all questions have been asked. The user's final score is then displayed.

To use the quiz application, simply copy the code into your Python environment and run it.

## Example
An example set of quiz questions is provided in the code. To use your own set of questions, modify the `question_data` list at the beginning of the code.