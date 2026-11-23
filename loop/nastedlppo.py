
# peoples = ["Salem", "Ali", "Saeed", "Ahemd"]
# skils = [ "php", "C++", "C#", "python"]

# for name in peoples : # Outer Loop

#     print(f"{name} skills is :")

#     for skill in skils : # inner Loop

#         print(f"- {skill}")

peoples = {

    "Salem" : {

        "php" : "10%",
        "C++" : "40%",
        "C#"  : "0%",
        "python" : "80%"
    },
    "Ali" : {
        "php" : "20%",
        "C++" : "50%",
        "C#"  : "10%",
        "python" : "90%"       
    },
    "Saeed" : {
        "php" : "30%",
        "C++" : "60%",
        "C#"  : "20%",
        "python" : "95%"
    },
    "Ahemed" : {
        "php" : "40%",
        "C++" : "70%",
        "C#"  : "30%",
        "python" : "100%"
    }
}

# print(peoples["Salem"])
# print(peoples["Ahemed"]['python'])

for name in peoples :

    # print(f"the skills of {name} is {peoples[name]}")
        print(f"the skills of {name} is : ")

        for skill in peoples[name] :

                print (f"- {skill.upper()} => {peoples[name][skill]}")


                

    



