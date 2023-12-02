# screens/start.py
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .base import BaseScreen

class StartScreen(BaseScreen):
    def __init__(self, game_screen_class, end_screen_class):
        super().__init__()
        self.game_screen_class = game_screen_class
        self.end_screen_class = end_screen_class
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Press SPACE to start", True, (0, 0, 0))

    def process_input(self):
        super().process_input()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next_screen = self.game_screen_class("levels/level1.csv")
            # Pass EndScreen class to GameScreen for later use
            self.next_screen.end_screen_class = self.end_screen_class

    def render(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, (SCREEN_WIDTH // 2 - self.text.get_width() // 2, SCREEN_HEIGHT // 2 - self.text.get_height() // 2))
