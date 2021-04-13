import pygame
import random

 
pygame.init()
 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
move_rules = {}
RESx = 600
RESy = 600
 
WIN = pygame.display.set_mode((RESx, RESy + 100))
pygame.display.set_caption('Snake')
 
FramePerSecond = pygame.time.Clock()
 
snake_block = 30
snake_speed = 12
 
font_style = pygame.font.Font("Materials/KA1.ttf", 30)
score_font = pygame.font.Font("Materials/KA1.ttf", 30)


def show_score(score):
    value = score_font.render(f"Score: {score}" , True, BLACK)
    pos = value.get_rect(center=(130,650))
    WIN.blit(value, pos)

def show_high_score(max_score):
    value = score_font.render(f"High Score: {max_score}" , True, BLACK)
    pos = value.get_rect(center=(420,650))
    WIN.blit(value, pos)

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x, self.y = RESx / 2, RESy / 2
        self.dx,self.dy = 0 , 0
        self.l = 1
        self.list = []
 
    def restart(self):
        self.x, self.y = RESx / 2, RESy / 2
        self.dx,self.dy = 0 , 0
        self.l = 1
        self.list = []

    def draw(self,snake_block, snake_list, colour):
        for x in snake_list:
            pygame.draw.rect(WIN, colour, [x[0], x[1], snake_block, snake_block])
            
    
    def move(self,keys):
        global move_rules
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and move_rules['A']:
                self.dx,self.dy = -snake_block, 0
                move_rules = {'W':True , 'S':True , 'A':True , 'D':False }
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and move_rules['D']:
                self.dx,self.dy =  snake_block, 0
                move_rules = {'W':True , 'S':True , 'A':False , 'D':True }
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and move_rules['W']:
                self.dx,self.dy = 0, -snake_block
                move_rules = {'W':True , 'S':False , 'A':True , 'D':True }
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and move_rules['S']:
                self.dx,self.dy = 0, snake_block
                move_rules = {'W':False , 'S':True , 'A':True , 'D':True }
        self.x += self.dx
        self.y +=self.dy

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = round(random.randrange(snake_block * 2, RESx - snake_block * 2) / float(snake_block)) * float(snake_block)
        self.y = round(random.randrange(snake_block * 2, RESy - snake_block * 2) / float(snake_block)) * float(snake_block)
    def draw(self):
        pygame.draw.rect(WIN, GREEN, [self.x, self.y, snake_block, snake_block])
    def restart(self):
        self.x = round(random.randrange(snake_block * 2, RESx - snake_block * 2) / float(snake_block)) * float(snake_block)
        self.y = round(random.randrange(snake_block * 2, RESy - snake_block * 2) / float(snake_block)) * float(snake_block)

class Walls(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x, self.y = x,y
        self.w, self.h = width , height
    def draw(self):
        pygame.draw.rect(WIN,RED, [self.x,self.y,self.w,self.h] )
        


def message(msg, color,y = 100):
    mesg = font_style.render(msg, True, color)
    pos = mesg.get_rect(center=(RESx // 2, (RESy  + y - 100) // 2))
    WIN.blit(mesg, pos)
 
#MAX_SCORE = int(open('h.txt','r').read()) #Global Highscore 
MAX_SCORE = 0 #Highscore of current session
menu = True
while menu:
    back_menu = True
    background = pygame.image.load("Materials/background.png")
    WIN.blit(background,(0,0))
    pygame.display.flip() 
    run = False
    while back_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                back_menu = False
                txt_i = open('h.txt','r').read()
                if int(txt_i) < MAX_SCORE:
                    txt_o = open('h.txt','w')
                    txt_o.write(str(MAX_SCORE))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run = True
                back_menu = False
                
    snake1 = Snake()
    food = Food()
    d_wall = Walls(0, RESy - snake_block , RESx , snake_block)
    r_wall = Walls(0,0,snake_block, RESy)
    l_wall = Walls(RESx - snake_block,0,snake_block,RESy)
    u_wall = Walls(0,0,RESx,snake_block)
    wl = pygame.sprite.Group()
    wl.add(u_wall)
    while run:
        move_rules = {'W':True , 'S':True , 'A':True , 'D':True }
        game_over = False
        lost = False
        snake_List = []
        while not game_over:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    txt_i = open('h.txt','r').read()
                    if int(txt_i) < MAX_SCORE:
                        txt_o = open('h.txt','w')
                        txt_o.write(str(MAX_SCORE))
                    game_over = True
                    back_menu = False
                    menu = False
                    run = False
                    menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = True
                        while pause:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                                    pause=False

            keys = pygame.key.get_pressed()
            snake1.move(keys)
            
            pygame.draw.rect(WIN,BLUE,[0,0,600,600])
            pygame.draw.rect(WIN,WHITE,[0,600,600,100])

            food.draw()

            snake1.draw(snake_block, snake_List , BLACK)
            snake_List.append((snake1.x,snake1.y))

            if snake1.x >= RESx - snake_block  or snake1.x < 0 + snake_block or snake1.y >= RESy - snake_block  or snake1.y < 0 + snake_block:
                lost = True
            if len(snake_List) > snake1.l:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == (snake1.x,snake1.y):
                    lost = True
    
            

            u_wall.draw()
            d_wall.draw()
            r_wall.draw()
            l_wall.draw()

            

            
            show_score(snake1.l - 1)
            show_high_score(MAX_SCORE)

            pygame.display.update()
            if snake1.x == food.x and snake1.y == food.y:
                food.restart()
                snake1.l += 1
                #Apple doesn't appear in Snake:
                for xy in snake_List:
                    if xy == (food.x,food.y):
                        food.restart()


            while lost:
                if MAX_SCORE < snake1.l - 1:
                    MAX_SCORE = snake1.l - 1
                message("You Lost!", RED,0)
                message("R to restart",RED,80)
                message("Q to menu",RED,160)
                show_score(snake1.l - 1)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            run = False
                            back_menu = True
                            lost = False
                        if event.key == pygame.K_r:
                            snake1.restart()
                            food.restart()
                            game_over = True
                            run = True
                            lost = False
                    if event.type == pygame.QUIT:
                        txt_i = open('h.txt','r').read()
                        if int(txt_i) < MAX_SCORE:
                            txt_o = open('h.txt','w')
                            txt_o.write(str(MAX_SCORE))
                        game_over = True
                        back_menu = False
                        run = False
                        menu = False
                        lost = False
                        
            FramePerSecond.tick(snake_speed)