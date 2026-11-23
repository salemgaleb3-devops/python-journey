#####       Built In Functions         #########

# enumerate()
# help()
# reversed()

# enumerate(iterable, start) # start by defaults 0
myskills = ["HTML", "CSS", "JS", "C#", "C++", "PYTHON"]
# myskillsCounter = enumerate(myskills)
myskillsCounter = enumerate(myskills, 50 )
# print(type(myskillsCounter))
# for skill in myskillsCounter:
#     print(skill)

for counter, skill in myskillsCounter:   # counter ينوب عن العداد في الدالة يمكن وضعه بأي اسم
    print(f"{counter} -  {skill}")

# help()
print(help(help))  # اذا تريد معرفة عن شيء ما ذالة او اي شيء

# reversed()
mystring = " salem"
print(reversed(mystring))
for letter in reversed(mystring):
    print(letter)

