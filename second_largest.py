def findLargest(arr):
	secondLargest = 0
	largest = min(arr)
	for i in range(len(arr)):
		if arr[i] > largest:
			secondLargest = largest
			largest = arr[i]
		else:
			secondLargest = max(secondLargest, arr[i])
	print("Laegest: ",largest)
	return secondLargest

arr=[2,34,12,33,89,32]
a=findLargest(arr)
print("Second Largest: ",a)
