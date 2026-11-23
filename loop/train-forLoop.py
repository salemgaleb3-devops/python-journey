# Range
# myrange = range(1, 101)

# for number in myrange :

#     print(number)

# Dictaiory
myskils = {

    "php": "20%",
    "js" :  "40%",
    "c++": "60%",
    "python": "80%"
    
}

# print(myskils["js"])
# print(myskils.get("python"))

for skills in myskils :

    # print(skills)
    print(f" My progress in Language {skills}  is : {myskils[skills]}")  # Or {myskils.get(skils)}
