
############# Function Lambda #############
# It has no name
# U can call it inline without define it
# U can use it in return data from another function
# Lambda use for simple function and def for large task
# Lambda is one single expression not block of code
# lambda type is function

def say_hello(name, age ): return f"Hello {name} yor age is {age}"

hello = lambda  name, age : f"Hello, {name}! your age is {age}"

print(say_hello("ali", "20"))
print(hello("salem", "22"))
print(say_hello.__name__)
print(hello.__name__)
print(type(hello))
print(type(say_hello))


