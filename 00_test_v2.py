#decoration
def decoration(statement, aesthetics):

    sides = aesthetics * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = aesthetics * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

#title
def title():
    decoration("Welcome to Quiz Quest" ,"?")
    decoration("You will be Quizzed on the anime 'One Piece'" ,"~")

print()

def instructions():
    print("You will be quizzed on 10 questions about One Piece, each question will give points, there are 18 points total. ")

#repeats the have you played before question
def yes_no(question) :
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y" or response == "yeah":
            response = "yes"
            return response

        elif response == "no" or response == "n" or response == "nah":
            response = "no"
            return response

        else:
            print("Answer with yes or no")

# score system
score = 0

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

print("Good luck ;)")

print()

# function
name = input("Before we get started, what is your name? ")
print()

win = "Correct +1 point"
wrong = "Wrong the answer is"
special = "THIS IS A SPECIAL QUESTION, MEANING ITS HARD!"
more_points = "Correct +5 points"

# questions
q_1 = input("ALright {}! What character created 'smile fruits'? ".format(name)).lower()

if q_1 == "doflamingo" or q_1 == "doffy":
    print("{}".format(win))
    score += 1

else:
    print("{} Doflamingo!".format(wrong))

print()

q_2 = input("Who was Luffy's first enemy? ").lower()

if q_2 == "alvida" or q_2 == "iron mace alvida" or q_2 == "that one fat lady":
    print("{}".format(win))
    score += 1

else:
    print("{} Alvida!".format(wrong))

print()

q_3 = input("What arc in One piece had Kin'emon introduced? ").lower()

if q_3 == "punk hazard":
    print("{}".format(win))
    score += 1

else:
    print("{} Punk Hazard!".format(wrong))

print()

q_4 = input("How many Strawhat pirates were there before Wano? ").lower()

if q_4 == "10":
    print("{}".format(win))
    score += 1

else:
    print("{} 10!".format(wrong))

print()

q_5 = input("{} Who is the king of the marines? ".format(special)).lower()

if q_5 == "imu" or q_5 == "king imu":
    print("{}".format(more_points))
    score += 5

else:
    print("{} King Imu!".format(wrong))

print()

q_6 = input("What marine fought the supernovas in Sabaody Archipelago? ").lower()

if q_6 == "kizaru" or q_6 == "adam sandler":
    print("{}".format(win))
    score += 1

else:
    print("{} Kizaru!".format(wrong))

print()

q_7 = input("What element is Luffy invincible to? ")

if q_7 == "lightning" or q_7 == "electricity":
    print("{}".format(win))
    score += 1

else:
    print("{} lightning!".format(wrong))

print()

q_8 = input("Almost done {}! Who gave Jinbe the sun mark on his chest to cover up his slave mark? ".format(name)).lower()

if q_8 == "fisher tiger":
    print("{}".format(win))
    score += 1

else:
    print("{} Fisher Tiger!".format(wrong))

print()

q_9 = input("What is the last island on the journey to become the pirate king called? ")

if q_9 == "laughtale" or q_9 == "laugh tale" or q_9 == "raftel":
    print("{}".format(win))
    score += 1

else:
    print("{} Laugh tale / Raftel!".format(wrong))

print()

q_10 = input("{} Last question {}! What is the name of the character that ate the Ryu Ryu no mi model: Pteranodon? ".format(special, name))

if q_10 == "king" or q_10 == "alber":
    print("{}".format(more_points))
    score += 5

else:
    print("{} King!".format(wrong))

print()

#results of quiz
if score >= 14:
    print("Congrats, you did better than I expected! Your score is {} / 18 points, {}!".format(score, name))

elif score == 0:
    print("Wow, you know nothing! Your score is {} / 18 points, {}!".format(score, name))

else:
    print("Ha, you did pretty bad! Your score is {} / 18 points, {}!".format(score, name))