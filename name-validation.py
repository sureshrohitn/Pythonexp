name=input("enter your name:")
length=len(name)
if length<=3:
    print("name must be atleast 3 charactors")
elif length>=50:
    print("name can be a maximum of 50 chaeacters")
else:
    print("name looks Cool")