import numpy as np



#The basics 
a = np.array([1,2,3])
print(a)
print("-------------")
b = np.array([[2.0,3.0,4.0],
              [6.0,7.0,8.0]])
print(b)
print("-------------")
#get dimension 
print(a.ndim)
print(b.ndim)
print("-------------")

#get shape 
print(a.shape)
print(b.shape)
print("-------------")
#get type
print(a.dtype)
print(b.dtype)
print("-------------")
#get size
print(a.size)
print(b.size)
print("-------------")
#itemsize
print(a.itemsize)
print(b.itemsize)
print("-------------")
#get total size
print(a.nbytes)