# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatables, drawables,shots)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfields = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}") 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable in updatables:
            updatable.update(dt)
            
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over")
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if(asteroid.check_collision(shot)):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        dt = clock.tick(60) /1000
        

if __name__ == "__main__":
        main()