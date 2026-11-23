

# x = 1   # Global Scope 

def one() : 


    global x   # يعمل اوفر رايد لل المتغير اكس ويجعلة قبوبال 

    x = 2  # خاص بهذه النكشن فقط 

    print(f" varible from function Scope is {x}")

def two() : 

    # x = 4 # خاص بهذه النكشن فقط 

    print(f" varible from function Scope is {x}")  


one()
two()
print (f" varible from golbal scop is {x}")


