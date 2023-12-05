# screens/game.py
import pygame
from components.player import Player
from components.level import Level
from components.platform import EndPlatform
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from .base import BaseScreen
from .end import EndScreen

class GameScreen(BaseScreen):
    def __init__(self, level_file):
        super().__init__()
        self.background = pygame.image.load('./images/background.png')
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.level = Level(level_file)

        # Create player
        self.player = Player()
        self.all_sprites.add(self.player)

        # Initialize camera offset
        self.camera_offset_x = 0

    def process_input(self):
        super().process_input()
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def update(self):
        self.all_sprites.update()

        # Update camera offset
        self.camera_offset_x = SCREEN_WIDTH // 2 - self.player.rect.x

        # Check if the player has fallen off the edge
        if self.player.rect.y > SCREEN_HEIGHT:
            # Pass the GameScreen class to the EndScreen constructor
            self.next_screen = EndScreen(self.__class__)

        # Check if the player collides with any platforms
        platform_hits = pygame.sprite.spritecollide(self.player, self.level.get_platforms(), False)
        for platform in platform_hits:
            if isinstance(platform, EndPlatform):
                self.next_screen = EndScreen(self.__class__)
            else:
                self.player.handle_platform_collision(platform_hits)


    def render(self, screen):

        screen.blit(self.background, (0, 0))

        # Draw platform images
        for platform in self.level.get_platforms():
            screen.blit(platform.image, (platform.rect.x + self.camera_offset_x, platform.rect.y))

        # Draw player sprite
        screen.blit(self.player.image, (SCREEN_WIDTH // 2, self.player.rect.y))