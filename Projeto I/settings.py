class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.5  # Ajuste este valor para um número menor para desacelerar o movimento horizontal
        self.fleet_drop_speed = 2  # Ajuste este valor para controlar a velocidade de descida
        self.fleet_direction = 1  # 1 representa direita, -1 representa esquerda
