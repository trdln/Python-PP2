#Imports
import pygame
import random
import json
pygame.init()
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = pygame.Color('yellow')

#Other Variables for use in the program
RESx = 400
RESy = 600
#Range for speed of Cars
S_start,S_end = 1,5
SPEED = random.randint(S_start,S_end)
#It's boring to have slow cars, that's why I have created variable to increase speed each 5 seconds 
SPEED_UP = 0
#Speed for coin 
COIN_SPEED = 2
#Speed of player: how many pixels he goes for 1 / FPS seconds
PLAYER_SPEED = (RESx // FPS)
#Var's for CarScore And CoinScore
SCORE = 0
COIN_SCORE = 0

game_run = True
run = True
 
#Setting up Fonts
font = pygame.font.Font("Materials/KA1.ttf", 45)
font_small = pygame.font.Font("Materials/KA1.ttf", 30)
#Render text
game_over = font.render("Game Over", True, BLACK)
replay = font_small.render("Press R to play",True,BLACK)
rechoose = font_small.render("Press Esc to menu",True, BLACK)
author = font_small.render("Trdln",True,BLACK)
#Setting background and menu for points
background = pygame.image.load("Materials/AnimatedStreet.png")
bar = pygame.image.load("Materials/bar.png")
#Create screen 
WIN = pygame.display.set_mode((RESx,RESy + 100))
pygame.display.set_caption("Драйв по встречке")
#Enemy different colours
Enemy_sprites = [pygame.image.load("Materials/Enemy1.png"),pygame.image.load("Materials/Enemy2.png"),
pygame.image.load("Materials/Enemy3.png"),pygame.image.load("Materials/Enemy4.png"),
pygame.image.load("Materials/Enemy5.png"),pygame.image.load("Materials/Enemy6.png"),
pygame.image.load("Materials/Enemy7.png"),pygame.image.load("Materials/Enemy8.png")]
#Player Cars
Cars = [pygame.image.load("Materials/Player1.png"),pygame.image.load("Materials/Player2.png"),
pygame.image.load("Materials/Player3.png"), pygame.image.load("Materials/Player4.png")]
#Animated Background
anim_counter = 0
animated_back = [pygame.image.load("Materials/AnimatedStreet1.png"), pygame.image.load("Materials/AnimatedStreet2.png"),
pygame.image.load("Materials/AnimatedStreet3.png"),pygame.image.load("Materials/AnimatedStreet4.png"),
pygame.image.load("Materials/AnimatedStreet5.png"),pygame.image.load("Materials/AnimatedStreet6.png"),
pygame.image.load("Materials/AnimatedStreet7.png"),pygame.image.load("Materials/AnimatedStreet8.png")]

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.id = random.randint(0,7)
        self.image = Enemy_sprites[self.id]
        self.surf = pygame.Surface(self.image.get_size())
        center = (random.randint(40,RESx-40), 0 - self.image.get_height())
        self.rect = self.surf.get_rect(center = center)
    
      def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600 + 10):
            SCORE += 1
            self.rect.top = 0 - self.image.get_height()
            self.rect.center = (random.randint(40, RESx - 40), 0 - self.image.get_height())
            SPEED = random.randint(S_start,S_end) + SPEED_UP
            self.id = random.randint(0,7)
            self.image = Enemy_sprites[self.id] # Enemy's colours changes randomly
  
class Player(pygame.sprite.Sprite):
    def __init__(self,choice):
        super().__init__() 
        self.image = Cars[choice - 1]
        self.surf = pygame.Surface(self.image.get_size())
        self.rect = self.surf.get_rect(center = (160, 520))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        '''
        if self.rect.top > 0 + 5:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -PLAYER_SPEED)
        if self.rect.bottom < RESy - 10:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,PLAYER_SPEED)
        '''
        if self.rect.left > 0 + 5:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-PLAYER_SPEED, 0)
        if self.rect.right < RESx - 5:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(PLAYER_SPEED, 0)
#Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Materials/coin.png')
        self.surf = pygame.Surface(self.image.get_size())
        center = (random.randint(40,RESx-40), 0 - self.image.get_height())
        self.rect = self.surf.get_rect(center = center)

    def move(self):
        global COIN_SPEED
        self.rect.move_ip(0,COIN_SPEED)
        if (self.rect.top > 600 + 10):
            self.rect.top = 0 - self.image.get_height()
            self.rect.center = (random.randint(40, RESx - 40), 0 - self.image.get_height())
            COIN_SPEED = 2 +  SPEED_UP
    def draw(self):
        self.surf = pygame.Surface(self.image.get_size())
        center = (random.randint(40,RESx-40), 0 - self.image.get_height())
        self.rect = self.surf.get_rect(center = center) # last function to re-draw coin
