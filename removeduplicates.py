a=[23,21,32,23,2,84,23,2,80,21,9,16,7]
b=[]
for x in a:
    if x not in b:
        b.append(x)
b.sort()
print(b)