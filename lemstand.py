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

"""Other globals."""

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
    print("\nHi! Welcome to Lemonsville, California!\n"
        "\nIn this small town, you are in charge of"
        "\nrunning your own lemonade stand. You can"
        "\ncompete with as many other people as you"
        "\nwish, but how much profit you make is up"
        "\nto you (the other stands' sales will not"
        "\naffect your business in any way). If you"
        "\nmake the most money, you're the winner!!")

    #Becomes true if the game is being continued
    continuing = False

    #Is the player starting a new game, or continuing?
    while True:
        try:
            in_str = input("\nAre you starting a new game? (yes or no)\n"
                "Type your answer and hit return ==> ")
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
            game.set_num_players(int(input("\nHow many people will be playing ==> ")))
            if game.get_num_players() in range(1, game.get_player_limit()+1):
                break
        except ValueError:
            pass

    #Initialize the list of players
    game.init_players(game.get_num_players())

    #TODO: Have returning players reenter their data if continuing
    if continuing:
        print("\nHi again! Welcome back to Lemonsville!")

        #Prompt the user for which day to resume the game at
        while True:
            try:
                game.set_current_day(1+int(input("\nLet's continue your last game from where"
                    "\nyou left it last time. Do you remember"
                    "\nwhat day number it was? ")))
                if game.get_current_day() in range(1, game.get_day_limit()+1):
                    break
            except ValueError:
                pass

        #Remind the player what the starting day is
        print("\nOkay -- we'll start with day no. " + str(game.get_current_day()))

        #Update information for each player rejoining the game
        for player in game.get_players():
            #How much money did the player have, if less than 2.00 give them 2.00
            while True:
                try:
                    in_val = float(input("\nPlayer No. " + str(game.get_players().index(player)+1) +
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
            in_str = input("\n...ready to continue? ")
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
            in_str = input("\nTo manage your lemonade stand, you will"
                "\nneed to make these decisions every day:\n"
                "\n1. How many glasses of lemonade to make"
                "\n(only one batch is made each morning)\n"
                "\n2. How Many Advertising Signs to make"
                "\n(the signs cost fifteen cents each)\n"
                "\n3. What price to charge for each glass\n"
                "\nYou will begin with $2.00 cash (assets)."
                "\nBecause your mother gave you some sugar,"
                "\nyour cost to make lemonade is two cents"
                "\na glass (this may change in the future).\n"
                "\n Continue? """)
            if in_str.lower() in AFFIRMATIVE:
                break
            elif in_str.lower() in NEGATIVE:
                exit()
        except ValueError:
            pass

    while True:
        try:
            in_str = input("\nYour expenses are the sum of the cost of"
                "\nthe lemonade and the cost of the signs.\n"
                "\nYour profits are the difference between"
                "\nthe income from sales and your expenses.\n"
                "\nThe number of glasses you sell each day"
                "\ndepends on the price you charge, and on"
                "\nthe number of advertising signs you use.\n"
                "\nKeep track of your assets, because you"
                "\ncan't spend more money than you have!\n"
                "\n Are you ready to begin? ")
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
    intro(game)

    #Display the tutorial screen before the game begins
    tutorial()

    #Enter the core of the game loop
    for day in range(1, game.get_day_limit()+1):
        #TODO: Weather report
        game.forecast()

        #TODO: Each player makes decisions for their stand

        #TODO: Each player is shown a daily financial report
        pass

#Start the game loop
main()
