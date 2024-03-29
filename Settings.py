from pygame import image
from game_stats import GameStats

class Settings():
    # Класс для хранения всех настроек игры

    def __init__(self):
        ##Инициализирует статические настройки игры
        #Размеры экрана
        self.bg = image.load("images/ground.bmp")
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.ship_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullets_allowed = 4
        self.fleet_drop_speed = 10
        #Темп ускорения игры
        self.speedup_scale = 1.1
        self.alien_speedup_scale = 1.1
        #Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.fleet_direction = 1
        self.ship_limit = 2
        self.d = 0
        self.bullet_long_speed_factor = 4
        #Время замедления
        self.local_time = 10
        #Количество скилов
        self.count_skill = 1

    def initialize_dynamic_settings(self):
        #Инициализирует настройки изменяющиеся в ходе игры
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.bullet_speed_factor1 = 3
        self.alien_speed_factor = 0.5

        #fleet_direction = 1 обозначает движение вправо a - 1 влево
        self.fleet_direction = 1

        #Подсчёт очков
        self.alien_points = 50

    def increase_speed(self):
        #Увеличивает настройки скорости и стоимости пришельцев
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor1 = self.bullet_speed_factor * self.speedup_scale
        self.alien_speed_factor *= self.alien_speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
