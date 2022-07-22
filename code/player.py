import pygame
from settings import *
from pygame.math import Vector2 as vector

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((40,80))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft = pos)

        # Float based movement
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = 400

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and [pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] and [pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and [pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and [pygame.K_d]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self,dt):
        # Horizontal Movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)

        # Vertical Movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)

    def update(self,dt):
        self.input()
        self.move(dt)