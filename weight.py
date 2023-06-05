weight=int(input("enter your weight"))
convert=input("Convert to (L)bs or (K)g:")


if convert.upper()=="L":
    print("Your are ",weight*0.45," kilos")
elif convert.upper()=="K":
    print("Your are ",weight/0.45," Pounds")
else:
    print("please enter the valid input")