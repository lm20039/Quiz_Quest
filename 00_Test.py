#decoration
def decoration(statement, aesthetics):

    sides = aesthetics * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = aesthetics * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

#title
decoration("Welcome to Quiz Quest" ,"~")
decoration("You will be Quizzed on One Piece" ,"~")


start = input("Press [Enter] to start! ").lower()
if start == "":

    print()
    instructions = input("Have you played before? ").lower()
    if instructions == "no" or instructions == "n" or instructions == "nah":
        print(
            "You will be quizzed on 10 questions about One Piece to test your knowledge about the topic. There is a score system, each question you get correct it will give +1 point but some questions will give you more ;) Good luck!")

    elif instructions == "yes" or instructions == "y" or instructions == "yeah":
        print("Good luck ;)")

    else:
        print("Your so funny ... not, please answer with yes or no next time!")

    # score system
    score = 0
    win = "Correct +1 point"

    print()
    # function
    name = input("Before we get started, what is your name? ")
    print()

    # questions
    question_1 = input("Alright {}, What character created 'smile fruits'? ".format(name)).lower()

    if question_1 == "doflamingo" or question_1 == "doffy":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is Doflamingo!")

    print()

    question_2 = input("Who was Luffy's first enemy? ").lower()

    if question_2 == "alvida" or question_2 == "iron mace alvida" or question_2 == "that one fat lady":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is Alvida!")

    print()

    question_3 = input("What arc in One piece had Kin'emon introduced? ").lower()

    if question_3 == "punk hazard":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is Punk Hazard!")

    print()

    question_4 = input("How many Strawhat pirates were there before Wano? ").lower()

    if question_4 == "10":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is 10!")

    print()

    question_5 = input("THIS IS A SPECIAL QUESTION, MEANING ITS HARD! Who is the king of the marines? ").lower()

    if question_5 == "imu" or question_5 == "king imu":
        print("Correct! +5 points")
        score += 5

    else:
        print("Wrong! The answer is Imu!")

    print()

    question_6 = input("What marine fought the supernovas in Sabaody Archipelago? ").lower()

    if question_6 == "kizaru" or question_6 == "adam sandler":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is Kizaru!")

    print()

    question_7 = input("What element is Luffy invincible to? ")

    if question_7 == "lightning":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is lightning!")

    print()

    question_8 = input("Almost there {}, Who gave Jinbe the sun mark on his chest? ".format(name)).lower()

    if question_8 == "fisher tiger":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is Fisher Tiger!")

    print()

    question_9 = input("What is the last island on the journey to become the pirate king called? ")

    if question_9 == "laughtale" or question_9 == "laugh tale" or question_9 == "raftel":
        print("{}".format(win))
        score += 1

    else:
        print("Wrong! The answer is Laugh tale / Raftel!")

    print()

    question_10 = input("THIS IS A SPECIAL QUESTION, MEANING ITS HARD! What is the name of the character that ate the Ryu Ryu no mi model: Pteranodon? ")

    if question_10 == "king" or question_10 == "alber":
        print("Correct! +5 points")
        score += 5

    else:
        print("Wrong! The answer is King!")

    print()

    if score >= 14:
        print("Congrats, you did better than I expected! Your score is {} / 18 points, {}!".format(score, name))

    elif score == 0:
        print("Wow, you know nothing! Your score is {} / 18 points, {}!".format(score, name))

    else:
        print("Ha, you did pretty bad! Your score is {} / 18 points, {}!".format(score, name))