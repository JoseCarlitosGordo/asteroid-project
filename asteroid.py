from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        #ties the speed of the object to the screen's framerate (every 0.017 seconds)
        self.position += self.velocity * dt