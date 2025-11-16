import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from Shot import Shot
import sys
def main():
    print(f"Starting Asteroids! with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialising pygame logic
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    #organising drawable and updatable components into groups 
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    non_player = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable, non_player)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots, non_player)
    asteroid_field = AsteroidField()

    #game loop
    isRunning = True
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while isRunning:
        #ticks timer every 1/60th seconds, pausing the game for that amount of time
        last_called = timer.tick(60)
        #adds event listener to the close button at the top right. 
        dt = last_called/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        #updates everything in the updatable container (including asteroid field, asteroids, players, etc.)
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()


            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        #sets the fill of the frame to a black colour 
        screen.fill("black")
        #player.draw(screen)
        for item in drawable:
            item.draw(screen) 
        #refreshes the game's screen
        pygame.display.flip()
       
    

if __name__ == "__main__":
    main()