def anim_background():
    global anim_counter
    if anim_counter + 1 == FPS:
        anim_counter = 0
    WIN.blit(animated_back[int(anim_counter//(FPS / len(animated_back)))], (0,0))
    anim_counter+=1
#Background Music
pygame.mixer.Sound('Materials/background.wav').play(-1)
#Variable for high score system
MAX_SCORE = 0
#I have menu, yes
menu = True
re_choose_car = True
while menu:
    re_choose_car = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            choose = False
    while re_choose_car:
        #Background for menu
        main_menu_background = pygame.image.load('Materials/main.png')
        #I tried to do so that when I choose background changes too, but I couldn't, so this is array with background photos
        if_car = []
        if_car.append(pygame.image.load('Materials/if1.png'))
        if_car.append(pygame.image.load('Materials/if2.png'))
        if_car.append(pygame.image.load('Materials/if3.png'))
        if_car.append(pygame.image.load('Materials/if4.png'))
        #Draw menu
        WIN.blit(main_menu_background,(0,0))
        #Draw my sign
        position = author.get_rect(center = (RESx//2,30))
        WIN.blit(author,position)
        #Choosing process
        menu_pause = False

        pygame.display.flip()
        #Bool if I have choosen or no
        car_choosen = False
        # Variable which I will use to determine which car I have choosen
        choice = 0
        #keys = pygame.key.get_pressed() # This is array which I tried to use to change background while I am choosing
        while not menu_pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_pause = True
                        game_run = True
                    #If Space we Start race
                if event.type == pygame.QUIT:
                        menu_pause = True
                        menu = False
                        game_run = False
                        run = False
                        re_choose_car = False
                    #To close
                #Choosing process
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        #WIN.blit(if_car[0],(0,0))
                        car_choosen = True
                        choice = 1
                    #I Have choosen first car, so on
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        #WIN.blit(if_car[1],(0,0))
                        car_choosen = True
                        choice = 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        #WIN.blit(if_car[2],(0,0))
                        car_choosen = True
                        choice = 3
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        #WIN.blit(if_car[3],(0,0))
                        car_choosen = True
                        choice = 4
            #If I didn't choose or forgot programm will use automatically first car
            if not car_choosen:
                choice = 1 
        pygame.display.flip()
        #The while for restarting
        while game_run:
            #Re-writing variables for restarting
            SPEED = random.randint(S_start,S_end)         
            SCORE = 0
            SPEED_UP = 0 
            COIN_SCORE = 0 
            COIN_SPEED = 2 
            #Setting up Sprites        
            P1 = Player(choice)
            E1 = Enemy()
            COIN = Coin()    
            #Creating Sprites Groups
            enemies = pygame.sprite.Group()
            enemies.add(E1)
            coins = pygame.sprite.Group()
            coins.add(COIN)
            all_sprites = pygame.sprite.Group()
            all_sprites.add(P1)
            all_sprites.add(E1)
            
            
            #Adding a new User event 
            INC_SPEED = pygame.USEREVENT + 1
            pygame.time.set_timer(INC_SPEED, 5000) # Timer for every 5 seconds
            
            #Game Loop
            run = True
            #The main game process
            while run:
                #Cycles through all events occurring  
                for event in pygame.event.get():
                    if event.type == INC_SPEED:
                        SPEED_UP += 1  #Every 5 seconds additional speed increses to 1
                    if event.type == pygame.QUIT:
                        menu = False
                        game_run = False
                        run = False
                        re_choose_car = False
                        #To close
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        p = True
                        while p:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                                    p = False
                                if event.type == pygame.QUIT:
                                    menu = False
                                    game_run = False
                                    run = False
                                    re_choose_car = False
                                    p = False
                #Draw background
                #WIN.blit(background, (0,0))
                anim_background()
                #Render texts for scores
                scores = font_small.render(f'Cars {SCORE}', True, YELLOW)
                highscore = font_small.render(f'High score {MAX_SCORE}',True, YELLOW)
                coin_score = font_small.render(f'Coins {COIN_SCORE}',True,YELLOW)
                
                #Moves and Re-draws all Sprites
                for entity in all_sprites:
                    WIN.blit(entity.image, entity.rect)
                    entity.move()
                #Check collision of player with Coins, if there is no collision:
                if not pygame.sprite.spritecollideany(P1, coins):
                    for i in coins:
                        WIN.blit(i.image,i.rect)
                        i.move()
                else:#If there is collision, sound for getting coin from Mario, and re-draw coin
                    pygame.mixer.Sound('Materials/coinsound.mp3').play()
                    COIN_SCORE+=1
                    COIN_SPEED += 0.2
                    COIN.draw()
                #Menu with scores, the reason why I write it here, to hide cars and coins under menu
                WIN.blit(bar,(0,600))
                #Draw all Scores
                WIN.blit(scores, (20,610))
                WIN.blit(coin_score,(220,610))
                WIN.blit(highscore,(70,650))
                #To be run if collision occurs between Player and Enemy
                if pygame.sprite.spritecollideany(P1, enemies):
                    pygame.mixer.Sound('Materials/crash.wav').play()
                    if MAX_SCORE < SCORE + COIN_SCORE:
                        MAX_SCORE = SCORE + COIN_SCORE #Finding high score
                    #The screen when I lose 
                    WIN.fill(RED)
                    #Draw informations about last game
                    text_score = font_small.render(f'Your score is {SCORE + COIN_SCORE}',True,BLACK)
                    pos1 = game_over.get_rect(center=(RESx // 2, (RESy - 100) // 2))
                    pos2 = replay.get_rect(center=(RESx // 2, (RESy+200) // 2))
                    pos3 = text_score.get_rect(center = (RESx // 2, (RESy + 50) // 2))
                    pos4 = rechoose.get_rect(center = (RESx//2,(RESy + 300)//2))
                    WIN.blit(game_over, pos1)
                    WIN.blit(replay, pos2)
                    WIN.blit(text_score, pos3)
                    WIN.blit(rechoose,pos4)
                    pygame.display.flip()
                    #Delete all added sprites from group, to clean and re-create them after
                    for entity in all_sprites:
                            entity.kill()
                    #While for re-starting
                    choose = False
                    while not choose:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                menu = False
                                choose = True
                                run = False
                                game_run = False 
                                re_choose_car = False
                                # out = open('highscore.txt','w')
                                # out.write(MAX_SCORE)
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_r:
                                    choose = True  
                                    run = False    #If type R we will re-start game 
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    choose = True
                                    run = False
                                    game_run = False   
                                    re_choose_car = False
                pygame.display.update()
                FramePerSec.tick(FPS)