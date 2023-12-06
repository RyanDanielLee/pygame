# screens/game.py
import pygame
from components.player import Player
from components.level import Level
from components.platform import EndPlatform
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .base import BaseScreen
from .end import EndScreen

class GameScreen(BaseScreen):
    def __init__(self, level_file):
        super().__init__()
        self.background = pygame.image.load('./images/background.png')
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.level = Level(level_file)
        self.start_time = pygame.time.get_ticks()

        # Create player
        self.player = Player()
        self.all_sprites.add(self.player)

        # Camera offset
        # This is used to move the player to the center of the screen at all times
        # and moves the platforms relative to the player
        # This prevents the player from moving off the screen
        self.camera_offset_x = 0

    def process_input(self):
        super().process_input()
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def update(self):
        self.all_sprites.update()

        # Update camera offset to center the player when moving
        self.camera_offset_x = SCREEN_WIDTH // 2 - self.player.rect.x

        # Check if the player has fallen off platforms
        if self.player.rect.y > SCREEN_HEIGHT:
            # Pass the GameScreen class to the EndScreen constructor
            # to allow the player to restart the game
            self.next_screen = EndScreen(self.__class__, self.elapsed_time)  

        # Check if the player collides with any platforms
        platform_hits = pygame.sprite.spritecollide(self.player, self.level.get_platforms(), False)
        for platform in platform_hits:
            # Check if the player collides with the end platform
            # If so, go to the end screen
            if isinstance(platform, EndPlatform):
                self.next_screen = EndScreen(self.__class__, self.elapsed_time)
            # If not, handle the collision with the platform
            else:
                self.player.handle_platform_collision(platform_hits)

        # Update time score 
        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

    def render(self, screen):
        screen.blit(self.background, (0, 0))

        # Draw platform images
        for platform in self.level.get_platforms():
            screen.blit(platform.image, (platform.rect.x + self.camera_offset_x, platform.rect.y))

        # Draw player sprite
        screen.blit(self.player.image, (SCREEN_WIDTH // 2, self.player.rect.y))
