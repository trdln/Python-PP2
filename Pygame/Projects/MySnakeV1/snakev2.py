import pygame 
from random import randrange

pygame.init()

RES = 600
SIZE = 25

win = pygame.display.set_mode((RES,RES+80))
pygame.display.set_caption('Snake')
back = pygame.image.load('tex/back.jpg')
font = pygame.font.Font('freesansbold.ttf', 32)

class Snake:
    def __init__(self):
        self.leng = 1
        self.x,self.y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)

        self.apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        self.image = pygame.image.load('tex/apple.png')

        
        self.w,self.h = SIZE,SIZE

        self.snake = [(self.x,self.y)]
        self.dx,self.dy = 0, 0

        self.speed = 10

        self.best = self.leng

        self.run = True

    def draw(self):
        [(pygame.draw.rect(win, pygame.Color('green'), (i,j,SIZE - 1 ,SIZE - 1))) for i,j in self.snake]
        win.blit(self.image, (self.apple))

 
        
    def gameover(self):
        if len(self.snake) != len(set(self.snake)):
            self.x , self.y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
            self.apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
            print(f'Score : {self.leng}')
            #max score system
            if self.leng > self.best:
                self.best = self.leng
            #reset settings of snake
            self.leng = 1
            self.speed = 10
            self.dx,self.dy = 0, 0
            
            
            
        if self.x < 0 or self.x > RES - SIZE or self.y < 0 or self.y > RES-SIZE:
            self.x,self.y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
            self.apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
            #max score system
            if self.leng > self.best:
                self.best = self.leng
            print(f'Score : {self.leng}')
            #reset settings of snake
            self.leng = 1
            self.speed = 10
            self.dx,self.dy = 0, 0

    def eat(self):
        if self.snake[-1] == self.apple:
            self.apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
            self.leng +=1
            self.speed +=0.5

        
snake = Snake()
clock = pygame.time.Clock()
win.blit(back, (0, 0))
dirs = {'W':True , 'S':True , 'A':True , 'D':True }
while snake.run:
    win.blit(back,(0,0))

    text = font.render(f'Score : {snake.leng}                             Best : {snake.best}', True, pygame.Color('white'))
    textRect = text.get_rect()
    textRect.center = (int(RES / 2 ), RES + 35)
    win.blit(text, textRect)
    clock.tick(snake.speed)
    snake.draw()
    snake.draw
    
    pygame.display.flip()
    snake.eat()
    if snake.gameover():
        dirs = {'W':True , 'S':True , 'A':True , 'D':True }
        snake.leng = 1

    snake.x+=snake.dx * SIZE
    snake.y+=snake.dy * SIZE
    snake.snake.append((snake.x,snake.y))
    snake.snake = snake.snake[-snake.leng:]

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dirs['A']:
        snake.dx,snake.dy = -1,0
        dirs = {'W':True , 'S':True , 'A':True , 'D':False }
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dirs['D']:
        snake.dx,snake.dy =  1,0
        dirs = {'W':True , 'S':True , 'A':False , 'D':True }
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dirs['W']:
        snake.dx,snake.dy = 0,-1
        dirs = {'W':True , 'S':False , 'A':True , 'D':True }
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dirs['S']:
        snake.dx,snake.dy = 0, 1
        dirs = {'W':False , 'S':True , 'A':True , 'D':True }

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.run = False
    pygame.display.update()

pygame.quit()

    