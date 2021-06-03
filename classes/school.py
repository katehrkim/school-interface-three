import csv
import os.path
from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students, start=1):
            print(f'{i}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
            
    def rewrite_csv(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path, 'w') as csv_file:
            fieldnames = ['name','age','role','school_id','password']
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fieldnames)
            for student in self.students:
                csv_writer.writerow([student.name, student.age, student.role, student.school_id, student.password])

    def add_student(self, dictionary):
        person = Student(**dictionary)
        self.students.append(person)
        self.rewrite_csv()
            
    def delete_student(self, school_id):
        for student in self.students:
            if student.school_id == school_id:
                self.students.remove(student)
        self.rewrite_csv()



