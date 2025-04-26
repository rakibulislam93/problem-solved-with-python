
class Student:
    
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    

n = int(input())
studentList = []
for _ in range(n):
    name, roll, marks = input().split()
    roll = int(roll)
    marks = int(marks)
    studentList.append(Student(name,roll,marks))

# sort student list theire maximum marks and roll 
studentList.sort(key=lambda student:(-student.marks,student.roll))

for student in studentList:
    print(student.name,student.roll,student.marks)

