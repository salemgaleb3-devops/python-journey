
tries = 4 

mainpassowrd = "salim77"

inputpassowrd =  input("Write the passowrd :   ")

while inputpassowrd != mainpassowrd :

    tries -= 1 

    print(f"Write the passowrd, { 'last' if tries == 1 else tries} chance  left")

    inputpassowrd =  input("Write the passowrd :   ")



    if tries == 1 :

        print("All tries is Finished")

        break


else :

    print("Passowrd is correct")








