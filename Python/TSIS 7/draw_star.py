import pygame
import math
pygame.init()

RESx,RESy = 600,400

win = pygame.display.set_mode((RESx,RESy))
pygame.display.set_caption("Cos and Sin")

run = True

pi = math.pi

def draw_star(n,rad, color, center):
    n *=2
    points = []
    for i in range(n):
        phi = pi * 2 / n * i
        r = rad if i % 2 == 0 else rad / 2

        x = r * math.sin(phi) + center[0]
        y = -r * math.cos(phi) + center[1]
        points.append((x,y))
    pygame.draw.polygon(win, color , points)

while run:
    win.fill((255,255,255))

    draw_star(1000,100, (255,255,0), (RESx / 2, RESy / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
        

    pygame.display.flip()