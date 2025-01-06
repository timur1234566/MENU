from turtle import Screen

import pygame
import button_class
import random

pygame.init()
clock = pygame.time.Clock()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

MENU_FILL = (162, 209, 255)
MENU_BUTTON = (189, 244, 254)
MENU_TEXT = (151, 89, 186)

screen_size = wight, height = 800, 800
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Моя игра')


def redraw_window():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsans', 70)
    img_score = font.render('Привет, друг!', True, (BLUE))
    screen.blit(img_score, (50,30))
    prodol.draw(screen, (0, 0, 0))
    ex.draw(screen, (0, 0, 0))
    nastr.draw(screen, (0, 0, 0))
    skins.draw(screen, (0, 0, 0))
def set_menu():
    screen.fill((0, 0, 0))
    back.draw(screen, (0, 0, 0))
    enemies.draw(screen,(0, 0, 0))
def skin_men():
    screen.fill((0, 0, 0))
    back.draw(screen, (0, 0, 0))
def enemy_inf():
    screen.fill((0, 0, 0))
    font_1 = pygame.font.SysFont('comicsans', 45)
    img_t = font_1.render(f'колличество врагов:{x}', True, (RED))
    screen.blit(img_t, (50, 30))
    back_1.draw(screen, (0, 0, 0))



prodol = button_class.Button((BLUE), 50, 220, 500, 100, 'продолжить игру')
ex = button_class.Button((BLUE), 50, 340, 220, 100, 'выйти')
nastr = button_class.Button((BLUE), 50, 460, 350, 100, 'настройки')
back = button_class.Button((BLUE), 50, 650, 350, 100, 'назад')
skins = button_class.Button((BLUE), 50, 580, 350, 100, 'скины')
enemies = button_class.Button((BLUE), 200, 400, 600, 100, 'количество врагов')
back_1 = button_class.Button((BLUE), 430, 650, 350, 100, 'назад')


game_menu = False
setting_menu= False
enemy_col = False
skin_menu = False
running = True

while running:

    screen.fill(BLACK)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_menu = not game_menu
        if game_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nastr.is_over(pygame.mouse.get_pos()):
                    setting_menu = not setting_menu
                if ex.is_over(pygame.mouse.get_pos()):
                    running = False
                if skins.is_over(pygame.mouse.get_pos()):
                    skin_menu = not skin_menu
                if back.is_over(pygame.mouse.get_pos()):
                    setting_menu = False
                    skin_menu = False


                if setting_menu:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if enemies.is_over(pygame.mouse.get_pos()):
                            x = random.randint(1, 9)
                            enemy_col = not enemy_col
                        if back_1 .is_over(pygame.mouse.get_pos()):
                            enemy_col = False
                            setting_menu = True



            if event.type == pygame.MOUSEMOTION:
                if prodol.is_over(pygame.mouse.get_pos()):
                    prodol.color = GREEN
                else:
                    prodol.color = BLUE
                if ex.is_over(pygame.mouse.get_pos()):
                    ex.color = GREEN
                else:
                    ex.color = BLUE
                if nastr.is_over(pygame.mouse.get_pos()):
                    nastr.color = GREEN
                else:
                    nastr.color = BLUE
                if back.is_over(pygame.mouse.get_pos()):
                    back.color = GREEN
                else:
                    back.color = BLUE
                if skins.is_over(pygame.mouse.get_pos()):
                    skins.color = GREEN
                else:
                    skins.color = BLUE
                if enemies.is_over(pygame.mouse.get_pos()):
                    enemies.color = GREEN
                else:
                    enemies.color = BLUE
                if back_1.is_over(pygame.mouse.get_pos()):
                    back_1.color = GREEN
                else:
                    back_1.color = BLUE


    if game_menu:
        redraw_window()
        if setting_menu:
            set_menu()
            if enemy_col:
                enemy_inf()
        if skin_menu:
            skin_men()
    else:
        pass
    pygame.display.update()

pygame.quit()