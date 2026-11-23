
import os
# os.remove("salim.txt")  ## remove file put need the path or the file in working directory

# myfile = open("myfile.txt","w")
# myfile.write("Hello from Python")

# myfile = open("myfile.txt","a")
# myfile.truncate(5)   ##  ياخد اول 5 احرف موجودة في الملف حسب لرقم الذي تضعه

# myfile = open("myfile.txt","a")
# print(myfile.tell())  ## يخبرك مكان الحرف الذيي علية المؤشر للكتابة الات

myfile = open("myfile.txt","r")
myfile.seek(6)    ### يوجه مؤشر القرائة من الحرف الذي تكتبة ويبداء منه
print(myfile.read())


