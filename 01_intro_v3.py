#decoration
def decoration(statement, aesthetics):

    sides = aesthetics * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = aesthetics * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

#title
decoration("Welcome to Quiz Quest" ,"*")
decoration("You will be Quizzed on One Piece" ,"*")


start = input("Press [Enter] to start! ").lower()
if start == "":

    print("Continues on the next component")