import pygame


class Laser:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        screen.blit(self.image, self.rect)

    def move(self, speed):
        self.rect.y += speed

    def off_screen(self):
        return self.rect.y > HEIGHT or self.rect.y < 0


class Ship:
    COOLDOWN = 30  # величина замедления при выстрелах лазерами

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health  # уровень здоровья
        self.ship_image = None  # изображение корабля
        self.rect = None  # прямоугольник для изображения корабля
        self.laser_image = None  # изображение лазера
        self.lasers = []  # список всех выпущенных лазеров
        self.cool_down_counter = 0

    def draw(self):
        screen.blit(self.ship_image, self.rect)
        # отрисовка лазеров
        for laser in self.lasers:
            laser.draw()

    def move_lasers(self, speed):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen() == True:  # если лазер вышел за пределы окна
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:  # выстрел лазером разрешён
            # выпускаем (создаём) лазер
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Player(Ship):
    pass


class Enemy(Ship):
    pass


def start_game():
    def redraw_window():
        screen.blit(bg_image, (0, 0))
        lives_label = main_font.render(f"Жизни: {lives}", True, WHITE)
        level_label = main_font.render(f"Уровень: {level}", True, WHITE)
        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        pygame.display.update()

    FPS = 60
    clock = pygame.time.Clock()

    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 40)

    run = True
    while run:
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        clock.tick(FPS)


pygame.init()
WIDTH, HEIGHT = 750, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космические захватчики")

# Цвета
WHITE = (255, 255, 255)

# Фон
bg_image = pygame.image.load("images/background-black.png").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Шрифт и текст
title_font = pygame.font.SysFont("comicsans", 56)
title_label = title_font.render("Нажми, чтобы начать...", True, WHITE)
title_rect = title_label.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Загрузка изображений
RED_SPACE_SHIP = pygame.image.load("images/pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pygame.image.load("images/pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pygame.image.load("images/pixel_ship_blue_small.png")
# Игрок
YELLOW_SPACE_SHIP = pygame.image.load("images/pixel_ship_yellow.png")
# Лазеры
RED_LASER = pygame.image.load("images/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("images/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("images/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("images/pixel_laser_yellow.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_game()

    screen.blit(bg_image, (0, 0))
    screen.blit(title_label, title_rect)
    pygame.display.update()