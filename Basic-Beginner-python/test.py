from collections import Counter
s = [2,2,2,4,4,5]

c = {}

for i in s:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(c)