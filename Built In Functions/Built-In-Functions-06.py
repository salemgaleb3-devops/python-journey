######   Built In Functions   ######
from functools import reduce


# reduce()
## Reduce take function and + interator
## Reduce run A function on first and second Element and give result
## Then run function On result and third Element
## Then run function On result and fourth  Element and so on ..
## Tail one Element is left and this is the result of reduce
## the function can be Pre-defined or lambda function

def sumAll(num1, num2):
    return num1 + num2
numbers = [20, 19, 11, 50, 100]

result = reduce(sumAll, numbers)

print(result)
print("#" * 50)
resultlamda = reduce(lambda num1, num2, : num1 + num2 , numbers)

print(resultlamda)