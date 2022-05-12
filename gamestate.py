"""Contains a class to be instantiated as gamestate objects."""

#Library imports
import random

#Custom module imports
from player import player

class gamestate():
    """Represents a game of Lemonade Stand."""
    def __init__(self):
        """Constructor to initialize game state variables."""

        #Which day is it?
        self._current_day = 1
        #How many days are being played before the game ends
        self._day_limit = 12

        #Refers to the type of weather
        #   2   sunny
        #   5   thunderstorms
        #   7   hot & dry
        #   10  cloudy
        self._sky_color = 2

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

    def get_sky_color(self):
        """Accessor for the self._sky_color variable."""
        return self._sky_color

    def set_sky_color(self, new):
        """Mutator for the self._sky_color variable."""
        self._sky_color = new
    
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
            self._players.append(player())

    def rnd(self, aexpr):
        """Emulates the functionality of the rnd function is Applesoft Basic."""
        #rnd can live in gamestate for now, might make another module just for
        #   helper functions like this
        #If aexpr is positive, return a rand from 0 to 0.999r
        if aexpr >= 0:
            rnd_result = random.random()
            return rnd_result
        #If aexpr is zero repeat the last rand result
        elif aexpr == 0:
            return rnd_result
        #If aexpr is negative, reseed the generator
        else:
            random.seed()

    def forecast(self):
        """Notify the players of the day's weather."""

        #Random factor for determining type of weather
        #   2   sunny
        #   5   thunderstorms
        #   7   hot & dry
        #   10  cloudy
        self._sky_color = self.rnd(1)

        #3 in 5 chance of a sunny day
        if self._sky_color < 0.6:
            self._sky_color = 2
        #1 in 5 chance of a cloudy day
        elif self._sky_color < 0.8:
            #If it would otherwise be a cloudy day, there is a 1 in 4 change of thunderstorms
            if self.rnd(1) < 0.25:
                self._sky_color = 5
            else:
                self._sky_color = 10
        #1 in 5 chance of a hot, dry day
        else:
            self._sky_color = 7

        #Weather should always be clear before day 3
        if self._current_day < 3:
            self._sky_color = 2

        #Notify the player of the weather
        print("""LEMONSVILLE WEATHER REPORT""")
        #TODO: Call a function to print an ASCII weather graphic
        if self._sky_color == 2:
            print("""SUNNY""")
        elif self._sky_color == 5:
            print("""THUNDERSTORMS!""")
        elif self._sky_color == 7:
            print("""HOT & DRY""")
        elif self._sky_color == 10:
            print("""CLOUDY""")
