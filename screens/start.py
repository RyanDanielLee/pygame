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
        self.name = self.font.render("By: Ryan Lee A01365270", True, (0, 0, 0))

    def process_input(self):
        super().process_input()
        keys = pygame.key.get_pressed()
        # If the space bar is pressed, switch to the main game screen
        if keys[pygame.K_SPACE]:
            self.next_screen = self.game_screen_class("levels/level1.csv")
            # Pass EndScreen class to GameScreen for later use
            self.next_screen.end_screen_class = self.end_screen_class(0)

    def render(self, screen):
        #Background color
        screen.fill((255, 255, 255)) 
        # Text message
        screen.blit(self.text, (SCREEN_WIDTH // 2 - self.text.get_width() // 2, SCREEN_HEIGHT // 2 - self.text.get_height() // 2))
        screen.blit(self.name, (SCREEN_WIDTH // 2 - self.name.get_width() // 2, SCREEN_HEIGHT // 2 - self.name.get_height() // 2 - 50))
