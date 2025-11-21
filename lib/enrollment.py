from datetime import datetime
class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()
    def course_count(self):
        return len(self._enrollments)
    
    def course_count(self):
        return len(self._enrollments)

class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
    

python = Course("Python Programming")
js = Course("JavaScript Programming")

student1= Student("Alice")
student2= Student("Bob")

student1.enroll(python)
student1.enroll(js)
student2.enroll(js) 
print(f"{student1.name} is enrolled in {student1.course_count()} courses.")
print(f"{student2.name} is enrolled in {student2.course_count()} courses.")