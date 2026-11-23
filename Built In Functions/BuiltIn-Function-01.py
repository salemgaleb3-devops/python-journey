
#### Built In Function ####
#all()
#any()
#bin()
#id()
################

x = [10 , 20 , 30, 40, []]

if all(x) :    ## all() built-in function

    print("ALL element is true")

else:
    print("at least one element is false")

x = [10 , 20 , 30, [], []]

if any(x) :    ## any() built-in function

    print("threes at leat one element is true")

else:
    print("threes no any true element")

print(bin(2))   ## bin()  يحول الرقن او النص الى binary

a = 1
b = 2

print(id(a))  ##id()  هو الرقم الذي تتخزن في المتغيرات وكل شيء في الداكرة
print(id(b))



