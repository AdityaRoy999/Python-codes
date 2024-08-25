# copyfile() = copies contents of a file
# copy() =  copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
import shutil

shutil.copyfile('test.txt','test1.txt')  #src,dst  - it will make a copy  
shutil.copy('test.txt','test1.txt')  #src,dst  - it will make a copy  
shutil.copy2('test.txt','test1.txt')  #src,dst  - it will make a copy  