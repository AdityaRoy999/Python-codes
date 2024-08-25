import os
# don't use single \ it is for escape sequence for string so use \\
source = "C:\\Users\\adiro\\Downloads\\test.txt"
destination = "C:\\Users\\adiro\\OneDrive\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print("source was moved")

except FileNotFoundError:
    print(source+" was not found" )