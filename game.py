import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from screens.start import StartScreen
from screens.end import EndScreen

def main():
    """
    The main function that initializes the game and starts the game loop.

    This function sets up the game window, handles input, updates the game state, and controls the frame rate.

    Returns:
        None
    """
    pygame.init()  # Initialize the Pygame library

    from screens.game import GameScreen
    from screens.end import EndScreen

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    pygame.display.set_caption("Database Hell")  

    # Clock for frame rate control
    clock = pygame.time.Clock()  

    # Pass the GameScreen class to the EndScreen constructor
    current_screen = StartScreen(GameScreen, EndScreen(GameScreen))

    while True:
        current_screen.process_input() 
        current_screen.update()  
        current_screen.render(screen) 

        pygame.display.flip()  

        # Control the frame rate using the clock
        clock.tick(FPS)  # This limits the loop to run at a specified frames per second (FPS)

        # Switch to next screen
        if current_screen.next_screen:
            current_screen = current_screen.next_screen 

if __name__ == "__main__":
    main()
