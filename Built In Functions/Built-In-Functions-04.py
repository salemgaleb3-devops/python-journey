#######     Built-In Functions     ###############
#  map()
## map take a function and + iterator
## called map because it maps the function in every element
# function can be predefined or lambda function

## map with predefined function
def formatext(text):
    return f"- {text} -"

tmyext = ["salem", "Ali", "Ahmed", "saEEd"]

myformattext = map(formatext, tmyext)
# print(myformattext)

for name in myformattext :

    print(name)

print("#" * 100)

# map with lambda
tmyext = ["salem", "Ali", "Ahmed", "saEEd"]

myformattext = map(lambda text :  f"- {text} -", tmyext)
# print(myformattext)

for name in myformattext :

    print(name)