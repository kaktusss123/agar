from math import sin

import pygame
from random import randint


class Ball:

    def __init__(self, radius: int, color: tuple, screen_width: int, screen_height: int):
        self.x = randint(radius, screen_width - radius)
        self.y = screen_height + radius
        self.radius = radius
        self.color = color

    def move(self, speed):
        self.y -= speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class TexturedBall:

    def __init__(self, texture, screen_width, screen_height, speed):
        self.size = texture.get_rect()
        self.x = randint(0, screen_width - self.size[3])
        self.y = screen_height
        self.image = texture
        self.dynamic_x = self.x

        self.chaos = randint(0, 500)
        self.speed = randint(1, speed + 1)

    def move(self):
        self.y -= self.speed
        self.dynamic_x = self.x + 100 * sin((self.y + self.chaos) / 60)

    def draw(self, screen):
        screen.blit(self.image, (self.dynamic_x, self.y))

