

class A:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        m3 = A(m1, m2)
        return m3


a1 = A(76, 56)
a2 = A(88, 67)

a3 = a1+a2

print(a3.m1)