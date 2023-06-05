def count_char(S):
    count={}
    for i in S:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print("Charactor Count of:", count)
    print()
word=input("Enter any String: ")
count_char(word)
 
