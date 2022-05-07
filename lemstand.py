#Library imports

#Custom module imports
from player import player
from gamestate import gamestate

"""Global constants."""
#Describes acceptable affirmative and negative responses in the lower case
AFFIRMATIVE = ["yes", "y"]
NEGATIVE    = ["no", "n"]
#Names of the days of the week
WEEKDAYS    = ["sunday", "monday", "tuesday", "wednesday", "thursday",
               "friday", "saturday"]

def title():
    """Displays the title graphic."""
    print("""
        L                                 L
        L                                 L
        L    LLLL LLLLL LLLL LLLL LLLL LLLL LLLL
        L    L  L L L L L  L L  L    L L  L L  L
        L    LLLL L L L L  L L  L LLLL L  L LLLL
        L    L    L L L L  L L  L L  L L  L L
        LLLL LLLL L   L LLLL L  L LLLL LLLL LLLL

                SSSSS  S               S
                S      S               S
                S     SSS SSSS SSSS SSSS
                SSSSS  S     S S  S S  S
                    S  S  SSSS S  S S  S
                    S  S  S  S S  S S  S
                SSSSS  S  SSSS S  S SSSS
        """)

def intro(game):
    """Displays introductory message, choose new or resume game."""
    #TODO: Big function, should probably be broken up
    print("""
        Hi! Welcome to Lemonsville, California!

        In this small town, you are in charge of
        running your own lemonade stand. You can
        compete with as many other people as you
        wish, but how much profit you make is up
        to you (the other stands' sales will not
        affect your business in any way). If you
        make the most money, you're the winner!!
        """)

    #Becomes true if the game is being continued
    continuing = False

    #Is the player starting a new game, or continuing?
    while True:
        try:
            in_str = input("""
                Are you starting a new game? (yes or no)
                Type your answer and hit return ==> """)
            if in_str.lower() in NEGATIVE:
                continuing = True
                break
            elif in_str.lower() in AFFIRMATIVE:
                break
        except ValueError:
            pass

    #How many players will be playing?
    while True:
        try:
            game.set_num_players(int(input("""
                How many people will be playing ==> """)))
            if game.get_num_players() in range(1, self.player_limit+1):
                break
        except ValueError:
            pass

    #Initialize the list of players
    game.init_players(game.get_num_players())

    #TODO: Have returning players reenter their data if continuing
    if continuing:
        print("Hi again! Welcome back to Lemonsville!")

        #Prompt the user for which day to resume the game at
        while True:
            try:
                game.set_current_day(1+int(input("""
                    Let's continue your last game from where
                    you left it last time. Do you remember
                    what day number it was? """)))
                if game.get_current_day in range(1, game.get_day_limit()+1):
                    break
            except ValueError:
                pass

        #Remind the player what the starting day is
        print("Okay -- we'll start with day no. " + str(self.current_day))

        #Update information for each player rejoining the game
        for player in game.get_players():
            #How much money did the player have, if less than 2.00 give them 2.00
            while True:
                try:
                    in_val = float(input("Player No. " + str(game.get_players().index(player)+1) +
                                            ", how much money (assets) did you have? "))
                    player.set_assets(in_val)
                    if player.get_assets() < 2.00:
                        print("O.K. - we'll start you out with $2.00")
                        player.set_assets(2.00)
                        break
                    else:
                        break
                except ValueError:
                    pass

    #Ask if players are ready to begin
    #TODO: Write a function for yes/no questions
    while True:
        try:
            in_str = input("...ready to continue? ")
            if in_str in AFFIRMATIVE:
                break
            elif in_str in NEGATIVE:
                exit()
        except ValueError:
            pass

def tutorial():
    """Displays a brief tutorial before the game begins."""
    #Yes to continue, no to end
    while True:
        try:
            in_str = input("""
                To manage your lemonade stand, you will
                need to make these decisions every day:

                1. How many glasses of lemonade to make
                (only one batch is made each morning)

                2. How Many Advertising Signs to make
                (the signs cost fifteen cents each)

                3. What price to charge for each glass

                You will begin with $2.00 cash (assets).
                Because your mother gave you some sugar,
                your cost to make lemonade is two cents
                a glass (this may change in the future).

                 Continue? """)
            if in_str.lower() in AFFIRMATIVE:
                break
            elif in_str.lower() in NEGATIVE:
                exit()
        except ValueError:
            pass

    while True:
        try:
            in_str = input("""
                Your expenses are the sum of the cost of
                the lemonade and the cost of the signs.

                Your profits are the difference between
                the income from sales and your expenses.

                The number of glasses you sell each day
                depends on the price you charge, and on
                the number of advertising signs you use.

                Keep track of your assets, because you
                can't spend more money than you have!

                 Are you ready to begin? """)
            if in_str.lower() in AFFIRMATIVE:
                break
            elif in_str.lower() in NEGATIVE:
                exit()
        except ValueError:
            pass

def main():
    """Main method for the game loop."""

    #Display the title graphic
    title()

    #Create a game object
    game = gamestate()

    #Display the introductory message
    game.intro()

    #Display the tutorial screen before the game begins
    tutorial()

    #Enter the core of the game loop
    for day in range(1, game.day_limit+1):
        #TODO: Weather report

        #TODO: Each player makes decisions for their stand

        #TODO: Each player is shown a daily financial report
        pass

#Start the game loop
main()
