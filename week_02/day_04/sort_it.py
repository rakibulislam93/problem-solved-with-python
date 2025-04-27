
class Student:
    def __init__(self,name,cls,section,stu_id,math_marks,eng_marks):
        self.name = name
        self.cls = cls
        self.section = section
        self.id = stu_id
        self.math_marks = math_marks
        self.eng_marks = eng_marks


n = int(input())
studentList = []
for _ in range(n):
    name, cls,section,stu_id,math_marks,eng_marks = input().split()
    cls,stu_id,math_marks,eng_marks = map(int,[cls,stu_id,math_marks,eng_marks])
    
    studentList.append(Student(name,cls,section,stu_id,math_marks,eng_marks))
    

studentList.sort(key=lambda student:(-(student.math_marks + student.eng_marks),student.id))

for student in studentList:
    print(student.name,student.cls,student.section,student.id,student.math_marks,student.eng_marks)