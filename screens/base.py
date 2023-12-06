import pygame

class BaseScreen:
    def __init__(self):
        self.next_screen = self

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        pass

    def render(self):
        pass

    def switch_to_next_screen(self):
        pass