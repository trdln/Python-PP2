import pygame
import random
import time
import pickle

pygame.init()
 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
RESx = 600
RESy = 600
 
WIN = pygame.display.set_mode((RESx, RESy + 100))
pygame.display.set_caption('Snake')
 
FramePerSecond = pygame.time.Clock()
 
snake_block = 25
snake_speed = 10
 
font_style = pygame.font.Font("Materials/KA1.ttf", 30)
score_font = pygame.font.Font("Materials/KA1.ttf", 30)


def show_score(score,name,y):
    value = score_font.render(f"Score {name}: {score}" , True, BLACK)
    pos = value.get_rect(center=(130,630 + y))
    WIN.blit(value, pos)

def show_high_score(max_score):
    value = score_font.render(f"High Score: {max_score}" , True, BLACK)
    pos = value.get_rect(center=(420,650))
    WIN.blit(value, pos)

class Snake(pygame.sprite.Sprite):
    def __init__(self,coordinates):
        super().__init__()
        self.crd = coordinates
        self.x, self.y = map(int, self.crd)
        self.dx,self.dy = 0 , 0
        self.l = 1
        self.list = []
 
    def restart(self):
        self.x, self.y = map(int, self.crd)
        self.dx,self.dy = 0 , 0
        self.l = 1
        self.list = []

    def draw(self,snake_block, snake_list, colour):
        for x in snake_list:
            pygame.draw.rect(WIN, colour, [x[0], x[1], snake_block, snake_block])
            
    
    def move1(self,keys,buttons):
        global move_rules1
        if (keys[buttons["A"]]) and move_rules1['A']:
                self.dx,self.dy = -snake_block, 0
                move_rules1 = {'W':True , 'S':True , 'A':True , 'D':False }
        if (keys[buttons["D"]]) and move_rules1['D']:
                self.dx,self.dy =  snake_block, 0
                move_rules1 = {'W':True , 'S':True , 'A':False , 'D':True }
        if (keys[buttons["W"]]) and move_rules1['W']:
                self.dx,self.dy = 0, -snake_block
                move_rules1 = {'W':True , 'S':False , 'A':True , 'D':True }
        if (keys[buttons["S"]]) and move_rules1['S']:
                self.dx,self.dy = 0, snake_block 
                move_rules1 = {'W':False , 'S':True , 'A':True , 'D':True }
        self.x += self.dx
        self.y += self.dy
    def move2(self,keys,buttons):
        global move_rules2
        if (keys[buttons["A"]]) and move_rules2['A']:
                self.dx,self.dy = -snake_block, 0
                move_rules2 = {'W':True , 'S':True , 'A':True , 'D':False }
        if (keys[buttons["D"]]) and move_rules2['D']:
                self.dx,self.dy =  snake_block, 0
                move_rules2 = {'W':True , 'S':True , 'A':False , 'D':True }
        if (keys[buttons["W"]]) and move_rules2['W']:
                self.dx,self.dy = 0, -snake_block
                move_rules2 = {'W':True , 'S':False , 'A':True , 'D':True }
        if (keys[buttons["S"]]) and move_rules2['S']:
                self.dx,self.dy = 0, snake_block 
                move_rules2 = {'W':False , 'S':True , 'A':True , 'D':True }
        self.x += self.dx
        self.y += self.dy

def check_walls(snake_x,snake_y,level_counter,list):
    global lost
    if level_counter == 0:
        if snake_x >= RESx or snake_x < 0 or snake_y >= RESy or snake_y < 0:
            lost = True
    for i in list:
        if i[0] == snake_x and i[1] == snake_y:
            lost = True
        

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
def check_eat(player, food, snake_list, wall_list):
    if player.x == food.x and player.y == food.y:
        food.restart()
        player.l += 1
        #Apple doesn't appear in Snake:
    for xy in snake_list:
        if xy == (food.x,food.y):
            food.restart()
    for xy in wall_list:
        if xy == (food.x,food.y):
            food.restart()

def check_itself(snake_list,snake_x ,snake_y):
    global lost
    for x in snake_list[:-1]:
        if x == (snake_x,snake_y):
            lost = True
def check_two_snakes(snake_list1,snake_list2):
    global lost
    for i in snake_list1:
        for j in snake_list2:
            if i == j:
                lost = True

def check_length(snake_list , snake_l):
    if len(snake_list) > snake_l:
        del snake_list[0]

def restart_all_class(snake1,snake2,food):
    global game_over,run
    snake1.restart()
    snake2.restart()
    food.restart()
    game_over = True
    run = True
