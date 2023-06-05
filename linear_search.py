# Liner search values

print("Searching Nuber Based on the Linear search")
ind = -1

list = [8, 5, 2, 9, 1, 4]
a = 5


def search(list, a):
    i = 0
    while i < len(list):
        if list[i] == a:
            globals()['ind'] = i
            return True
        i = i + 1
    else:
        return False


if search(list, a):
    print("Number Found", ind + 1)
else:
    print("Number Not Found")

print("_____________________________________________________")
