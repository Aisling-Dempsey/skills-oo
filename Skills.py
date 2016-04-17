class Student(object):
    """template to create students"""

    def __init__(self, first_name, last_name, address):
        self.name = first_name
        self.surname = last_name
        self.home = address

class Question(object):
    """Class for storing question/answer pairs"""

    def __init__(self, question, answer):
        self.question  = question
        self.question_answer = {}
        self.question_answer[question] = answer

    def ask(self):
        """prompts the user to answer question and returns True or False"""
        answer = raw_input(self.question + " ")
        if answer == self.question_answer[self.question]:
            return True



class Exam(object):
    """Template for making exams"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        """adds quesions to the list of questions for the exam"""
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def administer(self):
        """loops through all quetions in the exam and returns."""
        score = 0
        for question in self.questions:
            scoring = question.ask()
            if scoring == True:
                score += 1
        return score


def take_test(test, student):
    """administers the exam named as an argument and assigns the score to the student"""
    student.score = test.administer()

def example():
    final = Exam('final')
    final.add_question('Do you like SF?', 'Yes')
    final.add_question('2 + 2', '4')
    final.add_question('3 - 2', '1')
    final.add_question('What state do you live in?', 'California')
    balloonicorn = Student('Balloonicorn', 'Jones', 'Hackbrizzle')
    take_test(final, balloonicorn)

class Quiz(Exam):
    def administer(self):
        """loops through all questions in the exam and returns True if the quiz taker got 50% or more right"""
        score = 0
        for question in self.questions:
            scoring = question.ask()
            if scoring == True:
                score += 1
        total = float(score)/len(self.questions)
        print total
        if total >= .5:
            return True
        else:
            return False



#DEBUG CODE
# final = Quiz('final')
# final.add_question('Do you like SF?', 'Yes')
# final.add_question('2 + 2', '4')
# final.add_question('3 - 2', '1')
# final.add_question('What state do you live in?', 'California')
# print final.administer()

