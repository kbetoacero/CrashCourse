class GameStats:
    """ tracks statistics for the game """

    def __init__(self, ss_game):
        """ Initialize statistics"""
        self.settings = ss_game.settings
        self.reset_stats()

        # Start the gme in active state
        self.game_active = Active

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit