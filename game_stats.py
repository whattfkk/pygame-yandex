class GameStats():
    #Отслеживает статистики для игры

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #Тгра запускается в неактивном состоянии
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        #Инициализирует статистику изменяющуюся в ходе игры
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
