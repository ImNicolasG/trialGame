import pygame


class Coin(pygame.sprite.Sprite):
    COLOR = (254, 186, 23) # Gold*

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)