class gamestate():
    """Represents a game of Lemonade Stand."""
    def __init__(self):
        """Constructor to initialize game state variables."""
        #Number of players playing Lemonade Stand
        self.num_players = 1
        #Maximum number of players allowed in a single game
        self.player_limit = 30
        #Cost of lemonade per glass, in cents
        self.cost_lemonade = 0.5
        #Const of an advertising sign, in cents
        self.cost_sign = 0.15
        #Contains player objects
        self.players = []

    def init_players(self, num_players):
        """Add player objects to the list of players.

        Arguments:
        num_players -- Number of new players to add to the state
        """
        for x in range(num_players):
            self.players.append(player())

    def intro(self):
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
        while True:
            try:
                self.num_players = int(input("""
                    How many people will be playing ==> """))
                if self.num_players in range(1, self.player_limit+1):
                    break
            except ValueError:
                pass

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

def main():
    """Main method for the game loop."""

    #Display the title graphic
    title()

    #Create a game object
    game = gamestate()

    #Display the introductory message
    game.intro()

#Start the game loop
main()
