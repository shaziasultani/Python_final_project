from student import Student
from course import Course
from assessment import Assessment
from gradebook import Gradebook

gradebook = Gradebook()

while True:
    print("===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice =="0":
        break

    if choice =="1":
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_email = input("Enter student email: ")
        student = Student(student_id, student_name, student_email)
        result = gradebook.add_student(student)
        print(result)