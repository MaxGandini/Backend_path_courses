from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        x,y = self.position
        pygame.draw.circle(screen,"white",(x,y),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            x,y = self.position
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(x,y,new_radius)
            asteroid2 = Asteroid(x,y,new_radius)
            asteroid1.velocity = v1*1.2
            asteroid2.velocity = v2*1.2

