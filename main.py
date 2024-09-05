import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    my_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fill_color_black = (0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        my_surface.fill(fill_color_black)
        pygame.display.flip()

if __name__ == "__main__":
    main()
