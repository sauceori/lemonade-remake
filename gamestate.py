"""Contains a class to be instantiated as gamestate objects."""

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