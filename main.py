import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():

    print("Starting asteroids!")
    print(f"Screen width: { SCREEN_WIDTH }")
    print( SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers= (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable :
            obj.update(dt)

        screen.fill("black")

        for obj in drawable :
            obj.draw(screen)

        for ass in asteroids :
            if ass.check_collisions(player):
                print("Game over!")
                sys.exit()
            for shot in shots :
                if ass.check_collisions(shot):
                    ass.split()
                    shot.kill()



        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":

    main()
