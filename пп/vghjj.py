import pygame
from clas import *
import random

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1300)


def draw_result(x, y):
    font = pygame.font.SysFont("Arial", 60)
    text = font.render(f"Счёт: {score}", True, WHITE, GREEN)
    screen.blit(text, (x, y))


WIDTH = 864
HEIGHT = 936

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load('images/bird1.png'))

WHITE = (255, 255, 255)
GREEN = (47, 114, 84)

FPS = 60
clock = pygame.time.Clock()

# Фон
bg_image = pygame.image.load("images/bg.png").convert()
ground_image = pygame.image.load("images/ground.png").convert()
ground_image_height = ground_image.get_height()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT - ground_image_height))
bg_image_height = bg_image.get_height()

ground_scroll = 0  # отвечает за значение координаты Х изображения земли ground_image
scroll_speed = 4  # 4 пикселя - скорость движения

birds_group = pygame.sprite.Group()
flappy_bird = Bird(100, HEIGHT // 2)
birds_group.add(flappy_bird)

pipe_group = pygame.sprite.Group()  # группа для труб

game_over = False
result_is_showed = False

score = 0
pass_pipe = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and flappy_bird.flying == False and game_over == False:
            flappy_bird.flying = True
        elif event.type == pygame.USEREVENT and game_over == False and flappy_bird.flying == True:
            # создание труб
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(WIDTH, HEIGHT // 2 + pipe_height, -1, scroll_speed)
            top_pipe = Pipe(WIDTH, HEIGHT // 2 + pipe_height, 1, scroll_speed)
            pipe_group.add(bottom_pipe, top_pipe)

    screen.blit(bg_image, (0, 0))
    birds_group.draw(screen)
    birds_group.update()

    pipe_group.draw(screen)
    pipe_group.update()

    screen.blit(ground_image, (ground_scroll, bg_image_height))

    if game_over == False and flappy_bird.flying == True:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    # проверка столкновений спрайтов ИЛИ выхода птички за верхнюю/нижнюю границы окна
    if pygame.sprite.groupcollide(birds_group, pipe_group, False,
                                  False) or flappy_bird.rect.top < 0 or flappy_bird.rect.bottom >= 768:
        game_over = True
        flappy_bird.flying = False

    if game_over:
        draw_result(WIDTH // 2 - 100, HEIGHT // 2 - 50)
        result_is_showed = True

    if len(pipe_group) > 0 and game_over == False and flappy_bird.flying == True:  # если в группе труб есть трубы
        bird = birds_group.sprites()[0]
        pipe = pipe_group.sprites()[0]
        if bird.rect.left > pipe.rect.left and bird.rect.right < pipe.rect.right and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True and bird.rect.left > pipe.rect.right:
            score += 1
            pass_pipe = False


    pygame.display.update()
    clock.tick(FPS)