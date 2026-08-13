class Course:
    def __init__(self, course_code, course_name, ):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def add_assessment(self, assessment):
        self.assessments.append(assessment)


    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
        else:
            return None

    def display_info(self):
        print(self.course_code)
        print(self.course_name)
        print(self.students)
        for assessment in self.assessments:
            assessment.display_info()


