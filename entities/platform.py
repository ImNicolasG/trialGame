import pygame
from config import settings

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((settings.SCREEN_WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT - 10))