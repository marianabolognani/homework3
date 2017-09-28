print ("This program will show you your future depending on your name and age.\n")

name = raw_input("Please enter your name:")

if name == "Raenita":

    age = int(raw_input("How old are you:"))
    if age >= 30 and age  <= 49:
        print ("You will find $100 on the floor today!")
    elif age >=50 and age <=65 :
        print ("You will win a free car!")
    else:
        print ("You will be forver healthy!")

else :
    print("Your pet has been hit by a car.")
    print("Your house is flooded")
    print("A piano will fall on you.")