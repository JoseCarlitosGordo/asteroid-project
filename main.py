import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
def main():
    print(f"Starting Asteroids! with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialising pygame logic
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    
    
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
        player.update(dt)
        #sets the fill of the frame to a black colour 
        screen.fill("black")
        player.draw(screen)
        #refreshes the game's screen
        pygame.display.flip()
       
    

if __name__ == "__main__":
    main()
