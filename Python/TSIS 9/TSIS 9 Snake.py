import pygame,random,time,pickle

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

FILE_NAME_SNAKES = 'save/snakes_saved.data'

font_style = pygame.font.Font("Materials/KA1.ttf", 30)
score_font = pygame.font.Font("Materials/KA1.ttf", 30)

grass = pygame.image.load('Materials/lvl1.png')
bar = pygame.image.load('Materials/bar.png')
music = pygame.mixer.Sound('Materials/music.mp3')
green_snake = {"up_right" : pygame.image.load("Materials/rd.png"),
'up_left' : pygame.image.load("Materials/dl.png"),
'down_right' : pygame.image.load("Materials/ur.png"),
'down_left' : pygame.image.load("Materials/ul.png"),
'b_hor' : pygame.image.load("Materials/b_hor.png"),
'b_ver' : pygame.image.load("Materials/b_ver.png"),
'h_hor_l' : pygame.image.load("Materials/h_hor.png"),
'h_hor_r' : pygame.image.load("Materials/h_hor_r.png"),
'h_ver_d' : pygame.image.load("Materials/h_ver_d.png"),
'h_ver_u' : pygame.image.load("Materials/h_ver_u.png"),
'head_r' : pygame.image.load("Materials/head_r.png"),
'head_l' : pygame.image.load("Materials/head_l.png"),
'head_d' : pygame.image.load("Materials/head_d.png"),
'head_u' : pygame.image.load("Materials/head_u.png")}
yellow_snake = {"up_right" : pygame.image.load("Materials/yur.png"),
'up_left' : pygame.image.load("Materials/yul.png"),
'down_right' : pygame.image.load("Materials/ydr.png"),
'down_left' : pygame.image.load("Materials/ydl.png"),
'b_hor' : pygame.image.load("Materials/y_hor.png"),
'b_ver' : pygame.image.load("Materials/y_ver.png"),
'h_hor_l' : pygame.image.load("Materials/y_hor_l.png"),
'h_hor_r' : pygame.image.load("Materials/y_hor_r.png"),
'h_ver_d' : pygame.image.load("Materials/y_ver_d.png"),
'h_ver_u' : pygame.image.load("Materials/y_ver_u.png"),
'head_r' : pygame.image.load("Materials/head_yr.png"),
'head_l' : pygame.image.load("Materials/head_yl.png"),
'head_d' : pygame.image.load("Materials/head_yd.png"),
'head_u' : pygame.image.load("Materials/head_yu.png")}
def show_score(score,name,y):
    value = score_font.render(f"Score {name}: {score}" , True, YELLOW)
    pos = value.get_rect(center=(140,630 + y))
    WIN.blit(value, pos)
def show_high_score(max_score):
    value = score_font.render(f"High Score: {max_score}" , True, YELLOW)
    pos = value.get_rect(center=(430,650))
    WIN.blit(value, pos)
