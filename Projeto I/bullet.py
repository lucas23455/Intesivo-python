import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    'Uma classe que administra projeteis disparados pela nave'

    def __init__(self, ai_settings, screen, ship):
        'cria um objeto de projetil'

        super(Bullet,self).__init__()
        self.screen = screen

        #cria um retangulo para o projetil
        #posiçao correta
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        #armazena a posiçao do projetil
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor



    def update(self):
        'move o projetil'

        #atualiza a posiçao decimal do projetil
        self.y -= self.speed_factor

        #atualiza a posiçao de rect
        self.rect.y = self.y


    def draw_bullet(self):
        'desenha o projetil na tela'

        pygame.draw.rect(self.screen, self.color, self.rect)