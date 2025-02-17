import pygame  # noqa: F401
from circleshape import *  # noqa: F403
from player import Player # noqa: F403
from constants import *  # noqa: F403
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt=0
    updatable= pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)  # noqa: F405
    print("Screen height:", SCREEN_HEIGHT)  # noqa: F405

    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])  # noqa: F405
    x = SCREEN_WIDTH/2  # noqa: F405
    y = SCREEN_HEIGHT/2  # noqa: F405

    player_0 = Player(x,y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        delta = clock.tick(60)/1000
        updatable.update(delta)
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
