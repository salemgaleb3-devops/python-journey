######       Built In Function          ##########

#abs()
#pow()
#min()
#max()
#max()
#slice()

#abs(number)
print(abs(-100))
print(abs(100))
print(abs(35.25))
print(abs(-35.25))
print("#" * 100)

#pow(base, exp, mod)  => power   (base, exp) اجباري
print(pow(2, 5))
print(pow(2, 5, 10))   #(2*2*2*2*2) % 10 = 2 باقي القسمة
print("#" * 100)

#min(item, item, item, interator)
#max(item, item, item, interator)
myNumber = (22, 55, 65, -5, -22, )
print(min(10, 32, -2, -30))
print(max(10, 32, -2, -30))
print(min(myNumber))
print(max(myNumber))
print("#" * 100)

#slice()
a= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(a[:3])
print(a[slice(3)])
print(a[slice(3, 9)])



