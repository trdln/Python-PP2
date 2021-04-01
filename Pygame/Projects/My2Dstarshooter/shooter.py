from os import pathsep
from random import randrange
import pygame

pygame.init()

RESx = 600
RESy = 800
SIZE = (90, 100)

win = pygame.display.set_mode((RESx, RESy))
pygame.display.set_caption('Star Wars')

bg = pygame.image.load('tex/back.png')
ship = pygame.image.load('tex/ship.png')
asteroid = pygame.image.load('tex/asteroid.png')
bullet = pygame.image.load('tex/bullet.png')


clock = pygame.time.Clock()


class Starship:
    def __init__(self):
        self.x, self.y = RESx / 2 - SIZE[0] / 2, RESy * 0.75

    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.x -= 10
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.x += 10

    def gra(self):
        if self.x < 0:
            self.x = 0
        if self.x > RESx - SIZE[0]:
            self.x = RESx - SIZE[0]


class Bullet:
    def __init__(self):
        self.fly = False

    def draw(self, sx, sy):
        self.x, self.y = sx + SIZE[0] / 2 - 5, sy - 10
        if self.fly and sy >= 0:
            win.blit(bullet, (self.x, self.y))
        else:
            self.fly = False
            sy = Starship().y


class Asteroid:
    def __init__(self):
        self.y = 0 + SIZE[0]
        self.cnt = 0

    def draw(self):
        if not self.y > RESy * 0.85:
            if self.cnt < 5:
                self.x = randrange(0 + SIZE[0], RESx - SIZE[0])
                win.blit(asteroid, (self.x, self.y))
                self.cnt += 1
        else:
            self.cnt -= 1


run = True
starship = Starship()
ast = Asteroid()
bul = Bullet()


while run:
    win.blit(bg, (0, 0))
    clock.tick(30)

    win.blit(ship, (starship.x, starship.y))

    ast.draw()
    ast.y += 10

    keys = pygame.key.get_pressed()

    starship.move(keys)
    starship.gra()

    if keys[pygame.K_w]:
        bul.fly = True
    sy = starship.y

    bul.draw(starship.x, sy)
    sy -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
