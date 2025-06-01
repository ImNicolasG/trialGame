import pygame
import random
from config import settings

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (random.randint(0, settings.SCREEN_WIDTH-10),
                                                 random.randint(0, settings.SCREEN_HEIGHT-30)))