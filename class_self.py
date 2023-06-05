class Computer:
    def __init__(self):
        self.name = "suresh"
        self.age = 26

    def Compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 26
c2 = Computer()

if c1.Compare(c2):
    print("they are same")
else:
    print("they are not same")


print(c1.name)
print(c2.name)