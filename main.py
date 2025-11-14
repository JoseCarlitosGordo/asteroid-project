import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
def main():
    print(f"Starting Asteroids! with pygame version: {pygame.version.ver}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    isRunning = True

    #adds event listener to the close button at the top right. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    #game loop
    
    while isRunning:
        log_state()
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
