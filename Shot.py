from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def draw(self, screen, camera_x = 0, camera_y = 0):
        pygame.draw.circle(screen, "white", pygame.Vector2(self.position.x - camera_x, self.position.y - camera_y), self.radius, LINE_WIDTH)
    
    
    def update(self, dt):
        self.position += self.velocity * dt