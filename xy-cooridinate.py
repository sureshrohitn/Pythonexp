print(' (x, y) Coordinates are')
for x in range(4):
    for y in range(3):
        print('(',x,', ',y,')')

print("_______________________________________________")
for i in range(5):
    if i%2==0:
        print("XXXXX")
    else:
        print("XX")

print("_______________________________________________")
for i in range(5):
    if i%2!=0:
        print("XXXXX")
    else:
        print("XX")
print("_______________________________________________")

a=[4,5,3,4,3]
for x in a:
    print("x"*x)

print("_______________________________________________")
a=[4,5,3,4,3]
for x in a:
    output=""
    for y in range(x):
        output+='x'
    print(output)