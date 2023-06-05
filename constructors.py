class Person:
    def __self__(self, x, y):
        self.x = x
        self.y = y

    def talk(self):
        print("this is talk method")

    def walk(self):
        print("this is walk method")


a = Person()

a.walk()
a.talk()

print("__________________________________________________________")


class Poet:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Poet saying beautiful line")


b=Poet("Raju")
print(b.name)
b.talk()