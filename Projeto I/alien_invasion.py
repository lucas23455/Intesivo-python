import sys
import pygame
from settings import Settings
from nave import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Invasao Alien')

    # Create a ship
    ship = Ship(ai_settings, screen)

    # Create a group to store bullets and aliens
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Remove bullets that have moved off the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        print(len(bullets))


run_game()
