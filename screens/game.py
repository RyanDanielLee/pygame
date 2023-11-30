# screens/game.py
import pygame
from components.player import Player
from components.level import Level
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from .base import BaseScreen

class GameScreen(BaseScreen):
    def __init__(self, level_file):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.level = Level(level_file)

        # Create player
        self.player = Player()
        self.all_sprites.add(self.player)

    def process_input(self):
        super().process_input()
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def update(self):
        self.all_sprites.update()

        # Check if the player collides with any platforms
        platform_hits = pygame.sprite.spritecollide(self.player, self.level.get_platforms(), False)
        self.player.handle_platform_collision(platform_hits)

    def render(self, screen):
        # Set background color
        screen.fill(WHITE)

        # Draw platform images
        for platform in self.level.get_platforms():
            screen.blit(platform.image, platform.rect.topleft)

        # Draw player sprite
        self.all_sprites.draw(screen)