def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill(YELLOW)
    fade.set_alpha(5)
    WIN.blit(fade, (0,0))       
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
    def draw(self,snake_block, snake_list,snake_sprites):
        #Голова - не до конца корректная
        if self.dx == snake_block and self.dy == 0:
            WIN.blit(snake_sprites['head_r'] , (self.x - snake_block, self.y))
        if self.dx == -snake_block and self.dy == 0:
            WIN.blit(snake_sprites['head_l'] , (self.x + snake_block, self.y))
        if self.dx == 0 and self.dy == snake_block:
            WIN.blit(snake_sprites['head_d'], (self.x - 1 , self.y - snake_block))
        if self.dx == 0 and self.dy == -snake_block:
            WIN.blit(snake_sprites['head_u'] , (self.x - 1 , self.y + snake_block))
        if (self.dx == 0 and self.dy == 0):
            WIN.blit(snake_sprites['head_u'] , (self.x - 1 , self.y))
        l = len(snake_list) - 1
        for i in range(1,l):
            #1 Изгибы
            if snake_list[i][0] == snake_list[i+1][0] - snake_block and snake_list[i][1] == snake_list[i + 1][1]:
                if snake_list[i][0] == snake_list[i-1][0] and snake_list[i][1] == snake_list[i - 1][1] + snake_block:
                    WIN.blit(snake_sprites['down_right'] , (snake_list[i][0], snake_list[i][1]))
            #2
            if snake_list[i][0] == snake_list[i-1][0] - snake_block and snake_list[i][1] == snake_list[i - 1][1]:
                if snake_list[i][0] == snake_list[i+1][0] and snake_list[i][1] == snake_list[i + 1][1] + snake_block:
                    WIN.blit(snake_sprites['down_right'] , (snake_list[i][0], snake_list[i][1]))
            #3
            if snake_list[i + 1][0] == snake_list[i][0] - snake_block and snake_list[i + 1][1] == snake_list[i][1]:
                if snake_list[i-1][0] == snake_list[i][0] and snake_list[i - 1][1] == snake_list[i][1] + snake_block:
                    WIN.blit(snake_sprites['up_left'] , (snake_list[i][0], snake_list[i][1]))
            #4
            if snake_list[i - 1][0] == snake_list[i][0] - snake_block and snake_list[i - 1][1] == snake_list[i ][1]:
                if snake_list[i + 1][0] == snake_list[i][0] and snake_list[i + 1][1] == snake_list[i ][1] + snake_block:
                    WIN.blit(snake_sprites['up_left'] , (snake_list[i][0], snake_list[i][1]))
            #5
            if snake_list[i][0] == snake_list[i+1][0] + snake_block and snake_list[i][1] == snake_list[i + 1][1]:
                if snake_list[i][0] == snake_list[i-1][0] and snake_list[i][1] == snake_list[i - 1][1] + snake_block:
                    WIN.blit(snake_sprites['down_left'] , (snake_list[i][0], snake_list[i][1]))
            #6
            if snake_list[i][0] == snake_list[i - 1][0] + snake_block and snake_list[i][1] == snake_list[i - 1][1]:
                if snake_list[i][0] == snake_list[i+1][0] and snake_list[i][1] == snake_list[i + 1][1] + snake_block:
                    WIN.blit(snake_sprites['down_left'] , (snake_list[i][0], snake_list[i][1]))
            #7
            if snake_list[i][0] == snake_list[i+1][0] and snake_list[i][1] == snake_list[i + 1][1] - snake_block:
                if snake_list[i][0] == snake_list[i-1][0] - snake_block and snake_list[i][1] == snake_list[i - 1][1]:
                    WIN.blit(snake_sprites['up_right'] , (snake_list[i][0], snake_list[i][1]))
            #8
            if snake_list[i][0] == snake_list[i - 1][0] and snake_list[i][1] == snake_list[i - 1][1] - snake_block:
                if snake_list[i][0] == snake_list[i + 1][0] - snake_block and snake_list[i][1] == snake_list[i + 1][1]:
                    WIN.blit(snake_sprites['up_right'] , (snake_list[i][0], snake_list[i][1]))          
            #Hor тело
            if snake_list[i][0] == snake_list[i + 1][0] + snake_block and snake_list[i][1] == snake_list[i + 1][1]:
                if not (snake_list[i][0] == snake_list[i-1][0] and snake_list[i][1] == snake_list[i - 1][1] + snake_block):
                    if not(snake_list[i-1][0] == snake_list[i][0] and snake_list[i - 1][1] == snake_list[i][1] + snake_block): 
                        WIN.blit(snake_sprites['b_hor'] , (snake_list[i][0], snake_list[i][1]))
            if snake_list[i][0] == snake_list[i + 1][0] - snake_block and snake_list[i][1] == snake_list[i + 1][1]:
                if not (snake_list[i][0] == snake_list[i-1][0] and snake_list[i][1] == snake_list[i - 1][1] - snake_block):
                    if not(snake_list[i-1][0] == snake_list[i][0] and snake_list[i - 1][1] == snake_list[i][1] - snake_block): 
                        WIN.blit(snake_sprites['b_hor'] , (snake_list[i][0], snake_list[i][1]))
            #Ver тело
            if snake_list[i][0] == snake_list[i + 1][0] and snake_list[i][1] == snake_list[i + 1][1] + snake_block:
                if not(snake_list[i][0] == snake_list[i-1][0] - snake_block and snake_list[i][1] == snake_list[i - 1][1]):
                    if not(snake_list[i-1][0] == snake_list[i][0] - snake_block and snake_list[i-1][1] == snake_list[i][1]):
                        WIN.blit(snake_sprites['b_ver'], (snake_list[i][0], snake_list[i][1]))
            if snake_list[i][0] == snake_list[i + 1][0] and snake_list[i][1] == snake_list[i + 1][1] - snake_block:
                if not(snake_list[i][0] == snake_list[i-1][0] + snake_block and snake_list[i][1] == snake_list[i - 1][1]):
                    if not(snake_list[i-1][0] == snake_list[i][0] + snake_block and snake_list[i-1][1] == snake_list[i][1]):
                        WIN.blit(snake_sprites['b_ver'] , (snake_list[i][0], snake_list[i][1]))
            #Хвост
            if snake_list[0][0] == snake_list[1][0] - snake_block and snake_list[0][1] == snake_list[1][1]:
                WIN.blit(snake_sprites['h_hor_r'] , (snake_list[0][0], snake_list[0][1]))
            if snake_list[0][0] == snake_list[1][0] + snake_block and snake_list[0][1] == snake_list[1][1]:
                WIN.blit(snake_sprites['h_hor_l'] , (snake_list[0][0], snake_list[0][1]))
            if snake_list[0][0] == snake_list[1][0] and snake_list[0][1] == snake_list[1][1] + snake_block:
                WIN.blit(snake_sprites['h_ver_u'], (snake_list[0][0], snake_list[0][1]))
            if snake_list[0][0] == snake_list[1][0] and snake_list[0][1] == snake_list[1][1] - snake_block:
                WIN.blit(snake_sprites['h_ver_d'] , (snake_list[0][0], snake_list[0][1]))
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
        if 0 - snake_block > self.x or self.x > RESx:
            self.x = self.x % RESx
        if 0 - snake_block > self.y or self.y > RESx:
            self.y = self.y % RESy

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
        if 0 - snake_block > self.x or self.x > RESx:
            self.x = self.x % RESx
        if 0 - snake_block > self.y or self.y > RESx:
            self.y = self.y % RESy
