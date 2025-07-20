import pygame

ground = 325

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, x, y,WIDTHd, HEIGHTd):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('trex.png').convert()
        self.image = pygame.transform.scale(self.image, (WIDTHd, HEIGHTd))
        self.rect = self.image.get_rect(center=(x, y))

        self.counter = 0  # cчётчик
        self.vel = 0  # отвечает за скорость падения птички
        self.clicked = False  # флажок для нажатия на клавишу пробел
        self.running = False  # флажок для определения начала игры
    def update(self):
        if self.running == True:
            self.vel += 0.5
            if self.vel > 4:
                self.vel = 4
            # убеждаемся, что птичка не выходит на границу дороги
            if self.rect.bottom + int(self.vel) < ground:
                self.rect.y += int(self.vel)
            else:
                self.rect.bottom = ground
                self.clicked = False

        # управление кнопкой ПРОБЕЛ
        keys = pygame.key.get_pressed()
        if keys[
            pygame.K_SPACE] and self.clicked == False:  # if keys[pygame.K_SPACE] == True: была нажата клавиша пробел
            self.vel = -13
            self.clicked = True
        # if not keys[pygame.K_SPACE]:  # if keys[pygame.K_SPACE] == False:
        #     self.clicked = False
        # print(self.vel)

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, y,  scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        """
        :param x, y: координаты левого верхнего угла прям-ка с изображением трубы
        :param position: 1 - если трубу нужно создать сверху,
                        -1 - если трубу нужно создать снизу
        :param scroll_speed: cкорость движения трубы
        """
        self.image = pygame.image.load("cactus.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()
import pygame


BLACK = (0, 0, 0)
class Fontt():
    def __init__(self, textt, pos_x, pos_y, size):

        self.font = pygame.font.SysFont('candara', size)
        self.text_surface = self.font.render(textt, True, BLACK)  # True = сглаживание
        self.text_rect = self.text_surface.get_rect(center=(pos_x, pos_y))
