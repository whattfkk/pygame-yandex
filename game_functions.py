import sys
from pygame import display, QUIT, KEYDOWN, K_RIGHT, KEYUP, K_LEFT, K_SPACE, K_q, sprite, MOUSEBUTTONDOWN, mouse, K_DOWN, K_UP, K_c
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep, perf_counter

d = 0

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #Обрабатываем столкновение коробля с пришельцем

    if stats.ship_left > 0:
        #Уменьшение ship_left
        stats.ship_left -= 1

        #Обновление игровой информации
        sb.prep_ships()

        #Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        #Создание нового флота и размещение коробля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Пауза
        sleep(0.5)
    else:
        stats.game_active = False
        #Указатель мыши появляется
        mouse.set_visible(True)

def get_number_rows(ai_settings, ship_height, alien_height):
    #Определяем количество рядов
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    #Вычесляет количество пришельцев в ряду
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Создаём флот пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Проверка попаданий в пришельцев
    # При обнаружении попадания удалить пулю и пришельца
    if ai_settings.d == 0:
        collisions = sprite.groupcollide(bullets, aliens, True, True)
    if ai_settings.d == 1:
        collisions = sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        ##Если флот уничтожен начинается следующий уровень
        # Уничтожение существующих пуль, повышение скорости и создание нового флота
        bullets.empty()
        ai_settings.increase_speed()

        #Увеличение уровня
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def check_keydown_events(event, ai_settings, screen, ship, aliens, bullets):
    if event.key == K_RIGHT:
        # Переместить корабль вправо
        ship.moving_right = True
    elif event.key == K_LEFT:
        # Переместить корабль влево
        ship.moving_left = True
    elif event.key == K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        #Создание новой пули и включение ее в группу bullets
    #Выход из игры с помощью клавиши Q
    elif event.key == K_q:
        sys.exit()
    elif event.key == K_c:
        if ai_settings.count_skill == 1:
            ai_settings.alien_speed_factor = 0.5
            ai_settings.ship_speed_factor = 1.5
            ai_settings.alien_speedup_scale = 1.21
            ai_settings.count_skill = 0
    #Добавление режимов стрельбы
    elif event.key == K_DOWN:
        ai_settings.bullets_allowed = 1
        ai_settings.bullet_speed_factor = ai_settings.bullet_long_speed_factor
        ai_settings.bullet_width = 6
        ai_settings.d = 1
    elif event.key == K_UP:
        ai_settings.bullets_allowed = 4
        ai_settings.bullet_speed_factor = ai_settings.bullet_speed_factor1
        ai_settings.bullet_width = 3
        ai_settings.d = 0

def check_keyup_events(event, ship):
    if event.key == K_RIGHT:
        ship.moving_right = False
    elif event.key == K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == QUIT:  #Выход из игры
            sys.exit()
        elif event.type == KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, aliens, bullets)
        elif event.type == KEYUP:
            check_keyup_events(event, ship)
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    #Запускает новую игру при нажатии кнопки Play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #сброс игровых настроек
        ai_settings.initialize_dynamic_settings()

        #Указание мыши скрывается
        mouse.set_visible(False)

        #Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True

        #Сброс изображений счётов и уровня
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        #Создание нового флота и размещение коробля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_fleet_edges(ai_settings, aliens):
    #Реагирует на достижение пришельцем края экрана
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #Проверяет добрались ли пришельцы до нижнего края
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    #Проверяет появляется ли новый рекорд
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def change_fleet_direction(ai_settings, aliens):
    #Опускает весь флот и меняет направление
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()

    # Удаление пуль, вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #Проверяет достиг ли флот края экрана после чего обновляет позицию всех пришельцев во флоте
    check_fleet_edges(ai_settings, aliens)
    #Обновление позиции пришельцев
    aliens.update()

    #Проверка коллизий пришелец-корабль
    if sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    #Проверка пришельцев добравшихся до нижнего края экрана
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    #Обновляет изображения на экране и добавляет новые
    screen.blit(ai_settings.bg, (0, 0)) #Изменение цвета фона
    # Вывод счёта
    sb.show_score()
    #Все пули выводятся позади изображений коробля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    display.flip()