import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from screens.start import StartScreen
from screens.game import GameScreen
from screens.end import EndScreen

def main():
    pygame.init() 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    pygame.display.set_caption("Database Hell")  

    # Clock for frame rate control
    clock = pygame.time.Clock()  

    # Pass the GameScreen class to the EndScreen constructor
    current_screen = StartScreen(GameScreen, EndScreen)

    while True:
        current_screen.process_input() 
        current_screen.update()  
        current_screen.render(screen) 

        pygame.display.flip()  

        # This limits the loop to run at a specified frames per second (FPS)
        # The clock is refreshed in frames and in our case, it is refreshed every 1/60 seconds
        # This is how the player can update for falling and jumping
        clock.tick(FPS)  

        # Switch to next screen
        if current_screen.next_screen:
            current_screen = current_screen.next_screen 

if __name__ == "__main__":
    main()
