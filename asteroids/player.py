from constants import *  # noqa: F403
from circleshape import *
import pygame
from shot import Shot

class Player(CircleShape):  # noqa: F405
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)  # noqa: F405
        self.x = x
        self.y = y
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # noqa: F405
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5  # noqa: F405
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
        pass

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        if keys[pygame.K_SPACE]:
            shot = Shot(self.x, self.y,SHOT_RADIUS)
            shot.rotate(dt)
            shot.velocity = 

