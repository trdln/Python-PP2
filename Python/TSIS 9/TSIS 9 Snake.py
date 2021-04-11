from tkinter.constants import TRUE
import pygame
import time
import random

 
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
 
snake_block = 30
snake_speed = 15
 
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
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(WIN, BLACK, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color,y = 100):
    mesg = font_style.render(msg, True, color)
    pos = mesg.get_rect(center=(RESx // 2, (RESy  + y - 100) // 2))
    WIN.blit(mesg, pos)
 
MAX_SCORE = 0

def gameLoop():
    global MAX_SCORE,back_menu
    move_rules = {'W':True , 'S':True , 'A':True , 'D':True }
    game_over = False
    lost = False
 
    x1 = RESx / 2
    y1 = RESy / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, RESx - snake_block) / 30.0) * 30.0
    foody = round(random.randrange(0, RESy - snake_block) / 30.0) * 30.0
    
    while not game_over:

        while lost:
            if MAX_SCORE < Length_of_snake - 1:
                MAX_SCORE = Length_of_snake - 1
            message("You Lost!", RED,0)
            message("R to restart",RED,80)
            message("Q to menu",RED,160)
            show_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        lost = False
                        back_menu = False
                    if event.key == pygame.K_r:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    lost = False

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and move_rules['A']:
                    x1_change = -snake_block
                    y1_change = 0
                    move_rules = {'W':True , 'S':True , 'A':True , 'D':False }
                elif event.key == pygame.K_RIGHT and move_rules['D']:
                    x1_change = snake_block
                    y1_change = 0
                    move_rules = {'W':True , 'S':True , 'A':False , 'D':True }
                elif event.key == pygame.K_UP and move_rules['W']:
                    y1_change = -snake_block
                    x1_change = 0
                    move_rules = {'W':True , 'S':False , 'A':True , 'D':True }
                elif event.key == pygame.K_DOWN and move_rules['S']:
                    y1_change = snake_block
                    x1_change = 0
                    move_rules = {'W':False , 'S':True , 'A':True , 'D':True }
                elif event.key == pygame.K_p:
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                                pause=False
            
        if x1 >= RESx  or x1 < 0 or y1 >= RESy  or y1 < 0:
            lost = True
        x1 += x1_change
        y1 += y1_change
        pygame.draw.rect(WIN,BLUE,[0,0,600,600])
        pygame.draw.rect(WIN,WHITE,[0,600,600,100])
        pygame.draw.rect(WIN, GREEN, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                lost = True
 
        our_snake(snake_block, snake_List)
        show_score(Length_of_snake - 1)
        show_high_score(MAX_SCORE)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, RESx - snake_block) / 30.0) * 30.0
            foody = round(random.randrange(0, RESy - snake_block) / 30.0) * 30.0
            Length_of_snake += 1
 
        FramePerSecond.tick(snake_speed)
 

menu = True

while menu:
    back_menu = True
    background = pygame.image.load("Materials/background.png")
    WIN.blit(background,(0,0))
    pygame.display.flip()
    while back_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    gameLoop()