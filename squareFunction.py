import math
number=int(input("enter any number which you want to square: "))
def square(number):
    result = number * number
    print("displaying the square value of ", number, "is: ", result)


print("calculating the square value")
square(number)


a=math.sqrt(number)
print(a)