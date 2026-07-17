class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage <= 60:
            return "Need improvement"
        elif percentage <= 85:
            return "Good"
        else:
            return "Great job"

    def display_info(self):
        print("Title:", self.title)
        print("Max Score:", self.max_score)



# quiz class, the assessment' parent class and here, using overriding too.

class Quiz(Assessment):


    def display_info(self):
        print("Quiz:", self.title)
        print("Max Score:", self.max_score)

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage > 85:
            return "Great result!"
        elif percentage > 60:
            return "Good."
        else:
            return "Needs more quiz practice."

# exam class
class Exam(Assessment):

    def display_info(self):
        print("Exam:", self.title)
        print("Max Score:", self.max_score)


    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "You passed the exam"

        else:
            return "You failed the exam"


class Project(Assessment):


    def display_info(self):
        print("Project:", self.title)
        print("Max Score:", self.max_score)


    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 85:
            return "Excellent project"
        elif percentage >= 60:
            return "Project submitted."
        else:
            return "Project needs improvement."



        