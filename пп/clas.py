import pygame

ground = 768
pipe_gap = 150  # расстояние между трубами


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 4):
            img = pygame.image.load(f"images/bird{i}.png").convert_alpha()
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))

        self.counter = 0  # cчётчик
        self.vel = 0  # отвечает за скорость падения птички
        self.clicked = False  # флажок для нажатия на клавишу пробел
        self.flying = False  # флажок для определения начала игры

    def update(self):
        if self.flying == True:
            # падение птички вниз (гравитация)
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            # убеждаемся, что птичка не выходит на границу дороги
            if self.rect.bottom + int(self.vel) < ground:
                self.rect.y += int(self.vel)
            else:
                self.rect.bottom = ground

        # управление кнопкой ПРОБЕЛ
        keys = pygame.key.get_pressed()
        if keys[
            pygame.K_SPACE] and self.clicked == False:  # if keys[pygame.K_SPACE] == True: была нажата клавиша пробел
            self.vel = -10
            self.clicked = True
        if not keys[pygame.K_SPACE]:  # if keys[pygame.K_SPACE] == False:
            self.clicked = False

        # изменение изображения птички
        # self.counter += 1
        # flap_cooldown = 5
        #
        # if self.counter > flap_cooldown:
        #     self.counter = 0
        #     self.index += 1
        #     if self.index >= len(self.images):
        #         self.index = 0

        #self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, scroll_speed):
        """
        :param x, y: координаты левого верхнего угла прям-ка с изображением трубы
        :param position: 1 - если трубу нужно создать сверху,
                        -1 - если трубу нужно создать снизу
        :param scroll_speed: cкорость движения трубы
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/pipe.png").convert_alpha()
        self.rect = self.image.get_rect()

        if position == 1:  # трубу нужно создать сверху
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - pipe_gap // 2)
        if position == -1:  # трубу нужно создать снизу
            self.rect.topleft = (x, y + pipe_gap // 2)

        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()

