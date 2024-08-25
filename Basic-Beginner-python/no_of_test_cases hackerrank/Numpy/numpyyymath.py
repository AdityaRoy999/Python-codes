import numpy as np
#Mathematics in array 
a = np.array([1,2,3,4])
print(a)
print("-------------")
print(a + 2)
print("-------------")
print(a - 2)
print("-------------")
print(a * 2)
print("-------------")
print(a / 2)
print("-------------")
b = np.array([1,0,1,0])
print(a + b)
print("-------------")
print(a ** 2)
print("-------------")
print(a//2)
print("-------------")
print(np.cos(a))
print("-------------")

#linear algebra
a = np.ones((2,3))
print(a)
print("-------------")

b = np.full((3,2), 2)
print(b)
print("-------------")

print(np.matmul(a,b))

#find the determinant 
c= np.identity(3)
print("-------------")
print(np.linalg.det(c))
print("---------end----------")