import pygame  # noqa: F401
from constants import *  # noqa: F403


def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)  # noqa: F405
    print("Screen height:", SCREEN_HEIGHT)  # noqa: F405
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])  # noqa: F405
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
