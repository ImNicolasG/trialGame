import pygame
import math
from config import settings

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        samImage = pygame.image.load("./Assets/images/samurai.png")
        self.surf = pygame.transform.scale(samImage, (35, 50))
        self.rect = self.surf.get_rect()
        
        self.surfLeft = pygame.transform.flip(self.surf, True, False)
        self.surfRight = pygame.transform.scale(samImage, (35, 50))

        

        self.pos =  pygame.math.Vector2((10, 485)) #Start pos
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)

    def move(self):
        self.acc = pygame.math.Vector2(0,0.5) # second number is Gravity
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -settings.ACC
            self.surf = self.surfLeft
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = settings.ACC
            self.surf = self.surfRight
        self.acc.x += self.vel.x * settings.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > settings.SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.SCREEN_WIDTH

        self.rect.midbottom = self.pos


    def update(self, player, platform):
        hits = pygame.sprite.spritecollide(player, platform, False)
        if player.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    def jump(self, platform):
        hits = pygame.sprite.spritecollide(self, platform, False)
        if hits:
            self.vel.y = -10 # Jump height

