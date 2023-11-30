import pygame
from constants import SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # Blue color for player
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, 100)
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 1
        self.jump_power = -15
        self.is_jumping = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.velocity_x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = 5
        else:
            self.velocity_x = 0

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True

    def handle_platform_collision(self, platform_hits):
        if self.velocity_y > 0:
            for platform in platform_hits:
                if self.rect.bottom <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.is_jumping = False

    def update(self):
        self.velocity_y += self.gravity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
