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



    def add_course(self, course):

        if course.course_code in self.courses:
            return "Course already exists"

        else:
            self.courses[course.course_code] = course
            return f"Course with code {course.course_code} and name {course.course_name} is added successfully."



    def enroll_student(self, student_id, course_code):

        if student_id not in self.students:
            return "Student does not exist"

        student = self.students[student_id]


        if course_code not in self.courses:
            return "Course code does not exist"

        course = self.courses[course_code]


        student.enroll_course(course_code)
        course.add_student(student_id)


        return "Student enrolled successfully"



    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:
            return "Course does not exist"

        course = self.courses[course_code]

        course.add_assessment(assessment)

        return "Assessment added successfully"