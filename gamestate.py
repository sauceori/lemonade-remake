"""Contains a class to be instantiated as gamestate objects."""

class gamestate():
    """Represents a game of Lemonade Stand."""
    def __init__(self):
        """Constructor to initialize game state variables."""

        #Which day is it?
        self._current_day = 1
        #How many days are being played before the game ends
        self._day_limit = 12

        #Cost of lemonade per glass, in cents
        self._cost_lemonade = 0.5
        #Cost of an advertising sign, in cents
        self._cost_sign = 0.15

        #Number of players playing Lemonade Stand
        self._num_players = 1
        #Maximum number of players allowed in a single game
        self._player_limit = 30
        #Contains player objects
        self._players = []
    
    def get_current_day(self):
        """Accessor for the current_day variable."""
        return self._current_day
    
    def set_current_day(self, new):
        """Mutator for the current_day varaible."""
        #TODO: Add typechecks
        self._current_day = new
    
    def get_day_limit(self):
        """Accessor for the day_limit variable."""
        return self._day_limit
    
    def set_day_limit(self, new):
        """Mutator for the day_limit variable."""
        self._day_limit = new
    
    def get_cost_lemonade(self):
        """Accessor for the cost_lemonade variable."""
        return self._cost_lemonade
    
    def set_cost_lemonade(self, new):
        """Mutator for the cost_lemonade variable."""
        self._cost_lemonade = new
    
    def get_cost_sign(self):
        """Accessor for the cost_sign variable."""
        return self._cost_sign
    
    def set_cost_sign(self, new):
        """Mutator for the cost_sign variable."""
        self._cost_sign = new
    
    def get_num_players(self):
        """Accessor for the num_players variable."""
        return self._num_players
    
    def set_num_players(self, new):
        """Mutator for the num_players variable."""
        self._num_players = new
    
    def get_player_limit(self):
        """Accessor for the player_limit variable."""
        return self._player_limit
    
    def set_player_limit(self, new):
        """Mutator for the player_limit variable."""
        return self._player_limit

    def get_players(self):
        """Accessor for the players variable."""
        return self._players

    def init_players(self, num_players):
        """Add player objects to the list of players.

        Arguments:
        num_players -- Number of new players to add to the state
        """
        for x in range(num_players):
            self.players.append(player())