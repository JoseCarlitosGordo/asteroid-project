from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
import math
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, speed = 0):
        super().__init__(x, y, radius)
        self.angle = 0.0
        self.speed = speed
        self.local_verts = self.generate_shape()
    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        ca = math.cos(math.radians(self.angle))
        sa = math.sin(math.radians(self.angle))
        px, py = self.position.x, self.position.y
        pts = []
        for x, y in self.local_verts:
            rx = x * ca - y * sa
            ry = x * sa + y * ca
            pts.append((px + rx, py + ry))  # offset to world
        pygame.draw.polygon(screen, "white", pts, LINE_WIDTH)
    
    def generate_shape(self):
        r = random
        verts = []
        points = 16
        lumpiness = 0.3
        for i in range(points):
            theta = (2 * math.pi * i) / points
            rr = self.radius * (1 + r.uniform(-lumpiness, lumpiness))
            x = rr * math.cos(theta)
            y = rr * math.sin(theta)
            verts.append((x, y))  
        return verts    
    def update(self, dt):
        #ties the speed of the object to the screen's framerate (every 0.017 seconds)
        self.speed += 0.001
        self.position += self.velocity * dt *self.speed
        
    

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        #generates random number between 20 and 50 for angle 
        split_angle = random.uniform(20, 50)
        asteroid1_angle = self.velocity.rotate(split_angle)
        asteroid2_angle = self.velocity.rotate(-split_angle)
        small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, small_asteroid_radius, self.speed)
        asteroid_2 = Asteroid(self.position.x, self.position.y, small_asteroid_radius, self.speed)
        asteroid_1.velocity = asteroid1_angle * 1.2
        asteroid_2.velocity = asteroid2_angle * 1.2