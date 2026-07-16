class Student:
    def __init__(self, student_id, full_name,email):
        self.student_id = student_id
        self.name = full_name
        self.email = email
        self.courses = []

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def set_email(self, email):
        if "@" in email:
            self.email = email
            return True

        else:
            return("Invalid email")


    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
        else:
            return "Course already enrolled"
            return True

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Courses:", self.courses)
