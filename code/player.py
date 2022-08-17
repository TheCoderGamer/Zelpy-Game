import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load("res/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED
        self.obstacles_sprites = obstacles

    def input(self):
        key = pygame.key.get_pressed()
        # Left
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -1
        # Right
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # Up
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.direction.y = -1
        # Down
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.x += self.direction.x * PLAYER_SPEED
        self.collision("horizontal")
        self.rect.y += self.direction.y * PLAYER_SPEED
        self.collision("vertical")

    def collision(self, direction):
        if direction == "horizontal":
            for obstacle in self.obstacles_sprites:
                if obstacle.rect.colliderect(self.rect):
                    # Right
                    if self.direction.x > 0:
                        self.rect.right = obstacle.rect.left
                    # Left
                    if self.direction.x < 0:
                        self.rect.left = obstacle.rect.right

        if direction == "vertical":
            for obstacle in self.obstacles_sprites:
                if obstacle.rect.colliderect(self.rect):
                    # Down
                    if self.direction.y > 0:
                        self.rect.bottom = obstacle.rect.top
                    # Up
                    if self.direction.y < 0:
                        self.rect.top = obstacle.rect.bottom

    def update(self):
        self.input()
        self.move()
