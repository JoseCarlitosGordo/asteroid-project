import pygame
import math
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    #will override
    def draw(self, screen):
        pass
    
    #will override
    def update(self, dt):
        pass

    def collides_with(self, other_circle):
        dist = math.sqrt((self.position.x-other_circle.position.x)**2 + (self.position.y-other_circle.position.y)**2)
        sum_radius = self.radius + other_circle.radius
        return dist <= sum_radius
