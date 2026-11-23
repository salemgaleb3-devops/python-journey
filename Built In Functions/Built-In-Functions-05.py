#######     Built-In Functions     ###############
# filter()
## filter take a function and + iterator
## filter run function in every element
## function can be predefined or lambda function
## filter out all element which the function return true
## function need to return boolean value .

#  Ex1
def checnumber(nnum) :


    return nnum > 20
data = [12, 1, 22, 199]

filterchec = filter(checnumber, data)

for n in filterchec :

    print(n)

