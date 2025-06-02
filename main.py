import pygame
import os
import random
from config import settings
from entities import player, platform

pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
background = pygame.image.load("Assets/images/sBackground.png").convert()
backgroundfill = pygame.transform.scale(background, (settings.SCREEN_WIDTH + 10, settings.SCREEN_HEIGHT + 10))
pygame.display.set_caption(settings.WINDOW_TITLE)
game_on = True # Is the game running

vec = pygame.math.Vector2 # 2 for 2D


pt1 = platform.Platform()
p1 = player.Player()

pt1.surf = pygame.Surface((settings.SCREEN_WIDTH, 20))
pt1.surf.fill((255, 0, 0))
pt1.rect = pt1.surf.get_rect(center = (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT -10))

all_sprites = pygame.sprite.Group()
all_sprites.add(pt1)
all_sprites.add(p1)

platforms = pygame.sprite.Group()
platforms.add(pt1)



## Random Platforms
for x in range(random.randint(3, 5)):
    pl = platform.Platform()
    platforms.add(pl)
    all_sprites.add(pl)

while game_on:
    #Handle Events
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.jump(platforms)

    screen.fill((0,0,0))
    screen.blit(backgroundfill, (-5,-5))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    p1.move()

    p1.update(p1, platforms)
    pygame.display.update()
    CLOCK.tick(settings.FPS)

pygame.quit()