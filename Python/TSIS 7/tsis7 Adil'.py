import pygame as pg 
from math import sin, cos, radians, pi, ceil
pg.init()
RESx,RESy = 850,605
screen = pg.display.set_mode((850, 605))
pg.display.set_caption("sin and cos")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


def draw_lines(screen):
    # внешняя рамка
    pg.draw.rect(screen, black, [50, 15, 780, 540], 2)
    # линии
    for i in range(80, 831, 120):
        if i == 440:
            pg.draw.line(screen, black, [i, 15], [i, 555], 2)
        elif i == 560:
            pg.draw.line(screen, black, [i, 15], [i, 45], 1)
            pg.draw.line(screen, black, [i, 105], [i, 555], 1)
        else:
            pg.draw.line(screen, black, [i, 15], [i, 555], 1)
    for i in range(45, 556, 60):
        if i == 285:
            pg.draw.line(screen, black, [50, i], [830, i], 2)
        else:
            pg.draw.line(screen, black, [50, i], [830, i], 1)

def little_lines(screen):
    # маленькие штрихи по x
    for i in range(95, 786, 30):
        pg.draw.line(screen, black, [i, 15], [i, 20], 1)
        pg.draw.line(screen, black, [i, 550], [i, 555], 1)
    for i in range(110, 771, 60):
        pg.draw.line(screen, black, [i, 15], [i, 25], 1)
        pg.draw.line(screen, black, [i, 545], [i, 555], 1)
    for i in range(140, 741, 120):
        pg.draw.line(screen, black, [i, 15], [i, 30], 1)
        pg.draw.line(screen, black, [i, 540], [i, 555], 1)
    # маленькие штрихи по y
    for i in range(60, 511, 30):
        pg.draw.line(screen, black, [50, i], [55, i], 1)
        pg.draw.line(screen, black, [825, i], [830, i], 1)
    for i in range(75, 496, 60):
        pg.draw.line(screen, black, [50, i], [60, i], 1)
        pg.draw.line(screen, black, [820, i], [830, i], 1)



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(white)

    draw_lines(screen)
    little_lines(screen)

    pg.display.update()
pg.quit()
    

