# Camera Taylor 20234012
# Programming Techniques ITT103 - Course Registration and Payment System
# Jonathan Johnson - F2024
# Submission date: December 15, 2024.

# Course Registration System:

# Course Class
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

# Student Class
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0

    def enroll (self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.fee
        else:
            print("Student Exists! Enroll New Student.")

    def get_total_fee (self):
        return self.balance

# RegistrationSystem Class
class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}

    def add_course (self, course_id, name, fee):
        for course in self.courses:
            if course.course_id == course_id:
                print("Course Exists! Add New Course.")
                return
        self.courses.append(Course(course_id, name, fee))
        print("Course Added!")

    def register_student (self, student_id, name, email):
        for student in self.students.values():
            if student.student_id == student_id or student.email == email:
                print("Student Exists! Register New Student.")
                return
        self.students[student_id] = Student(student_id, name, email)
        print("Student Registered!")

    def enroll_in_course (self, student_id, course_id):
        if student_id not in self.students:
            print("Student Does Not Exist.")
            return
        for course in self.courses:
            if course.course_id == course_id:
                if course in self.students[student_id].courses:
                    print("Student Exists! Enroll New Student.")
                    return
                self.students[student_id].enroll(course)
                print("Student Enrolled!")
                return
        print("Course Does Not Exist.")

    def calculate_payment (self, student_id, amount):
        if student_id not in self.students:
            print("Student Does Not Exist.")
            return
        student = self.students[student_id]
        if amount < 0.4 * student.balance:
            print("Unsuccessful! Payment Amount Must be at Least 40%.")
            return
        student.balance -= amount
        print("Successful Payment. Balance: ", student.balance)

    def check_student_balance (self, student_id):
        if student_id not in self.students:
            print("Student Does Not Exist.")
            return
        student = self.students[student_id]
        return student.balance

    def show_courses (self):
        if not self.courses:
            print("Course Does Not Exist.")
            return[]
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.name}, Fee: {course.fee}")
        return [(course.course_id, course.name, course.fee)]

    def show_registered_students (self):
        if not self.students:
            print("No Students Registered!")
            return[]
        return [(student_id, student.name, student.email) for student_id, student in self.students.items()]

    def show_students_in_course (self, course_id):
        course_students = []
        for student_id, student in self.students.items():
            for course in student.courses:
                if course.course_id == course_id:
                    course_students.append((student.student_id, student.name))
                    break
        if not course_students:
            print("No Students Enrolled!")
        else:
            for student in course_students:
                print(f"Student ID: {student[0]}, Student Name: {student[1]}")
        return course_students

# RegistrationSystem Menu Options:
def main():
    system = RegistrationSystem()
    while True:
        print("Welcome! Menu Options: ")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll in Course")
        print("4. Calculate Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in Course")
        print("9. Exit")
        option = int(input("Select an Option (1-9): "))

# Add Course:
        if option == 1:
            print("1. Add a Course")
            course_id = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            while True:
                try:
                    fee = float(input("Enter Course Fee: "))
                    break
                except:
                    print("Numbers Only for Course Fee.")
            system.add_course(course_id, name, fee)
# Register Student:
        elif option == 2:
            print("2. Register a Student")
            while True:
                try:
                    student_id = int(input("Enter Student ID: "))
                    break
                except:
                    print("Numbers Only for Student ID.")
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            system.register_student(student_id, name, email)
# Enroll in Course
        elif option == 3:
            print("3. Enroll Students in Course")
            while True:
                try:
                    student_id = int(input("Enter Student ID: "))
                    break
                except:
                    print("Numbers Only for Student ID.")
            course_id = input("Enter Course ID: ")
            system.enroll_in_course(student_id, course_id)
# Calculate Payment
        elif option == 4:
            print("4. Calculate Student Payment")
            while True:
                try:
                    student_id = int(input("Enter Student ID: "))
                    break
                except:
                    print("Numbers Only for Student ID.")
            while True:
                try:
                    amount = float(input("Enter Amount: "))
                    break
                except:
                    print("Numbers Only for Amount.")
            system.calculate_payment(student_id, amount)
# Check Student Balance:
        elif option == 5:
            print("5. Check Student Balance")
            while True:
                try:
                    student_id = int(input("Enter Student ID: "))
                    break
                except:
                    print("Numbers Only for Student ID.")
            balance = system.check_student_balance(student_id)
            if balance is not None:
                print(f"Current Balance: {balance}")
# Show Courses:
        elif option == 6:
            print("6. Show Available Courses")
            system.show_courses()
# Show Registered Students:
        elif option == 7:
            print("7. Show Registered Students")
            students = system.show_registered_students()
            for student in students:
                student_id, name, email = student
                print(f"Student ID: {student_id}, Student Name: {name}, Email: {email}")
# Show Students in Course:
        elif option == 8:
            print("8. Show Students in Course")
            course_id = input("Enter Course ID: ")
            system.show_students_in_course(course_id)
# Exit
        elif option == 9:
            print("9. Exit. Goodbye!")
            exit()
# Incorrect Option Selected:
        else:
            print("Invalid Menu Option! Select Again.")

if __name__ == "__main__":
    main()



# "I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT". C.TAYLOR







