
class Student:
    # class level variables/atributes
    # name = 'rakib'
    def __init__(self,name,roll,section,math_marks,cls):
        # instance level variables/atributes
        self.name = name
        self.roll = roll
        self.section = section
        self.math_marks = math_marks
        self.cls = cls


s1 = Student('rakib',10,'A',80,'seven') # create an object for Student class
s2 = Student('sakib',10,'A',90,'seven')
s3 = Student('akib',10,'A',50,'seven')

if s1.math_marks > s2.math_marks and s1.math_marks>s3.math_marks:
    print(s1.name)
elif s2.math_marks>s1.math_marks and s2.math_marks>s3.math_marks:
    print(s2.name)
else:
    print(s3.name)