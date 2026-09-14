import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *
import sys
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0.0
    time = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(x, y)

    Shot.containers = (shots, updatable, drawable)

    while True:
            log_state()
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return
                
            screen.fill("black")
            updatable.update(dt)

            for asteroid in asteroids:
                if CircleShape.collides_with(player, asteroid):
                    log_event("player_hit")
                    print("Game Over!")
                    sys.exit()
                for shot in shots:
                    if CircleShape.collides_with(shot, asteroid):
                        log_event("asteroid_shot")
                        pygame.sprite.Sprite.kill(asteroid)
                        pygame.sprite.Sprite.kill(shot)
            for item in drawable:
                item.draw(screen)

            pygame.display.flip()

            dt = time.tick(60) / 1000
            
if __name__ == "__main__":
    main()
