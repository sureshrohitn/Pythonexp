a=[10,2.2,32.2,1,2,32,22]
s=list(a)
Largest_number=0

for x in a:
    if x>Largest_number:
        Largest_number=x
print("Largest Number in the give list",Largest_number)

print("__________________________________________________________")

a_list=[12,43,43,34,43,454,34,322,55,76,78]

def largest(a_list):
    Largest_number=0
    second_Largest_number=0
    for b in a_list:
        if b >Largest_number:
            Largest_number=b
    print("the largest Number in the given list is : ", Largest_number)
largest(a_list)

print("______________________________________________________")
def findLargest(arr):
    secondLargest = arr[0]
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]

    # Returning second largest element
    return secondLargest


# Calling above method over this array set
print("second Largest Number",findLargest([23,31,10,20,4,5,9]))


print("________________________________________________________")


def secondmax(arr):
    sublist = [x for x in arr if x < max(arr)]
    return max(sublist)

if __name__ == '__main__':
    arr = [23,31,10,20,4,5,9]
    print("Second Highest Number",secondmax(arr))