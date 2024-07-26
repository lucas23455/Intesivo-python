import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    'Uma classe que representa um único alienígena da frota'

    def __init__(self, ai_settings, screen):
        'Inicializa o alienígena'
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alien e redimensiona
        self.image = pygame.image.load('imagem/alien1.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Posiciona o alienígena na parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def blitme(self):
        'Desenha o alien na posição atual'
        self.screen.blit(self.image, self.rect)