def check_walls(snake_x,snake_y,level_counter,list):
    global lost
    if level_counter == 0:
        if snake_x >= RESx or snake_x < 0 or snake_y >= RESy or snake_y < 0:
            #lost = True
            pass
    for i in list:
        if i[0] == snake_x and i[1] == snake_y:
            lost = True
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = round(random.randrange(snake_block * 2, RESx - snake_block * 2) / float(snake_block)) * float(snake_block)
        self.y = round(random.randrange(snake_block * 2, RESy - snake_block * 2) / float(snake_block)) * float(snake_block)
        self.pos = (self.x,self.y)
        self.image = pygame.image.load("Materials/apple.png")
    def draw(self):
        #pygame.draw.rect(WIN, GREEN, [self.x, self.y, snake_block, snake_block])
        WIN.blit(self.image,(self.x, self.y))
    def restart(self):
        self.x = round(random.randrange(snake_block * 2, RESx - snake_block * 2) / float(snake_block)) * float(snake_block)
        self.y = round(random.randrange(snake_block * 2, RESy - snake_block * 2) / float(snake_block)) * float(snake_block)
        self.pos = (self.x,self.y)
def check_eat(player, food, snake_list, wall_list):
    if player.x == food.x and player.y == food.y:
        food.restart()
        player.l += 1
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
def check_two_foods(food1,food2):
    if food1.x == food2.x and food1.y == food2.y:
        food1.restart()
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
#MAX_SCORE = int(open('Levels/h.txt','r').read()) #Global Highscore 
MAX_SCORE = 0 #Highscore of current session
menu = True
upgrade_cnt = 15
game_speed = 10
level_counter = 0
dif = 2
dif_made = False
while menu:
    music.play(-1)
    background = pygame.image.load("Materials/background.png")
    WIN.blit(background,(0,0))
    pygame.display.flip() 
    run = True
    back_menu = True
    cmd_restart = True
    snakes = []
    while back_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                back_menu = False
                txt_i = open('Levels/h.txt','r').read()
                if int(txt_i) < MAX_SCORE:
                    txt_o = open('Levels/h.txt','w')
                    txt_o.write(str(MAX_SCORE))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    back_menu = False
                    cmd_restart = True
                if event.key == pygame.K_e:
                    try:
                        with open(FILE_NAME_SNAKES, 'br') as f:
                            snakes = pickle.load(f)
                        cmd_restart = False
                        dif_made = True
                    except Exception as e:
                        cmd_restart = True
                    run = True
                    back_menu = False
                if event.key == pygame.K_1:
                    dif = 1
                    dif_made = True
                if event.key == pygame.K_2:
                    dif = 2
                    dif_made = True
                if event.key == pygame.K_3:
                    dif = 3
                    dif_made = True
    if cmd_restart:        
        snake1 = Snake((RESx/2 + 2 * snake_block,RESy/2 - snake_block))
        snake2 = Snake((RESx/2 - 3 * snake_block,RESy/2 - snake_block))
        level_counter = 0
    else:
        snake1 = snakes[0]
        snake2 = snakes[1]
        level_counter = snakes[4]
        dif = snakes[5]
    if not dif_made:
        dif = 2
    wall = Walls(snake_block , snake_block)
    level_names = ["Levels/lvl1.txt","Levels/lvl2.txt","Levels/lvl3.txt","Levels/lvl4.txt","Levels/lvl5.txt"]
    walls_point = []
    collision_of_snakes = False
    two_apples = False
    if dif == 1:
        upgrade_cnt = 8
        game_speed = 8
    if dif == 2:
        upgrade_cnt = 20
        game_speed = 12
    if dif == 3:
        upgrade_cnt = 30
        game_speed = 14
        collision_of_snakes = True
        two_apples = True
    if two_apples:
        food = Food()
        food2 = Food()
    else:
        food = Food()
    while run:
        move_rules1 = {'W':True , 'S':True , 'A':True , 'D':True }
        move_rules2 = {'W':True , 'S':True , 'A':True , 'D':True }
        game_over = False
        lost = False
        walls_point = []
        time.sleep(1)
        if cmd_restart:
            snake_List1 = []
            snake_List2 = []
        else:
            snake_List1 = snakes[2]
            snake_List2 = snakes[3]
        while not game_over:

            keys = pygame.key.get_pressed()
            buttons1 = {"A" : pygame.K_a , "D" : pygame.K_d, "W" : pygame.K_w , "S" : pygame.K_s}
            buttons2 = {"A" : pygame.K_LEFT , "D" : pygame.K_RIGHT, "W" : pygame.K_UP , "S" : pygame.K_DOWN}
            snake1.move1(keys,buttons1)
            snake2.move2(keys,buttons2)
            
            WIN.blit(grass,(0,0))
            WIN.blit(bar,(0,600))
            
            snake1.draw(snake_block, snake_List1,green_snake)
            snake2.draw(snake_block, snake_List2,yellow_snake)
            snake_List1.append((snake1.x,snake1.y))
            snake_List2.append((snake2.x,snake2.y))

            check_length(snake_List1,snake1.l)
            check_length(snake_List2,snake2.l)

            check_itself(snake_List1,snake1.x,snake1.y)
            check_itself(snake_List2,snake2.x,snake2.y)
            
            if collision_of_snakes:
                check_two_snakes(snake_List1,snake_List2)

            if snake1.l  - 1 + upgrade_cnt * level_counter > upgrade_cnt * (level_counter + 1) or snake2.l - 1+ upgrade_cnt * level_counter > upgrade_cnt * (level_counter + 1):
                level_counter += 1
                cmd_restart = True
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

            if two_apples:
                check_two_foods(food,food2)
                food.draw()
                check_eat(snake1, food, snake_List1,walls_point)
                check_eat(snake2, food, snake_List2,walls_point)
                food2.draw()
                check_eat(snake1, food2, snake_List1,walls_point)
                check_eat(snake2, food2, snake_List2,walls_point)
            else:
                food.draw()
                check_eat(snake1, food, snake_List1,walls_point)
                check_eat(snake2, food, snake_List2,walls_point)

            if level_counter > len(level_names):
                lost = True
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    txt_i = open('Levels/h.txt','r').read()
                    if int(txt_i) < MAX_SCORE:
                        txt_o = open('Levels/h.txt','w')
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
                    if event.key == pygame.K_ESCAPE:
                        snakes = [snake1, snake2 , snake_List1,snake_List2,level_counter,dif]
                        with open(FILE_NAME_SNAKES, 'bw') as f:
                            pickle.dump(snakes, f)
                        '''
                        game_over = True
                        back_menu = False
                        menu = False
                        run = False
                        menu = False
                        '''
            while lost:
                fade(600,700)
                if MAX_SCORE < snake1.l - 1 + upgrade_cnt * level_counter:
                    MAX_SCORE = snake1.l - 1 + upgrade_cnt * level_counter
                if MAX_SCORE < snake2.l - 1 + upgrade_cnt * level_counter: 
                    MAX_SCORE = snake2.l - 1 + upgrade_cnt * level_counter
                message("You Lost!", BLUE,0)
                message("R to restart",BLUE,80)
                message("Q to menu",BLUE,160)
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
                            cmd_restart = True
                            restart_all_class(snake1,snake2,food)
                            lost = False
                    if event.type == pygame.QUIT:
                        txt_i = open('Levels/h.txt','r').read()
                        if int(txt_i) < MAX_SCORE:
                            txt_o = open('Levels/h.txt','w')
                            txt_o.write(str(MAX_SCORE))
                        game_over = True
                        back_menu = False
                        run = False
                        menu = False
                        lost = False
            FramePerSecond.tick(game_speed)