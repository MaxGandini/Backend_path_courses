import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y,radius):

        super().__init__(x,y,radius)
        self.velocity = pygame.vector2(0,0)
        self.SHOT_RADIUS = SHOT_RADIUS 
        
    def draw(self,screen):
        x,y = self.position
        pygame.draw.circle(screen,"white",(x,y),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt
