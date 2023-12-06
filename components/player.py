import pygame
from constants import SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/player.png')
        #Scale the image
        self.image = pygame.transform.scale(self.image, (75, 75)) 
        # Reference to the image rect
        self.rect.center = (SCREEN_WIDTH // 2, 100)
        # The velocity of x
        self.velocity_x = 0
        # The velocity of y with initial velocity of -1
        self.velocity_y = -1  
        # The gravity so the player falls down after jumping
        self.gravity = 1
        # The amount of coordinates the player moves up when jumping
        self.jump_power = -15
        # Boolean for checking if the player is jumping
        self.is_jumping = False

    def handle_input(self, keys):
        # If the left key is pressed, update the x velocity to -5
        # (or move left)
        if keys[pygame.K_LEFT]:
            self.velocity_x = -5
        # If the right key is pressed, update the x velocity to 5
        # (or move right)
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = 5
        # If neither left or right key is pressed, set the x velocity to 0
        # (or not moving right or left)
        else:
            self.velocity_x = 0

        # If the space bar is pressed and the player is not jumping
        # (or not already jumping), set the y velocity to the jump power
        # this prevents double jumping
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True


    # How the user stays on the platform
    def handle_platform_collision(self, platform_hits):
        for platform in platform_hits:
            # If the player is moving downwards (falling or jumping down)
            # and the player is below the platform, set the player's bottom
            # to the platform's top and set the y velocity to 0
            if self.velocity_y >= 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.is_jumping = False
            # If the player is moving upwards (jumping up)
            # and the player is above the platform, set the player's top
            # to the platform's bottom and set the y velocity to 0
            elif self.velocity_y < 0:
                self.rect.top = platform.rect.bottom
                self.velocity_y = 0

    
    def update(self):
        self.velocity_y += self.gravity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
