i=0
j=3
number=8
while i<j:
    a = int(input("Guess the a number: "))
    i=i+1
    if a==number:
        print("congratulation your won!!!!!")
        break
else:
    print("Sorry your failed to Guess")