######    Modules  =>  Create your own module    ############

# ------------------------
import sys  ## يعمل لك جلب للمسارات الموجدوة في النظام الذي سوف يبحث عن الموديول فيها
sys.path.append(r"D:\Intel")  # في حالة تريد اضافة مسار لكي يبجث عن الموديول فية
print(sys.path)

# import myModule
#
# print(dir(myModule))  # print function in the module
#
# myModule.hello_name("salem")
# myModule.howareyou("fine")

###  Alise

# import myModule as m
#
# print(dir(m))  # print function in the module
#
# m.hello_name("salem")
# m.howareyou("fine")

from myModule import hello_name as  h   # after as is the alise

h("Ali")




