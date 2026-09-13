import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0.0
    time = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
            log_state()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            player.update(dt)
            player.draw(screen)
            pygame.display.flip()

            dt = time.tick(60) / 1000
            
if __name__ == "__main__":
    main()
