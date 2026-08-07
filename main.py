from student import Student
from course import Course
from assessment import Quiz, Exam, Project
from gradebook import Gradebook

gradebook = Gradebook()

while True:

    print("===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Add Assessment")
    print("6. Record Grade")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice =="0":
        break

    elif choice =="1":
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_email = input("Enter student email: ")
        student = Student(student_id, student_name, student_email)
        result = gradebook.add_student(student)
        print(result)

    elif choice == "2":
        gradebook.view_students()

    elif choice == "3":

        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")

        course = Course(course_code, course_name)

        result = gradebook.add_course(course)

        print(result)

    elif choice == "4":
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")

        enroll_result = gradebook.enroll_student(student_id, course_code)

        print(enroll_result)



    elif choice == "5":

        course_code = input("Enter course code: ")

        print("1. Quiz")

        print("2. Exam")

        print("3. Project")

        assessment_type = input("Choose assessment type: ")

        title = input("Enter assessment title: ")

        max_score = float(input("Enter maximum score: "))

        if assessment_type == "1":
            assessment = Quiz(title, max_score)

        elif assessment_type == "2":
            assessment = Exam(title, max_score)

        elif assessment_type == "3":
            assessment = Project(title, max_score)

        else:
            print("Invalid assessment type")
            continue

        result = gradebook.add_assessment(course_code, assessment)
        print(result)


