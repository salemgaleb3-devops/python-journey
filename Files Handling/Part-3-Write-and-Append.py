
import os

os.chdir(os.path.dirname("/home/salem/"))

mylist = ["salem\n", "saeed\n", "ahmed\n"]
# file = open("salem.txt", "w")
#
# file.write("Hello World from Python\n")
# file.write("this is salem")
# file.write("ghaleb\n"* 10)
myfile = open("fun.txt", "a") ## a يسمح لك تكتب داخل الملف دون مسح المحتوى الموجود عكس الكتابه

myfile.write("this names is : \n")
myfile.write("new line")

myfile.close()
