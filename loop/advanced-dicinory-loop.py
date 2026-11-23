
myskils = {

    "php": "20%",
    "js" :  "40%",
    "c++": "60%",
    "python": "80%"
    
}

# print (myskils.items())

# for skils in myskils :

#     print (f" {skils} => {myskils[skils]}")

# for skill_key, skill_progress in myskils.items():

#     print(f" {skill_key} => {skill_progress}")


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

for name_key, langaue_key in peoples.items():

    print (f" {name_key} skills is : ")

    for main_key, mane_value in langaue_key.items() :

        print (f" {main_key} => {mane_value}")







