from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self):
        pygame.draw.circle(self.x,self.y,2)

    def update(self,dt):
        self.postion += self.velocity * dt
