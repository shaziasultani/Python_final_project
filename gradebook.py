class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}


    def add_student(self, student):

        if student.student_id in self.students:
            return "This student already exists"
        else:
            self.students[student.student_id] = student
            return "Student added successfully"

