def player():
    """Represents a single player."""
    def __init__(self):
        """Constructor for a player."""
        #Cash on hand, in dollars
        self.assets = 0
        #True if stand ruined by Thunderstorm, else False
        self.storm_ruined = False
        #Number of glasses lemonade made by the player
        self.glasses_made = 0
        #Price the player is charging for their lemonade, in dollars
        self.price_charged = 0
        #Number of signs made by the player
        self.num_signs = 0

def title():
    """Displays the title graphic."""
    #TODO: This could look better, replace when convenient
    print("""
        ;LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL;LLLLL
        ;LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL;LLLLL
        ;LLLL;;;;L;;;;;L;;;;L;;;;L;;;;L;;;;L;;;;
        ;LLLL;LL;L;L;L;L;LL;L;LL;LLLL;L;LL;L;LL;
        ;LLLL;;;;L;L;L;L;LL;L;LL;L;;;;L;LL;L;;;;
        ;LLLL;LLLL;L;L;L;LL;L;LL;L;LL;L;LL;L;LLL
        ;;;;L;;;;L;LLL;L;;;;L;LL;L;;;;L;;;;L;;;;

        LLLLLLLL;;;;;LL;LLLLLLLLLLLLLLL;LLLLLLLL
        LLLLLLLL;LLLLLL;LLLLLLLLLLLLLLL;LLLLLLLL
        LLLLLLLL;LLLLL;;;L;;;;L;;;;L;;;;LLLLLLLL
        LLLLLLLL;;;;;LL;LLLLL;L;LL;L;LL;LLLLLLLL
        LLLLLLLLLLLL;LL;LL;;;;L;LL;L;LL;LLLLLLLL
        LLLLLLLLLLLL;LL;LL;LL;L;LL;L;LL;LLLLLLLL
        LLLLLLLL;;;;;LL;LL;;;;L;LL;L;;;;LLLLLLLL
        """)

def intro():
    """Displays introductory message, choose new or resume game."""
    print("""
        Hi! Welcome to Lemonsville, California!

        In this small town, tou are in charge of
        running your own lemonade stand. You can
        compete with as many other people as you
        wish, but how much profit you make is up
        to you (the other stands' sales will not
        affect your business in any way). If you
        make the most money, you're the winner!!
        """)

    #TODO: Is the player starting a new game, or continuing?
    print("""
        Are you starting a new game? (yes or no)
        Type your answer and hit return ==> """)

    #How many players will be playing?
    print("How many people will be playing ==>")

def main():
    """Main method for the game loop."""

    #Display the title graphic
    title()

    #Display the introductory message
    intro()

    #Initialize game state variables
    #Number of players playing Lemonade Stand
    num_players = 1
    #Cost of lemonade per glass, in cents
    cost_lemonade = 0.5
    #Const of an advertising sign, in cents
    cost_sign = 0.15
    #Contains player objects
    players = []

    #Append number of players to list
    for x in range(num_players):
        players.append(player())

#Start the game loop
main()