class Walls(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.w, self.h = width , height
        self.list = []
        self.image = pygame.image.load("Materials/wall.png")
        
def message(msg, color,y = 100):
    mesg = font_style.render(msg, True, color)
    pos = mesg.get_rect(center=(RESx // 2, (RESy  + y - 100) // 2))
    WIN.blit(mesg, pos)
 
#MAX_SCORE = int(open('h.txt','r').read()) #Global Highscore 
MAX_SCORE = 0 #Highscore of current session
menu = True
upgrade_cnt = 15
level_counter = 0
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
                
    snake1 = Snake((RESx/2 + 2 * snake_block,RESy/2))
    snake2 = Snake((RESx/2 - 3 * snake_block,RESy/2))
    food = Food()
    wall = Walls(snake_block , snake_block)
    level_names = ["lvl1.txt","lvl2.txt","lvl3.txt","lvl4.txt","lvl5.txt"]
    walls_point = []
    while run:
        move_rules1 = {'W':True , 'S':True , 'A':True , 'D':True }
        move_rules2 = {'W':True , 'S':True , 'A':True , 'D':True }
        game_over = False
        lost = False
        snake_List1 = []
        snake_List2 = []
        walls_point = []
        time.sleep(1)
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
            buttons1 = {"A" : pygame.K_a , "D" : pygame.K_d, "W" : pygame.K_w , "S" : pygame.K_s}
            buttons2 = {"A" : pygame.K_LEFT , "D" : pygame.K_RIGHT, "W" : pygame.K_UP , "S" : pygame.K_DOWN}
            snake1.move1(keys,buttons1)
            snake2.move2(keys,buttons2)
            
            pygame.draw.rect(WIN,BLUE,[0,0,600,600])
            pygame.draw.rect(WIN,WHITE,[0,600,600,100])

            food.draw()
            snake1.draw(snake_block, snake_List1 , BLACK)
            snake2.draw(snake_block, snake_List2 , WHITE)
            snake_List1.append((snake1.x,snake1.y))
            snake_List2.append((snake2.x,snake2.y))

            check_length(snake_List1,snake1.l)
            check_length(snake_List2,snake2.l)

            check_itself(snake_List1,snake1.x,snake1.y)
            check_itself(snake_List2,snake2.x,snake2.y)
            
            check_two_snakes(snake_List1,snake_List2)

            #if snake1.l + upgrade_cnt * level_counter > upgrade_cnt * (level_counter + 1) or snake2.l + upgrade_cnt * level_counter > upgrade_cnt * (level_counter + 1):
            if snake1.l  - 1 + upgrade_cnt * level_counter > upgrade_cnt * (level_counter + 1) or snake2.l - 1+ upgrade_cnt * level_counter > upgrade_cnt * (level_counter + 1):
                level_counter += 1
                restart_all_class(snake1,snake2,food)

            file = open(level_names[level_counter],'r').readlines()
            for i in range(len(file)):
                for j in range(len(file[i])):
                    if file[i][j] == "#":
                        #pygame.draw.rect(WIN,RED, [j * snake_block,i * snake_block,snake_block,snake_block])
                        WIN.blit(wall.image , (j * snake_block,i * snake_block))
                        walls_point.append((j * snake_block,i * snake_block))

            check_walls(snake1.x,snake1.y,level_counter,walls_point)
            check_walls(snake2.x,snake2.y,level_counter,walls_point)
            
            show_score(snake1.l - 1, "P1" , 0)
            show_score(snake2.l - 1, "P2" , 40)

            show_high_score(MAX_SCORE)

            
            check_eat(snake1, food, snake_List1,walls_point)
            check_eat(snake2, food, snake_List2,walls_point)

            pygame.display.flip()
            while lost:
                if MAX_SCORE < snake1.l - 1 + upgrade_cnt * level_counter:
                    MAX_SCORE = snake1.l - 1 + upgrade_cnt * level_counter
                if MAX_SCORE < snake2.l - 1 + upgrade_cnt * level_counter: 
                    MAX_SCORE = snake2.l - 1 + upgrade_cnt * level_counter
                message("You Lost!", RED,0)
                message("R to restart",RED,80)
                message("Q to menu",RED,160)
                show_score(snake1.l - 1,"P1" , 0)
                show_score(snake2.l - 1,"P2" , 40)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            run = False
                            back_menu = True
                            lost = False
                        if event.key == pygame.K_r:
                            walls_point = []
                            level_counter = 0
                            file = ""
                            restart_all_class(snake1,snake2,food)
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