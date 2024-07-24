import sys
import pygame
from settings import Settings
from nave import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Inicializa o jogo e cria um objeto
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Invasao Alien')

    # Cria uma nave
    ship = Ship(ai_settings, screen)

    # Cria um grupo para armazenar projéteis
    bullets = Group()

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # Remove projéteis que saíram da tela
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
