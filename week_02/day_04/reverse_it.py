
# time and space complexity ---- > O(n)
class Student:
    def __init__(self,name,clas,section,stu_id):
        self.name = name
        self.cls = clas
        self.section = section
        self.id = stu_id



n = int(input())
studentList = []
for _ in range(n):
    name, clas, section, stu_id = input().split()
    
    clas = int(clas)
    stu_id = int(stu_id)
    studentList.append(Student(name,clas,section,stu_id))

i = 0
j = len(studentList)-1

while i<j:
    temp = studentList[i].section
    studentList[i].section = studentList[j].section
    studentList[j].section = temp
    i+=1
    j-=1

for student in studentList:
    print(student.name,student.cls,student.section,student.id)