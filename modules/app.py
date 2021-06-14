from student import Student
from utils import return_average

inp = ''
students = []
while inp != 'q':
    inp = input("Write your command: ")
    if inp == 'a':
        name = input("First name: ")
        lastname = input("Last name: ")
        average = float(input("Average: "))
        students.append(Student(name, lastname, average))
    if inp == 'r':
        print("Average is: ", return_average(students))
    if inp == 'l':
        for l in students:
            print("{}, {}, {}".format(l.name, l.lastname, l.average))