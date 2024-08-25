from collections import defaultdict

"""values = {
    "person1":0,
    "person2":0,
    "person3":0
}"""
#when you try to print person 4 it will give error so we use defaultdict
"""values = {
    "person1":0,
    "person2":0,
    "person3":0
}
values['person4'] = 10
print(values)"""


"""mylist = [1,2,3,4,5,6,7,8,9,10]
counter = defaultdict(int)

for i in mylist:
    counter[i] += 1

print(counter)"""

#You can also use deafult dictionary for grouping stuff
words = ["apple","banana","potato","orange"]
grouped = defaultdict(list)

for i in words:
    grouped[i[0]].append(i)

print(grouped)