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

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            return "Student does not exist"

        student = self.students[student_id]

        if course_code not in self.courses:
            return "Course does not exist"

        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)

        if assessment is None:
            return "No assessment"

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score
        return "Grade recorded successfully"


    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades:
            return "Student does not exist"

        if course_code not in self.grades[student_id]:
            return "Course does not exist"

        course_grades = self.grades[student_id][course_code]

        total = 0

        for score in course_grades.values():
            total += score

        average = total / len(course_grades)
        return average


    def get_result(self, average):
        if average >= 55:
            return "Passed"
        else:
            return "Failed"


    def show_report(self, student_id):
        if student_id not in self.students:
            return "Student does not exist"
        student = self.students[student_id]


        print("===== Student Report =====")
        print(f"student ID:{student_id} \n Name:{student.name}, \n Email: {student.email} \n Courses: {student.courses}")


        student_grades = self.grades[student_id]

        for  course_code in student_grades:
            course_grade = student_grades[course_code]


        for assessment in course_grade:
            score = course_grade[assessment]

            print(f"{assessment}: {score}")

        average = self.calculate_average(student_id, course_code)
        print(f"Average: {average}")

        result = self.get_result(average)
        print(f"Result: {result}")

