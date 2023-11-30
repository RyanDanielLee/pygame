# components/platform.py
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(0, 255, 0)):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
