score = 0
win = "Correct +1 point"
wrong = "Wrong the answer is"
special = "THIS IS A SPECIAL QUESTION, MEANING ITS HARD!"
more_points = "Correct +5 points"

q_1 = input("What character created 'smile fruits'? ").lower()

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

q_8 = input("Who gave Jinbe the sun mark on his chest? ").lower()

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

q_10 = input("{} What is the name of the character that ate the Ryu Ryu no mi model: Pteranodon? ".format(special))

if q_10 == "king" or q_10 == "alber":
    print("{}".format(more_points))
    score += 5

else:
    print("{} King!".format(wrong))

print()

print("You have {} / 18 score!".format(score))