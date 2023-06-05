# Binary Search Values
print("Searching Nuber Based on the Binary search")

pos = -1

def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
    else:
        return False


list = [2, 3, 14, 25, 34, 51, 85, 65, 302, 358]
n = 302

if search(list, n):
    print("Number Found at: ", pos + 1)
else:
    print("Number Not Found")
