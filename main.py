import pygame
import os
from config import settings

pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.WINDOW_TITLE)
game_on = True # Is the game running


while game_on:
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

pygame.quit()