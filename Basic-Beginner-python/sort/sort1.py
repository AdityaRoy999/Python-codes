students = [("Squidward", "F", 60),
("Sandy", "A", 33),
("Patrick","D", 36),
("Spongebob", "B", 20),
("Mr.Krabs","C", 78)]
# let's say there is a thing inside the list that defines the name , grade and ages for each of the names
# and we want to sort the grades only so we can create a func that will operate on index 2 

#students_1 = (("Squidward", "F", 60),
#("Sandy", "A", 33),
#("Patrick","D", 36),
#("Spongebob", "B", 20),
#("Mr.Krabs","C", 78))
age = lambda ages:ages[2]
#sorted_students = sorted(students_1,key = age)   for the tuple inside tuple 

students.sort(key=age,reverse=True)

for i in students:
  print(i)