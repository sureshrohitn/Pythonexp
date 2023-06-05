from colorama import Fore
word=input("enter any string:")

count={}
for i in word:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
for a,b in count.items():
    print("Charactor Count of:",a," : ", b)

print(Fore.RED,"Welcome")
