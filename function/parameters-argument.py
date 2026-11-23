
a, b, c = "salem", "omer", "ossama"

# print(f"hello {a}")
# print(f"hello {b}")
# print(f"hello {c}")

# def                     is the function key
# say_hello()             function name
# say_hello(name)         name is the parameter
# print(f"Hello {name}")  is the task
# say_hello(a)            a is the argument
# def say_hello(name):
#
#     print(f"Hello {name}")
#
# say_hello(a)
# say_hello(b)
# say_hello(c)

def addition(n1, n2):

    if type(n1) != int or type(n2) != int:

        print("Onlay interrger are allowed")

    else:

        print(n1 + n2)
addition(100, 90)

def fullname(first, middle, last):

    print(f" {first.strip().capitalize()} {middle.upper():.1s} {last.strip().capitalize()}")

fullname("salem", "ghaleb", "bamakhram")








