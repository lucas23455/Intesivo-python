class Settings():
    def __init__(self):
        # Inicializa as configurações do jogo
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        #configuraçoes da espaçonave
        self.ship_speed_factor = 1.5


        #configuraçao dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3