class A:
    def __init__(self):
        print("Class A init Method")

    def Strategy1(self):
        print("simple one")

    def Strategy2(self):
        print("little bit work on this ")


class B(A):

    def __init__(self):
        super().__init__()
        print("Class B init Method")

    def Strategy3(self):
        print("hard one")

    def Strategy4(self):
        print("this is not that much easy ")
b1=B()
