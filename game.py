# game.py
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from screens.game import GameScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Platformer")

    clock = pygame.time.Clock()
    
    # Create a GameScreen instance with the path to your level CSV file
    game_screen = GameScreen("levels/level1.csv")

    while True:
        game_screen.process_input()
        game_screen.update()
        game_screen.render(screen)

        pygame.display.flip()
        clock.tick(FPS)

        if game_screen.next_screen:
            game_screen = game_screen.next_screen

if __name__ == "__main__":
    main()
