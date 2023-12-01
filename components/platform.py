# components/platform.py
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path=""):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image_path = image_path
        self.original_image = pygame.image.load(image_path).convert()  # Load the original image

        print(f"Original image size: {self.original_image.get_size()}")  # Debug line

        # If the image has transparency, set the color key
        self.original_image.set_colorkey((255, 255, 255))

        # Resize the image to match the platform size
        self.image = self.resize(width, height)

        print(f"Resized image size: {self.image.get_size()}")  # Debug line

    def resize(self, width, height):
        # Resize the image to match the platform size
        return pygame.transform.scale(self.original_image, (width, height))
