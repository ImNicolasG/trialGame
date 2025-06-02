import pygame
import random
from config import settings

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        platImage = pygame.image.load("./Assets/images/tile.png")

        self.surf = pygame.transform.scale(platImage, (40, 10))
        self.rect = self.surf.get_rect(center = (random.randint(0, settings.SCREEN_WIDTH-10),
                                                 random.randint(settings.SCREEN_HEIGHT - 50, settings.SCREEN_HEIGHT - 30)))