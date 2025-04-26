
class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    

n = int(input())
studentList = []
for _ in range(n):
    name , roll , marks = input().split()
    marks = int(marks)
    roll = int(roll)
    studentList.append(Student(name,roll,marks))
    

for i in range(n-1,-1,-1):
    print(studentList[i].name,studentList[i].roll,studentList[i].marks)