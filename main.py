import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PARRALAX
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

    bg = pygame.transform.smoothscale(pygame.image.load('stars.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Scroll the background
    scroll_x = 0
    scroll_y = 0
    background_x = 0

    #organising drawable and updatable components into groups 
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    non_player = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable, non_player)
    Shot.containers = (updatable, drawable, shots, non_player)
    asteroid_field = AsteroidField()

    #game loop
    isRunning = True
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    camera_x = 0
    camera_y = 0
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
        camera_x = player.position.x - SCREEN_WIDTH / 2
        camera_y = player.position.y - SCREEN_HEIGHT / 2
        asteroid_field.update(dt, camera_x, camera_y)
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
        #sets the fill of the frame to a black colour and deletes old frames
        screen.fill("black")
       # Compute scrolling offset
        scroll_x = -camera_x * PARRALAX
        scroll_y = -camera_y * PARRALAX

        # Wrap using modulo
        x_rel = scroll_x % SCREEN_WIDTH
        y_rel = scroll_y % SCREEN_HEIGHT

        # Draw 4 tiles to cover all movement directions
        screen.blit(bg, (x_rel - SCREEN_WIDTH, y_rel - SCREEN_HEIGHT))
        screen.blit(bg, (x_rel, y_rel - SCREEN_HEIGHT))
        screen.blit(bg, (x_rel - SCREEN_WIDTH, y_rel))
        screen.blit(bg, (x_rel, y_rel))
        #screen.blit(bg, (-camera_x + player.position.x, -camera_y + player.position.y))
        for item in drawable:
            item.draw(screen, camera_x, camera_y) 
        #refreshes the game's screen
        pygame.display.flip()
       
    

if __name__ == "__main__":
    main()
