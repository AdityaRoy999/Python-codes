#accessing/changing specific elements rows,columns etc.
import numpy as np
a = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
print(a)

#get a specific element [r, c]
print(a[1,2])

#get a specific row 
print(a[0,:])

#get a specific column 
print(a[:,1])

#getting a little more fancy  [starindex:stopindex:stepsize]
print(a[0, 1:6:2])

#a[1,5] = 20 #changes the fifth element of the first row to 20
a[:,2] = [1,2]#changes the second element of the rows to the consecutive 1 and 2
print(a)

#a 3-d example for the above 
#get specific element outside in 
b= np.array([[[1,2], 
              [3,4]], 
              [[5,6], 
               [7,8]]])
print(b)
print(b[0,1,1])
b[:,0,:] = [[2,3],[3,4]]
print(b)