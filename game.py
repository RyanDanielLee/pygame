# game.py
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from screens.start import StartScreen
from screens.end import EndScreen

def main():
    pygame.init()

    # Import EndScreen after initializing pygame to avoid circular import
    from screens.game import GameScreen
    from screens.end import EndScreen

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Platformer")

    clock = pygame.time.Clock()  # Create a Clock object

    # Pass the GameScreen class to the EndScreen constructor
    current_screen = StartScreen(GameScreen, EndScreen(GameScreen))

    while True:
        current_screen.process_input()
        current_screen.update()
        current_screen.render(screen)

        pygame.display.flip()
        clock.tick(FPS)  # Use the tick method to control the frame rate

        if current_screen.next_screen:
            current_screen = current_screen.next_screen

if __name__ == "__main__":
    main()
