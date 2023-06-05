
class A:
    def Strategy1(self):
        print("simple one")
    def Strategy2(self):
        print("little bit work on this ")
class B:
    def Strategy3(self):
        print("hard one")
    def Strategy4(self):
        print("this is not that much easy ")

class C(A,B):
    def Strategy5(self):
        print("Focus On the Subject")
a1=A()
b1=B()
c1=C()

a1.Strategy1()
a1.Strategy2()
b1.Strategy3()
b1.Strategy4()
c1.Strategy5()
c1.Strategy4()
print("======================================================")


class A:
    def Strategy1(self):
        print("simple one")
    def Strategy2(self):
        print("little bit work on this ")
class B(A):
    def Strategy3(self):
        print("hard one")
    def Strategy4(self):
        print("this is not that much easy ")

class C(B):
    def Strategy5(self):
        print("Focus On the Subject")
a1=A()
b1=B()
c1=C()


c1.Strategy1()
c1.Strategy2()
c1.Strategy3()
c1.Strategy4()
c1.Strategy5()