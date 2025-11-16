from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, speed = 0):
        super().__init__(x, y, radius)
        self.rotation = self.velocity.x
        self.speed = speed
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        #ties the speed of the object to the screen's framerate (every 0.017 seconds)
        self.speed += 0.01
        self.position += self.velocity * dt *self.speed
        self.rotation *= dt
    

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