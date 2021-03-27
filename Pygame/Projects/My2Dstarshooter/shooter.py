import pygame

pygame.init()

RESx = 900
RESy = 600
SIZE = "SIZE OF STARSHIP"

win = pygame.display.set_mode((RESx,RESy))
pygame.display.set_option('Star Wars')
bg = 'BACKROUND'
person = "PERSON"
enemy = "ENEMY"

class hero:
    def __init__(self):
        self.x , self.y = RESx / 2 , RESy * 0.75
