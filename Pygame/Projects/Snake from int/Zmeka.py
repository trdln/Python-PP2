# import all libraries which are uses
import pygame
import random
import sys
import math

# Define some colors
BLACK = (20, 60, 20)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
field1 = (105, 166, 52)
field2 = (105, 176, 52)

pygame.init()

# Set the width and height of the screen [width, height]
size = (440, 445)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ZMEKA")


#class GuideSettings():
#    def __init__(self, x, y, filename):
#        self.x = x
#        self.y = y
#        self.bitmap = pygame.image.load(filename).convert
#
#    def page(self):
#        done = True
#        while done:
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    done = False
#                elif event.type == pygame.KEYDOWN:
#                    if event.key == pygame.K_ESCAPE:
#                        sys.exit()
#        screen.blit(self.bitmap, (self.x, self.y))
#        pygame.display.flip()
#
#
#guide = GuideSettings(0, 0, "pictures/Main Menu/Control menu.png")
#guide.page()


# --------- Creating main menu ---------
class Menu():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename)
        self.done = True
    def menu(self):
        self.done = True
        # -- Pos button Start --
        # Left-up angle of Start
        start_pos = (120, 170)
        s_p_x = start_pos[0]
        s_p_y = start_pos[1]
        # Right-down angle of Start
        start_pos1 = (320, 210)
        s_p1_x = start_pos1[0]
        s_p1_y = start_pos1[1]
        # -- Pos button Quit --
        quit_pos = (120, 330)
        # Left-up angle of Quit
        q_p_x = quit_pos[0]
        q_p_y = quit_pos[1]
        quit_pos1 = (320, 371)
        # Right-down angle of Quit
        q_p1_x = quit_pos1[0]
        q_p1_y = quit_pos1[1]
        # -- pos button of Control --
        control = (120, 250)
        # Left-up angle of Control
        c_p_x = control[0]
        c_p_y = control[1]
        control1 = (320, 291)
        # Right-down angle of Control
        c_p1_x = control1[0]
        c_p1_y = control1[1]
        # ---- Main loop for main menu ----
        while self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                    # Checer of mouse clicker
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Detector of mouse pos
                    pos = pygame.mouse.get_pos()
                    posx = pos[0]
                    posy = pos[1]
                    # Check pos of mouse and button Start
                    if s_p_x < posx < s_p1_x and s_p_y < posy < s_p1_y:
                        done = False
                    elif c_p_x < posx < c_p1_x and c_p_y < posy < c_p1_y:
                        pass
                    elif q_p_x < posx < q_p1_x and q_p_y < posy < q_p1_y:
                        sys.exit()
                    # Exit from the game when you press ESCAPE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    # Start game when you press SPACE
                    elif event.key == pygame.K_SPACE:
                        self.done = False
            screen.blit(self.bitmap, (self.x, self.y))
            pygame.display.flip()


# Creating main menu
plunt = Menu(0, 0, "pictures/Main Menu/main_menu.png")
plunt.menu()


