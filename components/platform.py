# components/platform.py
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path="", scale=1.0):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image_path = image_path
        self.original_image = pygame.image.load(image_path).convert()  # Load the original image

        print(f"Original image size: {self.original_image.get_size()}")  # Debug line

        # If the image has transparency, set the color key
        self.original_image.set_colorkey((255, 255, 255))

        # Resize the image based on the scale
        self.image = self.resize(scale)

        print(f"Resized image size: {self.image.get_size()}")  # Debug line

    def resize(self, scale):
        # Calculate the new size based on the scale
        new_width = int(self.original_image.get_width() * scale)
        new_height = int(self.original_image.get_height() * scale)
        return pygame.transform.scale(self.original_image, (new_width, new_height))
