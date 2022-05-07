"""Contains a class to be instantiated as player objects."""

class player():
    """Represents a single player."""
    def __init__(self):
        """Constructor for a player."""
        #Cash on hand, in dollars
        self._assets = 0
        #True if stand ruined by Thunderstorm, else False
        self._storm_ruined = False
        #Number of glasses lemonade made by the player
        self._glasses_made = 0
        #Price the player is charging for their lemonade, in dollars
        self._price_charged = 0
        #Number of signs made by the player
        self._num_signs = 0
    
    def get_assets(self):
        """Accessor for the assets variable."""
        return self._assets

    def set_assets(self, new):
        """Mutator for the assets variable."""
        #TODO: Typecheck here
        self._assets = new
    
    def get_storm_ruined(self):
        """Accessor for the assets variable."""
        return self._storm_ruined

    def set_storm_ruined(self, new):
        """Mutator for the storm_ruined variable."""
        self._storm_ruined = new
    
    def get_glasses_made(self):
        """Accessor for the glasses_made variable."""
        return self._glasses_made
    
    def set_glasses_made(self, new):
        """Mutator for the glasses_made varaible."""
        self._glasses_made = new
    
    def get_price_charged(self):
        """Accessor for the price_changed variable."""
        return self._price_charged
    
    def set_price_charged(self, new):
        """Mutator for the price_charged variable."""
        self._price_charged = new
    
    def get_num_signs(self):
        """Accessor for the num_signs variable."""
        return self._num_signs
    
    def set_num_signs(self, new):
        """Mutator for the num_signs variable."""
        self._num_signs = new