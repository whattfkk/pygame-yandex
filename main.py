from pygame import init, display
from Settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Инициализирует игру и создаёт объект экрана
    init() #Добавляем настройки для пайгейм
    ai_settings = Settings()
    screen = display.set_mode((ai_settings.screen_width, ai_settings.screen_height))#Создаём окно
    display.set_caption("Alien Invasion")

    #Создаём кнопку Play
    play_button = Button(ai_settings, screen, "Play")

    #Создание экземпляра GameStats и Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Создание коробля
    ship = Ship(ai_settings, screen)

    #Создаём группу для хранения пуль
    bullets = Group()

    #Создаём группу для хранения пришельцев
    aliens = Group()
    #Создаём флот пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()