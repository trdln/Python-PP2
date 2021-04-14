import pygame 
import random
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
pygame.display.set_caption("Snake")

snake_block = 30
snake_speed = 12

FramePerSecond = pygame.time.Clock()

font_style = pygame.font.Font("Materials/KA1.ttf", 30)
score_font = pygame.font.Font("Materials/KA1.ttf", 30)

FILE_NAME = 'snakes_saved.data'
move_rules = {}
class Snake():
    def __init__(self, color, coordinates):
        self.speed = snake_block 
        self.color = color
        self.elements = [coordinates]
        self.dx = 0
        self.dy = 0
        self.ate_food = False
    
    def move(self,key,buttons, move_rules):
        if (key[buttons["A"]]) and move_rules['A']:
                self.dx,self.dy = -snake_block, 0
                move_rules = {'W':True , 'S':True , 'A':True , 'D':False }
        if (key[buttons["D"]]) and move_rules['D']:
                self.dx,self.dy =  snake_block, 0
                move_rules = {'W':True , 'S':True , 'A':False , 'D':True }
        if (key[buttons["W"]]) and move_rules['W']:
                self.dx,self.dy = 0, -snake_block
                move_rules = {'W':True , 'S':False , 'A':True , 'D':True }
        if (key[buttons["S"]]) and move_rules['S']:
                self.dx,self.dy = 0, snake_block
                move_rules = {'W':False , 'S':True , 'A':True , 'D':True }

        
        old_head = self.elements[0]
        head = [old_head[0] + self.dx, old_head[1] + self.dy]

        if self.ate_food:
            self.elements = [head] + self.elements
        else:
            self.elements = [head] + self.elements[:-1]
        self.ate_food = False
    
    def draw(self):
        for item in self.elements:
            pygame.draw.rect(WIN, self.color, [*item, snake_block, snake_block])

    def get_head_coordinates(self):
        return self.elements[0]
    
    def get_length(self):
        return len(self.elements)

    def add_block(self):
        self.ate_food = True
    
    def is_collide(self, walls):
        pass
    
    def is_ate_food(self, food):
        pass

def message(msg, color,y = 100):
    mesg = font_style.render(msg, True, color)
    pos = mesg.get_rect(center=(RESx // 2, (RESy  + y - 100) // 2))
    WIN.blit(mesg, pos)

def game_loop():
    game_over = False
    game_close = False
    choose = False
    move_rules = {'W':True , 'S':True , 'A':True , 'D':True }
    buttons1 = {"A" : pygame.K_a , "D" : pygame.K_d, "W" : pygame.K_w , "S" : pygame.K_s}
    buttons2 = {"A" : pygame.K_LEFT , "D" : pygame.K_RIGHT, "W" : pygame.K_UP , "S" : pygame.K_DOWN}
    but = [buttons1 , buttons2]

    snake1 = Snake(BLACK, [RESx // 2, RESy // 2])
    snake2 = Snake(WHITE, [RESx // 2 + 50, RESy // 2])
    

    while not choose:
        WIN.fill(BLUE)
        message("Space to load", WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        with open(FILE_NAME, 'br') as f:
                            snakes = pickle.load(f)
                    except Exception as e:
                        print(e)
                        snakes = (snake1,snake2)
                else:
                    snakes = (snake1,snake2)
                choose = True
    
    foodx = round(random.randrange(0, RESx - snake_block) / float(snake_block)) * float(snake_block)
    foody = round(random.randrange(0, RESy - snake_block) / float(snake_block)) * float(snake_block)
    
    while not game_close:
        FramePerSecond.tick(snake_speed)

        while game_over:
            WIN.fill(BLUE)
            message("Game over!", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snakes, f)
                    game_close = True

        for snake in snakes:
            x1, y1 = snake.get_head_coordinates()
            if x1 >= RESx or x1 < 0 or y1 >= RESy or y1 < 0:
                game_over = True
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, RESx - snake_block) / float(snake_block)) * float(snake_block)
                foody = round(random.randrange(0, RESy - snake_block) / float(snake_block)) * float(snake_block)
                snake.add_block()

        pressed_keys = pygame.key.get_pressed()
        i = 0
        for snake in snakes:
            snake.move(pressed_keys, buttons1,but[i])
            i+=1

        WIN.fill(BLUE)
        pygame.draw.rect(WIN, GREEN, [foodx, foody, snake_block, snake_block]) 
        for snake in snakes:
            snake.draw()

        message(f"Your score: {str(snake1.get_length() - 1)}", YELLOW , -500)
   
        pygame.display.update()
            

if __name__ == '__main__':
    game_loop()