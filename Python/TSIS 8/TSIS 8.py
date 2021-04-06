#Imports
from math import trunc
import pygame
import random

from pygame import key
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
S_start,S_end = 1,5
SPEED = random.randint(S_start,S_end) 
SPEED_UP = 0
COIN_SPEED = 2
PLAYER_SPEED = 5
SCORE = 0
COIN_SCORE = 0
game_run = True
run = True
 
#Setting up Fonts
font = pygame.font.Font("Materials/KA1.ttf", 45)
font_small = pygame.font.Font("Materials/KA1.ttf", 30)
game_over = font.render("Game Over", True, BLACK)
replay = font_small.render("Press R to play",True,BLACK)
author = font_small.render("Trdln",True,BLACK)
 
background = pygame.image.load("Materials/AnimatedStreet.png")
bar = pygame.image.load("Materials/bar.png")
#Create a white screen 
WIN = pygame.display.set_mode((RESx,RESy + 100))
WIN.fill(WHITE)
pygame.display.set_caption("Драйв по встречке")
#Enemy different colours
Enemy_sprites = []
Enemy_sprites.append(pygame.image.load("Materials/Enemy1.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy2.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy3.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy4.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy5.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy6.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy7.png"))
Enemy_sprites.append(pygame.image.load("Materials/Enemy8.png"))
#Player Cars
Cars = []
Cars.append(pygame.image.load("Materials/Player1.png"))
Cars.append(pygame.image.load("Materials/Player2.png"))
Cars.append(pygame.image.load("Materials/Player3.png"))
Cars.append(pygame.image.load("Materials/Player4.png"))
#Coin


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
            self.image = Enemy_sprites[self.id]
 
 
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
            COIN_SPEED = random.randint(3,8) + SPEED_UP
    def draw(self):
        self.surf = pygame.Surface(self.image.get_size())
        center = (random.randint(40,RESx-40), 0 - self.image.get_height())
        self.rect = self.surf.get_rect(center = center)
        
        
pygame.mixer.Sound('Materials/background.wav').play(-1)
MAX_SCORE = 0
menu = True
while menu:
    
    main_menu_background = pygame.image.load('Materials/main.png')

    if_car = []
    if_car.append(pygame.image.load('Materials/if1.png'))
    if_car.append(pygame.image.load('Materials/if2.png'))
    if_car.append(pygame.image.load('Materials/if3.png'))
    if_car.append(pygame.image.load('Materials/if4.png'))

    WIN.blit(main_menu_background,(0,0))
    position = author.get_rect(center = (RESx//2,30))
    WIN.blit(author,position)
    menu_pause = False
    pygame.display.flip()
    car_choosen = False
    choice = 0
    keys = pygame.key.get_pressed()
    while not menu_pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_pause = True
            if event.type == pygame.QUIT:
                    menu_pause = True
                    menu = False
                    game_run = False
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    #WIN.blit(if_car[0],(0,0))
                    car_choosen = True
                    choice = 1
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
        if not car_choosen:
            choice = 1 # Машина по умолачанию
    pygame.display.flip()
    while game_run:
        SPEED = random.randint(S_start,S_end)         
        SCORE = 0
        SPEED_UP = 0 
        COIN_SCORE = 0  
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
        pygame.time.set_timer(INC_SPEED, 5000)
        
        #Game Loop
        run = True
        while run:
            #Cycles through all events occurring  
            for event in pygame.event.get():
                if event.type == INC_SPEED:
                    SPEED_UP += 1  
                if event.type == pygame.QUIT:
                    menu = False
                    game_run = False
                    run = False
            WIN.fill(WHITE)
            WIN.blit(background, (0,0))
            
            scores = font_small.render(f'Cars {SCORE}', True, YELLOW)
            highscore = font_small.render(f'High score {MAX_SCORE}',True, YELLOW)
            coin_score = font_small.render(f'Coins {COIN_SCORE}',True,YELLOW)
            
            #Moves and Re-draws all Sprites
            for entity in all_sprites:
                WIN.blit(entity.image, entity.rect)
                entity.move()
            
            if not pygame.sprite.spritecollideany(P1, coins):
                for i in coins:
                    WIN.blit(i.image,i.rect)
                    i.move()
            else:
                pygame.mixer.Sound('Materials/coinsound.mp3').play()
                COIN_SCORE+=1
                COIN.draw()
                coins.add(COIN)
                WIN.blit(COIN.image,COIN.rect)
            WIN.blit(bar,(0,600))
            #All scores
            WIN.blit(scores, (20,610))
            WIN.blit(coin_score,(220,610))
            WIN.blit(highscore,(70,650))
            #To be run if collision occurs between Player and Enemy
            if pygame.sprite.spritecollideany(P1, enemies):
                pygame.mixer.Sound('Materials/crash.wav').play()
                if MAX_SCORE < SCORE + COIN_SCORE:
                    MAX_SCORE = SCORE + COIN_SCORE  
                WIN.fill(RED)
                text_score = font_small.render(f'Your score is {MAX_SCORE}',True,BLACK)
                pos1 = game_over.get_rect(center=(RESx // 2, (RESy - 100) // 2))
                pos2 = replay.get_rect(center=(RESx // 2, (RESy+200) // 2))
                pos3 = text_score.get_rect(center = (RESx // 2, (RESy + 50) // 2))
                WIN.blit(game_over, pos1)
                WIN.blit(replay, pos2)
                WIN.blit(text_score, pos3)
                
                pygame.display.flip()
                for entity in all_sprites:
                        entity.kill()
                choose = False
                while not choose:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            menu = False
                            choose = True
                            run = False
                            game_run = False 
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                choose = True  
                                run = False        
                        
            pygame.display.update()
            FramePerSec.tick(FPS)