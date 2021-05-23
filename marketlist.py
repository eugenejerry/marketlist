print("HELLO, THERE!...This is Hydro!", "\n" "I am HYDRO again!", "\n" "I will be helping you with your list of requirements today..")
marketstuff = [ ]
name = input("Enter your Name pls: ")
print("Hi", name, "What Items do you wanna get today? (type below): ")

#as long the condition remains true, using while loop
while True:
    item = input("Enter an Item you which to purchase today: OR type X to cancel: ")
    
    if item == "x":
        print(name, " Below are the Item(s) you wish to get today ", "\n", marketstuff)
        break
        
    elif item == "":
        print("item cannot be empty pls")
    else:
        print(item, "is successfully added")
        marketstuff.append(item)
    for x in (marketstuff):
        print(x)
        


