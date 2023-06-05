from threading import *
from time import sleep


class First(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Second(Thread):
    def run(self):
        for i in range(5):
            print("welcome to")
            sleep(1)



class Third(Thread):
    def run(self):
        for i in range(5):
            print("Threading Concept")
            sleep(1)


a = First()
b = Second()
c = Third()

a.start()
sleep(0.2)
b.start()
sleep(0.2)
c.start()
a.join()
b.join()
c.join()
print()
print("Good Day!!")