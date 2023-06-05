
def SelectionSort(List):
    for i in range(len(List)-1):
        minimum=i
        for j in range(i+1,len(List)):
            if(List[j]<List[minimum]):
                minimum=j
        if(minimum!=i):
            List[i],List[minimum]=List[minimum],List[i]
    return List

def BubbleSort(List):
    for i in range(len(List)):
        for j in range(len(List)-1,i,-1):
            if List[j]<List[j-1]:
                List[j],List[j-1]=List[j-1],List[j]
    return List

def InsertionSort(List):
    for i in range(1, len(List)):
        currentnumber=List[i]
        for j in range(i-1,-1,-1):
            if List[j]>currentnumber:
                List[j],List[j+1]=List[j+1],List[j]
            else:
                List[j+1]=currentnumber
                
                break
    return List

if __name__=='__main__':
    List=[5,18,29,63,37,33,22,14]
    List1=[16,7,23,22,4,51,81,29]
    List2=[55,17,23,72,14,51,41,29]
    print('Selection Sorted List: ', SelectionSort(List))
    print('Bubble Sort List: ', BubbleSort(List1))
    print('Bubble Sort List: ', InsertionSort(List))
