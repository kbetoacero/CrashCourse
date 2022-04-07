import pygame


class Settings:
    """ A class to store all settings for SideWays Shooting """

    def __init__(self):
        """ initialize the game's settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.image_bg = pygame.image.load('images/science-fiction-g774a29dea_1280.png')

        # Ship Settings

        self.ship_speed = 2.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 6.0
        self.bullet_height = 3
        self.bullet_width = 19
        self.bullet_color = (230, 0, 0)
        self.bullet_allowed = 3

        # alien settings
        # alien_frecuency controls how often a new alien appears
        # higher values -> more frecueen aliens. Max = 1.0
        self.alien_frecuency = 0.008
        self.alien_speed = 1.0

