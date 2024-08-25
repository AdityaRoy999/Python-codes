text = "Yoooooo \n This is a new line of text "

with open('test.txt','w') as file: #w for write
    file.write(text)

with open('test.txt','a') as file: #a for append
    file.write(text)               #it will not overwrite the info in the test file whereas in 'w' it will replace the info.
    