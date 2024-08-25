#tuple is collection which is ordered and unchangeable used to group together related data


student = ("Bro",21,"male")


print(student.count("Bro"))
print(student.index("male"))

for x in range(len(student)):
 print(student[x])



for i in range(len(student)):
 if student[i] == 'Bro':
  print(i)


