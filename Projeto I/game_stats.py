class GameStats():
    'armazena dados estatisticos da invasao alien'

    def __init__(self,ai_settings):
        'inicializa dados estatisticos'
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        'inicializa os dados estatisticos que podem mudar durante o jogo'
        self.ships_left = self.ai_settings.ship_limit


