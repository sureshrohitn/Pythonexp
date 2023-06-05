class A:
    def laptop(self):
        print("most trusted Brand")
        print("dell is a Foreign Company")


class B:
    def laptop(self):
        print("Most Popular Brand")
        print("Hp is a Foreign Company")


class C:
    def laptop(self):
        print("Most User Friendly")
        print("Budget Friendly prices")


class Laptop:
    def laptop(self, refver):
        refver.laptop()


"""
class Laptop:
    def laptop(self, B):
        b1.Hp()

class Laptop:
    def laptop(self, A):
        a1.Dell()
"""

refver = C()

lap = Laptop()
lap.laptop(refver)
