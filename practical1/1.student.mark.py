# Student Mark Management System

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (DoB): ")
            self.students.append(Student(student_id, name, dob))

    def input_number_of_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks_for_course(self):
        self.list_courses()
        course_id = input("Select a course by entering the course ID: ")
        selected_course = next((course for course in self.courses if course.course_id == course_id), None)
        if not selected_course:
            print("Course not found!")
            return
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            student.marks[course_id] = mark
        print("Marks have been entered successfully!")

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks_for_course(self):
        self.list_courses()
        course_id = input("Enter the course ID to display marks: ")
        selected_course = next((course for course in self.courses if course.course_id == course_id), None)
        if not selected_course:
            print("Course not found!")
            return
        print(f"\nMarks for Course: {selected_course.name}")
        for student in self.students:
            mark = student.marks.get(course_id, "Not entered")
            print(f"Student: {student.name} (ID: {student.student_id}), Mark: {mark}")

def main():
    system = StudentMarkManagement()
    while True:
        print("\n--- Student Mark Management System ---")
        print("1. Input number of students and student information")
        print("2. Input number of courses and course information")
        print("3. Input marks for students in a course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show student marks for a given course")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            system.input_number_of_students()
        elif choice == '2':
            system.input_number_of_courses()
        elif choice == '3':
            system.input_marks_for_course()
        elif choice == '4':
            system.list_courses()
        elif choice == '5':
            system.list_students()
        elif choice == '6':
            system.show_student_marks_for_course()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
