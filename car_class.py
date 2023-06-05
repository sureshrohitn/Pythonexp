class Car:
    doors = 5

    def __init__(self):
        self.mil = 20
        self.com = "Audi"


c1 = Car()
c2 = Car()

c1.doors = 4
c1.mil = 25
print(c1.com, c1.mil, c1.doors)

print(c2.com, c2.mil, c2.doors)