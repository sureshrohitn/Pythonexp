import numpy as np
inputarr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(inputarr)

new_col11=np.array([[20,30,40]])
new_col=np.delete(inputarr, 2, axis=1)
print(new_col)

arr=np.insert(new_col, 2, new_col11, axis=1)
print(arr)

arr1=np.insert(new_col,0,new_col11,axis=1)
print(arr1)



a=np.loadtxt("Exception.txt", dtype=int)
print(a)
