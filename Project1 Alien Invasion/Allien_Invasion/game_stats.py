import json


class GameStats:
    """ track statistics for alien inavsion """

    def __init__(self, ai_game):
        """ initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien inavsion in active state
        self.game_active = False

        # high score should never be reset
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """ Get high score from file if it exist. """
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """ initialize statistics tha can change suring the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
