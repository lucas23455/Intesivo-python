import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        'Inicializa a espaçonave'
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem da nave e redimensiona
        self.image = pygame.image.load('imagem/nave.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))  # Redimensione conforme necessário
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializa cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        'Atualiza a posição da espaçonave'
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        'Desenha a nave na posição atual'
        self.screen.blit(self.image, self.rect)
