import pygame
import os
from config import settings
from entities import player, platform

pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.WINDOW_TITLE)
game_on = True # Is the game running

vec = pygame.math.Vector2 # 2 for 2D


pt1 = platform.Platform()
p1 = player.Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(pt1)
all_sprites.add(p1)

platforms = pygame.sprite.Group()
platforms.add(pt1)

while game_on:
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.jump(platforms)

    screen.fill((0,0,0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    p1.move()
    p1.update(p1, platforms)
    pygame.display.update()
    CLOCK.tick(settings.FPS)

pygame.quit()