

class Student:
    college="Suresh University"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getcollege(cls):
        return cls.college

    @staticmethod
    def info():
        print("Student's Results in Average marks")


print(Student.getcollege())

print(Student.info())
s1=Student(85,65,95)
print("S1: ", s1.avg())
print()
s2=Student(75,65,45)
print("S2: ", s2.avg())