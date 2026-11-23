myFavouritwebs = []

maxwebs = 5

while maxwebs > 0:

 web = input("website name without https://")

 myFavouritwebs.append(f"https://{web.strip().lower()}")  # strip يشيل المسافاست

 maxwebs -= 1 

 print(f"website added, {maxwebs} place left")

 print("My Favourit webs")

else :
 print (" Book makrk is full")

if len(myFavouritwebs) > 0 :

    myFavouritwebs.sort()
    index = 0

    print("printing the list Of the website")

    while index < len(myFavouritwebs) :

       print(myFavouritwebs[index])

       index += 1
