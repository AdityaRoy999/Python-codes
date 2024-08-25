#sort() method = used with lists 
#sorted() function = used with iterabels

students = ["Squidward","Sandy","Patrick", "Spongebob", "Mr . Krabs"]
students_1 = ("Squidward","Sandy","Handy", "Mr .  Bob", "Mr . Krabs")# here you can not used sort() cause its not list.

students.sort()
#students.sort(reverse=True) # sorts the list in reverse
sorted_students = sorted(students_1) #sorted basically converts the students_1 into a new list containg the original arguments then operated the sort function on it 
#sorted_students = sorted(students_1,reverse=True) # sorts the iterable in reverse
#for i in students:
#    print(i)

#reversed_students = reversed(students)

#print(next(reversed_students))


#for i in sorted_students:
#    print(i)

