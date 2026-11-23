
import os
os.chdir("/home/salem/")
# print(os.getcwd())

myfile = open ("salim.txt")

# print(myfile) # file data object
# print(myfile.name)
# print (myfile.mode)
# print(myfile.encoding)
# print(myfile.read())
# print(myfile.read(5))
# print(myfile.readline(8))
# print(myfile.readline(2))
# print(myfile.readlines(10))
# print(type(myfile.readlines()))
for line in myfile:

    print(line)
    if line.startswith("I") :
        break
# close the file
myfile.close()







