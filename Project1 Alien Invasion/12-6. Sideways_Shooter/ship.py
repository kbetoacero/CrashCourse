import pygame


class Ship:
    """ A Class to manage a ship """

    def __init__(self, ss_game):
        """ initialize the ship and set its starting position """
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/cohete_off_side2.png')
        self.rect = self.image.get_rect()

        #Start each new ship at the left center of the screen
        self.center_ship()

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the ship's position based on the movement flag """
       # update the ship's value, not the rect
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # update rect object from self.y
        self.rect.y = self.y

    def center_ship(self):
        """ center the ship on the center """
        self.rect.midleft = self.screen_rect.midleft

        # Store a decmal value for the ship's horizontal position
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)