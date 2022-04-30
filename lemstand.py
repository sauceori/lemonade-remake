"""Global constants."""
#Describes acceptable affirmative and negative responses in the lower case
AFFIRMATIVE = ["yes", "y"]
NEGATIVE    = ["no", "n"]

class gamestate():
    """Represents a game of Lemonade Stand."""
    def __init__(self):
        """Constructor to initialize game state variables."""

        #Which day is it?
        self.current_day = 1
        #How many days are being played before the game ends
        self.day_limit = 12

        #Cost of lemonade per glass, in cents
        self.cost_lemonade = 0.5
        #Cost of an advertising sign, in cents
        self.cost_sign = 0.15

        #Number of players playing Lemonade Stand
        self.num_players = 1
        #Maximum number of players allowed in a single game
        self.player_limit = 30
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
                self.num_players = int(input("""
                    How many people will be playing ==> """))
                if self.num_players in range(1, self.player_limit+1):
                    break
            except ValueError:
                pass

        #Initialize the list of players
        self.init_players(self.num_players)

        #TODO: Have returning players reenter their data if continuing
        if continuing:
            print("Hi again! Welcome back to Lemonsville!")

            #Prompt the user for which day to resume the game at
            while True:
                try:
                    self.current_day = int(input("""
                        Let's continue your last game from where
                        you left it last time. Do you remember
                        what day number it was? """))
                    if self.current_day in range(1, self.day_limit+1):
                        break
                except ValueError:
                    pass

            #TODO: Update information for each player rejoining the game
            for player in self.players:
                break

class player():
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
