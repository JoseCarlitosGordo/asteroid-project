from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from Shot import Shot
import pygame
class Player(CircleShape):
    def __init__(self, x, y, player_radius = PLAYER_RADIUS):
        super().__init__(x, y, player_radius)
        self.rotation = 0
        self.bullet_cooldown = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotation_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotation_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        #ties the bullet cooldown to the frame rate
        self.bullet_cooldown -= dt
        #rotating the player character
        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            # rotate left
            self.move(dt)
        if keys[pygame.K_s]:
            # rotate right
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            #Shoot
            if(self.bullet_cooldown <= 0):
                self.bullet_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
    
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1)
        new_shot.velocity = new_shot.velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED