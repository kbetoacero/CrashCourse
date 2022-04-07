import sys
from time import sleep
from random import random

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class SidewaysShooter:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        pygame.display.set_caption("SideWays Shooter")

        # create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            self._check_events()

            if self.stats.game_active:
                # Consider creatong a new alien
                self._create_alien()

                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses """
        if event.key == pygame.K_UP:
            # Move ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullet Group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bulelts and get rid of old bullets """
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that have been dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
            #print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ check whether any bullts hav hit an alien """
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _create_alien(self):
        """ Create an alien, if conditions are right """
        if random() < self.settings.alien_frecuency:
            alien = Alien(self)
            self.aliens.add(alien)
            #print(len(self.aliens))

    def _update_aliens(self):
        """ update alien positions ans look for collisions with ship"""
        self.aliens.update()

        # look for alien_ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """ Respond to an aline hittong the ship """
        if self.stats.ships_left > 0:

            # Decrement ship left
            self.stats.ships_left -= 1

            # get rid of bullets and aliens
            #self.aliens.empty()
            self.bullets.empty()

            # center the ship
            self.ship.center_ship()

            # pause
            #sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """ update images on the screen, and flip to the new screen """
        # pygame.transform.scale(self.settings.image_bg, (self.settings.screen_width, self.settings.screen_height))
        self.screen.blit(self.settings.image_bg, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make an instance, and run the game
    ss = SidewaysShooter()
    ss.run_game()