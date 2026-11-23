
# Function Recursion
# Print "wwwoooorrlld"  as world

def cleanworld(world):

    if len(world) == 1 :

        return world
    if world[0] == world[1] :

        return cleanworld(world[1:])

    return world[0] + cleanworld(world[1:])


print(cleanworld("wwwoooorrlld"))
