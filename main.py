import sys
import pygame
from constants import *
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = (game_clock.tick(60))/1000
        
        


        

if __name__ == "__main__":
    main()
