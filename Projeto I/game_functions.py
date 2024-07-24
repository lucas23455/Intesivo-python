import sys
import pygame

def check_events(ship):
    'Responde a eventos de pressionamento de teclas e mouse'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move a espaçonave para a direita
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                #Move a espaçonave para a esquerda
                ship.moving_left = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False






def update_screen(ai_settings, screen, ship):
    'Atualiza as imagens de tela'
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()