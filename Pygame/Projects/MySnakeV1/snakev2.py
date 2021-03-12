import pygame 
from random import randrange

pygame.init()

RES = 600
SIZE = 25

win = pygame.display.set_mode((RES,RES+80))
pygame.display.set_caption('Snake')
back = pygame.image.load('tex/back.jpg')
font = pygame.font.Font('freesansbold.ttf', 32)
dir = {'W':True , 'S':True , 'A':True , 'D':True }


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
        if self.dx == 0 and self.dy == 0:
            (pygame.draw.circle(win, pygame.Color('green'), (self.x+SIZE / 2,self.y+SIZE / 2),12)) in self.snake[0]
        if self.dx == 1 and self.dy == 0:
            (pygame.draw.circle(win, pygame.Color('green'), (self.x  + SIZE  - SIZE / 20 ,self.y+SIZE / 2),12)) in self.snake[0]
        if self.dx == -1 and self.dy == 0:
            (pygame.draw.circle(win, pygame.Color('green'), (self.x-SIZE / 20,self.y+SIZE / 2),12)) in self.snake[0]
        if self.dx == 0 and self.dy == 1:
            (pygame.draw.circle(win, pygame.Color('green'), (self.x+SIZE / 2 ,self.y+SIZE),12)) in self.snake[0]
        if self.dx == 0 and self.dy == -1:
            (pygame.draw.circle(win, pygame.Color('green'), (self.x+SIZE / 2,self.y- SIZE / 20 ),12)) in self.snake[0]
        
        [(pygame.draw.rect(win, pygame.Color('green'), (i,j,SIZE  - 1,SIZE - 1 ))) for i,j in self.snake[1:]]
        win.blit(self.image, (self.apple))

 
        
    def gameover(self):
        global dir
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
            win.blit(back,(0,0))
            dir = {'W':True , 'S':True , 'A':True , 'D':True }
            
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
            win.blit(back,(0,0))
            dir = {'W':True , 'S':True , 'A':True , 'D':True }

    def eat(self):
        if self.snake[-1] == self.apple:
            self.apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
            self.leng +=1
            self.speed +=0.25


    def move(self,keys):
        global dir
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dir['A']:
                self.dx,self.dy = -1,0
                dir = {'W':True , 'S':True , 'A':True , 'D':False }
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dir['D']:
                self.dx,self.dy =  1,0
                dir = {'W':True , 'S':True , 'A':False , 'D':True }
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and dir['W']:
                self.dx,self.dy = 0,-1
                dir = {'W':True , 'S':False , 'A':True , 'D':True }
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dir['S']:
                self.dx,self.dy = 0, 1
                dir = {'W':False , 'S':True , 'A':True , 'D':True }

        
        
snake = Snake()
clock = pygame.time.Clock()
win.blit(back, (0, 0))


while snake.run:
    win.blit(back,(0,0))
    
    text = font.render(f'Score : {snake.leng}                             Best : {snake.best}', True, pygame.Color('white'))
    textRect = text.get_rect()
    textRect.center = (int(RES / 2 ), RES + 35)
    win.blit(text, textRect)
    clock.tick(snake.speed)
        
    snake.draw()
        
    pygame.display.flip()
    snake.eat()
    if snake.gameover():
        snake.leng = 1

    snake.x+=snake.dx * SIZE
    snake.y+=snake.dy * SIZE
    snake.snake.append((snake.x,snake.y))
    snake.snake = snake.snake[-snake.leng:]
    
    keys = pygame.key.get_pressed()
    snake.move(keys)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.run = False
    pygame.display.update()


        