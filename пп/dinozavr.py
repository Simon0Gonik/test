import pygame
from classes import *

WIDTH = 1000  # можно изменить
HEIGHT = 325

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Google's Dinosaur")

timer1 = pygame.USEREVENT + 0
timer2 = pygame.USEREVENT + 1

pygame.init()
pygame.time.set_timer(timer1, 2000)
pygame.time.set_timer(timer2, 7000)


score = 0
hi_score = 0

WHITE = (255, 255, 255)
GREEN = (47, 114, 84)



FPS = 60
clock = pygame.time.Clock()

WIDTHd = 100
HEIGHTd = HEIGHT//3

WIDTHc = 50
HEIGHTc = HEIGHT//6

# cоздаю динозавра


scroll_speed = 4  # 4 пикселя - скорость движения
game_over = False
die = False

dinos_group = pygame.sprite.Group()
dino = Dinosaur(WIDTHd//2, HEIGHT-(HEIGHTd//2), WIDTHd, HEIGHTd)
dinos_group.add(dino)

cactuses_group = pygame.sprite.Group()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and dino.running == False and game_over == False:
            dino.running = True
        elif event.type == timer1 and game_over == False and dino.running == True:
            cactus = Cactus(WIDTH-(WIDTHc//2), HEIGHT-(HEIGHTc//2), scroll_speed)
            cactuses_group.add(cactus)
        if event.type == timer2:
            scroll_speed += 4

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and dino.running != True:
        game_over = False
        score = 0
        cactuses_group.empty()

    screen.fill(WHITE)
    if pygame.sprite.groupcollide(dinos_group, cactuses_group, False,
                                  True):
        game_over = True
        die = True
        dino.running = False


    file = open('hi_score', mode='r', encoding='utf-8')
    hi_score = int(file.read())


    if game_over == True:
        with open('hi_score', mode='w', encoding='utf-8') as file:

            if hi_score < int(score):
                hi_score = int(score)

            file.write(str(hi_score))
        g_o = Fontt("game over", WIDTH//2, HEIGHT//2, 36)
        screen.blit(g_o.text_surface, g_o.text_rect)
        cactuses_group.empty()
        scroll_speed = 4
    dinos_group.draw(screen)
    dinos_group.update()

    cactuses_group.draw(screen)
    cactuses_group.update()



    if dino.running:
        score += 0.5

    score_p = Fontt(f'Счёт:{int(score)}', WIDTH-100, 50, 20)
    screen.blit(score_p.text_surface, score_p.text_rect)

    HIscore_p = Fontt(f'Рекорд:{hi_score}', WIDTH - 200, 50, 20)
    screen.blit(HIscore_p.text_surface, HIscore_p.text_rect)

    # screen.blit(dino_image, (0, HEIGHT - HEIGHTd))
    pygame.display.update()

    clock.tick(FPS)