def statement_generator(statement, aesthetics):

    sides = aesthetics * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = aesthetics * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

statement_generator("Welcome to Quiz Quest        The Quiz topic is One Piece", "-")