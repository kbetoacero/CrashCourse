from random import randint

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to reprsent a single alien in the fleet """

    def __init__(self, ss_game):
        """ initialize the alien and set its starting point """
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect atrtibutte
        self.image = pygame.image.load('images/spacecraft-g4e6668f73_640.png')
        self.rect = self.image.get_rect()

        # Start each new alien at a random position on the right side of the screen
        self.rect.left = self.screen.get_rect().right
        # the farthest dow the screen we'll place the alien is the height
        # of he screen, minus the height of the alien
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)
        # Store the alien's exact horozontal position
        self.x = float(self.rect.x)

    def update(self):
       """ Move the alien steadly to the left """
       self.x -= self.settings.alien_speed
       self.rect.x = self.x