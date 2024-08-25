import numpy as np 
stats = np.array([[1,2,3],
                  [4,5,6]])
print("-----start-----")
print(stats)
print("-------------")
print(np.min(stats,axis=1))
print("-------------")
print(np.max(stats))
print("-------------")
print(np.sum(stats)) # give sum of all the elements in the matrix
print("-------------")
print(np.sum(stats,axis = 0)) 
print("-----end-----")

