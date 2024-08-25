#zip(*iterables) = aggregate elements from two or more iterables (list,tuples,sets,etc..) 
#                  creates a zip object with paired elements stored in tuples for each elements


usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
#s = {i:j for i,j in zip(usernames, passwords)}

users = zip(usernames ,passwords)

#you can also cast the type into another type list list ,tuple or dict
# users = list(zip(usernames,passwords))

for i in users:
    print(i)

