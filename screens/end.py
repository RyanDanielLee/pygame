# screens/end.py
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL
from .base import BaseScreen

class EndScreen(BaseScreen):
    def __init__(self, game_screen_class, elapsed_time=0): 
        super().__init__()
        self.game_screen_class = game_screen_class
        self.font = pygame.font.Font(None, 36)
        #Game over text
        self.text = self.font.render("Game Over! Press SPACE to restart", True, (0, 0, 0))
        #Round time score to 2 decimal places
        elapsed_time = round(elapsed_time, 2)
        #Time score text
        self.score_text = self.font.render(f"Time elapsed: {elapsed_time} seconds", True, (0, 0, 0))

    def process_input(self):
        super().process_input()
        # If the space key is pressed, go to the next screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next_screen = self.game_screen_class(LEVEL)

    def render(self, screen):
        screen.fill((255, 255, 255))
        # Render the text
        screen.blit(self.text, (SCREEN_WIDTH // 2 - self.text.get_width() // 2, SCREEN_HEIGHT // 2 - self.text.get_height() // 2))
        # Render the time score text
        screen.blit(self.score_text, (SCREEN_WIDTH // 2 - self.score_text.get_width() // 2, SCREEN_HEIGHT // 2 - self.score_text.get_height() // 2 + 50))
