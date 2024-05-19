import sys
import pygame
from configuracoes import Configuracoes

def run_game():
    # Inicializa o Pygame
    pygame.init()

    # Cria uma instância da classe Configuracoes
    ai_configuracoes = Configuracoes()

    # Configura a tela do jogo
    #importo a tela de classe configuraçoes
    tela = pygame.display.set_mode((ai_configuracoes.tela_largura, ai_configuracoes.tela_altura))
    pygame.display.set_caption('Invasao Alien')

    # Define a cor de fundo da tela
    bg_color = ai_configuracoes.bg_color

    # Laço principal do jogo
    while True:
        # Observa eventos de teclado e mouse
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

        # Preenche a tela com a cor de fundo
        tela.fill(bg_color)

        # Atualiza a tela
        pygame.display.flip()

run_game()
