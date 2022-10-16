#score system
score = 0
win = "Correct +1 point"
print("There is a score system, each question you get correct it will give +1 point but some questions will give you more ;) Good luck!")
print()
#function
name = input("Before we get started, what is your name? ")
print()

#questions
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

question_7 = input("THIS IS A TRUE OR FALSE QUESTION! Kaido admires Luffy? ").lower()

if question_7 == "true" or question_7 == "yes":
    print("Correct! +2 points")
    score += 2

else:
    print("Wrong! The answer is true!")

print()
print("You have advanced to medium questions, so far you've got {} / 12 points, {}!".format(score, name))
print()

question_8 = input("Doing well {}, Who gave Jinbe the sun mark on his chest? ".format(name)).lower()

if question_8 == "fisher tiger":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is Fisher Tiger!")

print()

question_9 = input("Who along with Garp was sent to fight Roger? ").lower()

if question_9 == "sengoku":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is Sengoku!")

print()

question_10 = input("THIS IS A MULTI QUESTION CHOICE! Who is the strongest swordsman? Zoro, Oden, Ryuma, Mihawk ")

if question_10 == "ryuma":
    print("Correct! +2 points")
    score += 2

else:
    print("Wrong! The answer is Ryuma!")

print()

question_11 = input("What element is Luffy invincible to? ")

if question_11 == "lightning":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is lightning!")

print()

question_12 = input("THIS IS A SPECIAL QUESTION, MEANING ITS HARD! What is the name of the character that ate the Ryu Ryu no mi model: Pteranodon? ")

if question_12 == "king" or question_12 == "alber":
    print("Correct! +5 points")
    score += 5

else:
    print("Wrong! The answer is King!")

print()

question_13 = input("What is Ussop's dream? ")

if question_13 == "to become a brave warrior of the sea" or question_13 == "to be a brave warrior":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is to become a brave warrior of the sea!")

print()

question_14 = input("THIS IS A TRUE OR FALSE QUESTION! Nami joined the strawhats in orange town? ")

if question_14 == "false" or question_14 == "no":
    print("Correct! +2 points")
    score += 2

else:
    print("Wrong! The answer is false!")

print()
print("You have advanced to hard questions, so far you've got {} / 25 points, {}!".format(score, name))
print()

question_15 = input("Good job {}, What is the last island on the journey to become the pirate king called? ".format(name))

if question_15 == "laughtale" or question_15 == "laugh tale" or question_15 == "raftel":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is Laugh tale / Raftel!")

print()

question_16 = input("Who is Shanks right hand man? ")

if question_16 == "ben" or question_16 == "ben beckman":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is Ben Beckman!")

print()

question_17 = input("THIS IS A MULTI QUESTION CHOICE! Which of these things is Luffy invincible to? Bullets / Canon balls, Fire, Venom, Magma ")

if question_17 == "bullets" or question_17 == "canon balls" or question_17 == "bullets / canon balls" or question_17 == "fire" or question_17 == "venom":
    print("Correct! +2 points")
    score += 2

else:
    print("Wrong! The answer is all of them except magma!")

print()

question_18 = input("Who had the giant strawhat? ")

if question_18 == "joyboy" or question_18 == "joy boy":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is JoyBoy!")

print()

question_19 = input("THIS IS A SPECIAL QUESTION, MEANING ITS HARD! Which character had big moms devil fruit (Soru Soru no mi) before her? ")

if question_19 == "carmel" or question_19 == "mother carmel":
    print("Correct! +5 points")
    score += 5

else:
    print("Wrong! The answer is Mother Carmel!")

print()

question_20 = input("What happens to the devil fruits after a devil fruit eater dies? ")

if question_20 == "it becomes the closest fruit" or question_20 == "it transfers into the closest fruit" or question_20 == "it transfers into the closest normal fruit" or question_20 == "it becomes the closest normal fruit":
    print("{}".format(win))
    score += 1

else:
    print("Wrong! The answer is it becomes the closest fruit!")

print()

question_21 = input("THIS IS A TRUE OR FALSE QUESTION! Akainu is stronger than Garp? ")

if question_21 == "false" or question_21 == "no":
    print("Correct! +2 points")
    score += 2

else:
    print("Wrong! The answer is false!")

print()
print("Your score is {} / 38 points, {}".format(score, name))