# Creating Snake
class Snake():
    # Adding pictures for changing picture by direction
    def __init__(self, image_pth):
        # x, y position head of snake
        self.head = [122, 202]
        # mass of x and y position of all body of snake
        self.body = [[122, 202], [102, 202], [82, 202]]
        # direction where snake goes
        self.direction = "Right"
        # sprite of snake
        self.image_pth = pygame.image.load(image_pth).convert()
        # mass for adding new part of body in the future
        self.segment = []
        self.Score = 0
        # variable for main loop
        self.done = False
        # x pos for food
        self.food_x = (random.randrange(0, 20) * 20) + 20
        # y pos for food
        self.food_y = (random.randrange(0, 20) * 20) + 20
        # wide for Blue line of WIN
        self.line_to_win = 1
        # detector for food, it won't spawn in snake
        self.detector = []
        # stoping time for few checks
        self.time_stop = True
        # variable for continuation or exit the game
        self.retry = ""

    def draw_head(self):
        pygame.draw.rect(screen, YELLOW, (self.head[0], self.head[1], 16, 16))

    # Control of head and by the way body
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.direction != "Left":
                    self.direction = "Right"
                elif event.key == pygame.K_LEFT and self.direction != "Right":
                    self.direction = "Left"
                elif event.key == pygame.K_UP and self.direction != "Down":
                    self.direction = "Up"
                elif event.key == pygame.K_DOWN and self.direction != "Up":
                    self.direction = "Down"
                elif event.key == pygame.K_ESCAPE:
                    self.time_stop = True
                    plunt.done = True
                    plunt.menu()
                # when you press SPACE game will start
                elif event.key == pygame.K_SPACE:
                    self.time_stop = False

                elif event.key == pygame.K_r:
                    self.head = [122, 202]
                    self.body = [[122, 202], [102, 202], [82, 202]]
                    self.direction = "Right"
                    self.Score = 0
                    self.food_x = (random.randrange(0, 20) * 20) + 20
                    self.food_y = (random.randrange(0, 20) * 20) + 20
                    self.retry = ""
                    self.line_to_win = 1

    # detecting head and body crush
    def hit_body(self):
        if self.time_stop == False:
            for hit in self.body:
                if hit[0] == self.head[0] and hit[1] == self.head[1]:
                    print("You lose!")
                    # Stoping time for check
                    self.time_stop = True

    # detecting that food won't spawn in body
    def exclusion_stucking_food(self):
        for self.detector in self.body:
            if self.detector[0] == self.food_x + 2 and self.detector[1] == self.food_y + 2:
                self.food_x = (random.randrange(0, 20) * 20) + 20
                self.food_y = (random.randrange(0, 20) * 20) + 20

    # That is logic how snake goes on a field
    def logic_move(self):
        if self.time_stop == False:
            if self.direction == "Right":
                self.head[0] += 20
            if self.direction == "Left":
                self.head[0] -= 20
            if self.direction == "Up":
                self.head[1] -= 20
            if self.direction == "Down":
                self.head[1] += 20

    # That is logic where snake can't go
    def field_snake(self):
        if self.head[0] > 402:
            self.head[0] -= 20
        if self.head[0] < 22:
            self.head[0] += 20
        if self.head[1] > 402:
            self.head[1] -= 20
        if self.head[1] < 22:
            self.head[1] += 20

    # Changing sprites on snake depending on direction
    def sprites(self):
        if self.direction == "Right":
            screen.blit(head_right, (self.head[0], self.head[1]))
        if self.direction == "Left":
            screen.blit(head_left, (self.head[0], self.head[1]))
        if self.direction == "Up":
            screen.blit(head_up, (self.head[0], self.head[1]))
        if self.direction == "Down":
            screen.blit(head_down, (self.head[0], self.head[1]))

    # Every time when snake "eat" food: Change positions of food, Score + 1 and blue line up, +one body block
    def eating_food(self):
        if self.food_x < self.head[0] < self.food_x + 20 and self.food_y < self.head[1] < self.food_y + 20:
            self.food_x = (random.randrange(0, 20) * 20) + 20
            self.food_y = (random.randrange(0, 20) * 20) + 20
            # Score + 1
            self.Score += 1
            print(self.Score)
            # Random food everytime when snake get food
            self.body.append(self.body[0])
            self.line_to_win += 1

    def drawing_food(self):
        pygame.draw.rect(screen, RED, (self.food_x + 2, self.food_y + 2, 16, 16))

    # Logic that snake follow the head
    def animation(self):
        if self.time_stop == False:
            self.body.insert(0, list(self.head))
            self.body.pop()

    def draw_body(self):
        self.segment = []
        for segment in self.body:
            pygame.draw.rect(screen, YELLOW, pygame.Rect(segment[0], segment[1], 16, 16))


# Creating snake
snake = Snake("pictures/Head/Head-right.png")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
head_right = pygame.image.load('pictures/Head/Head-right.png').convert()
head_left = pygame.image.load('pictures/Head/Head-left.png').convert()
head_up = pygame.image.load('pictures/Head/Head-up.png').convert()
head_down = pygame.image.load('pictures/Head/Head-down.png').convert()

# -------- Main Program Loop -----------
while not snake.done:
    # --- Main event loop and control
    snake.move()
    # --- Game logic should go here
    snake.logic_move()
    snake.field_snake()
    snake.hit_body()
    snake.exclusion_stucking_food()
    # --- Screen-clearing code goes here
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Floop of field where snake goes
    # Actually i don't know how it's to explain but if you
    # interesting in this, look at the code down below =)(meme)
    row1 = [0, 0]
    for row in range(20):
        row1[0] += 20
        row1[1] = 20
        h = row1[0] / 2
        for column in range(20):
            pygame.draw.rect(screen, field2, (row1[0], row1[1], 20, 20))
            if math.fmod(row, 2) == 0:
                pygame.draw.rect(screen, field1, (row1[0], row1[1], 20, 20))
            if math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field1, (row1[0], row1[1], 20, 20))
            if math.fmod(row, 2) == 0 and math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field2, (row1[0], row1[1], 20, 20))
            row1[1] += 20
    # Body trucking head
    snake.animation()
    # Drawing Head of snake
    snake.draw_head()
    # Drawing body of snake
    snake.draw_body()
    # Drawing food
    snake.drawing_food()
    snake.eating_food()

    # "LINE TO WIN"
    pygame.draw.rect(screen, BLUE, (20, 425, snake.line_to_win, 15))
    # That is check when score goes 100+ points
    if snake.line_to_win > 100:
        print("You win!")
        sys.exit()

    snake.sprites()

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
