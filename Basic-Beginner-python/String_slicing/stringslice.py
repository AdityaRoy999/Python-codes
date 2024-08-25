# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start: stop:step]

name = "Bro Code"

first_name = name[:3]        #[start:3]
last_name = name[4:]         #[4:end]
funky_name = name[::2]       #[start:end:2 spaces step]
reversed_name = name[::-1]   #[start:stop: 1 space step]


print (reversed_name)

websitel = "http://google.com"
website2 = "http://wikipedia.com"

#slice function slices the string from the star:stop given by the user

slice1 = slice(7,-4)

print(websitel[slice1])
print(website2[slice1])