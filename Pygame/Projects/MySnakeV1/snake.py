import pygame
from random import randrange
#размер окна, размер каждого блока
RES = 600
SIZE = 25
#!!! то что нужно исправить: яблоко спавнется внутри змейки если змейка длинная, змейка с нижней сначала выходит на SIZE и толко потом заканчивается игра


# Первое это рандомная точка спавна для змейки, а второе рандомная точка спавна для яблока
x,y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
# Это словарь для предотвращения невозможных движений
dirs = {'W':True , 'S':True , 'A':True , 'D':True }
# Размеры яблок и каждого блока змейки
w,h = 20,20

# Начальная длина, сам массив который является змейкой, две кординаты движения, и скорость
length = 1
snake = [(x,y)]
dx,dy = 0, 0
speed = 10
# Иницилизация, название для окна, создаем окно, и даем счетчик обновления кадров для изменения скорости
pygame.init()
pygame.display.set_caption("Snake")
win = pygame.display.set_mode((RES,RES+70)) # +70 for score information
clock = pygame.time.Clock()

# создаем переменную для шрифта
font = pygame.font.Font('freesansbold.ttf', 32)

# фунция для того чтобы рисовать линии
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0, y),(w,y))
# Переменная с лучшим результатом, переменная для бесконечного цикла, и сам цикл
best = 1
run = True
while run:
    # заполняем или же красим окно для того чтобы пред кадр пропадал
    win.fill(pygame.Color('black'))
    #рисуем змейку
    [(pygame.draw.rect(win, pygame.Color('green'), (i,j,SIZE - 1 ,SIZE - 1))) for i,j in snake]
    #рисуем яблоко
    pygame.draw.rect(win,pygame.Color('red'),(*apple,SIZE,SIZE))
    #рисуем линии
    drawGrid(RES,int(RES / SIZE), win)
    #четыре строки для текста в окне
    text = font.render(f'Score : {length}    Best : {best}', True, pygame.Color('white'))
    textRect = text.get_rect()
    textRect.center = (int(RES / 2), RES + 35)
    #значение кадров для скорости
    clock.tick(speed)
    #пишем сам текст в окне
    win.blit(text, textRect)

    
    #движение змейки зависит от его размеров и скорости по осям
    x+=dx * SIZE
    y+=dy * SIZE

    #????
    snake.append((x,y))
    snake = snake[-length:]

    # Когда змейка кушает яблоко, длина увеличивается, а также скорость для интереса
    if snake[-1] == apple:
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        length +=1
        speed +=0.5
    
    #первый случай когда игра заканчивается (когда змейка косается границ зоны)
    if x < 0 or x > RES - SIZE or y < 0 or y > RES-SIZE:
        x,y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        #max score system
        if length> best:
            best = length

        #reset settings of snake
        length = 1
        speed = 10
        dx,dy = 0, 0
        dirs = {'W':True , 'S':True , 'A':True , 'D':True }
    #второй случай когда змейка сопрекасается с собой
    if len(snake) != len(set(snake)):
        x,y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        #max score system
        if length> best:
            best = length

        #reset settings of snake

        length = 1
        speed = 10
        dx,dy = 0, 0
        dirs = {'W':True , 'S':True , 'A':True , 'D':True }
    #массив в который вписываются все наши нажатия 
    keys = pygame.key.get_pressed()

    #чтобы закрыть окно
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #механика движения
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dirs['A']:
        dx,dy = -1,0
        dirs = {'W':True , 'S':True , 'A':True , 'D':False }
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dirs['D']:
        dx,dy =  1,0
        dirs = {'W':True , 'S':True , 'A':False , 'D':True }
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dirs['W']:
        dx,dy = 0,-1
        dirs = {'W':True , 'S':False , 'A':True , 'D':True }
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dirs['S']:
        dx,dy = 0, 1
        dirs = {'W':False , 'S':True , 'A':True , 'D':True }
    #все изменения обновляются и показываются на экран
    pygame.display.update()

#это чтобы окончательно закрыть программу
pygame.quit()