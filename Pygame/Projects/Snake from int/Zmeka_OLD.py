# import all libraries which are uses
import pygame
import sys
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
field1 = (105, 166, 52)
field2 = (105, 176, 52)

pygame.init()

# Set the width and height of the screen [width, height]
size = (455,440)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Creating Ponits
NewScore = 0
xNS = 1

# Creating Snake
# Head
snake = [82,82]
# Start direction
goes_side = "Right"
# body
body = [[82,82],[62,82],[42,82]]
segment = []
# Creating logic Body of snake
def animation():
    body.insert(0,list(snake))
    body.pop()
# DELETED this code i wrote in Dreawing code DELETED
    #def draw_snake():
    #    for segment in body:
    #        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1],16,16))

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

head_right = pygame.image.load('pictures/Head/Head-right.png').convert()
head_left = pygame.image.load('pictures/Head/Head-left.png').convert()
head_up = pygame.image.load('pictures/Head/Head-up.png').convert()
head_down = pygame.image.load('pictures/Head/Head-down.png').convert()

body1 = pygame.image.load('pictures/Body/Body1.png').convert()
body2 = pygame.image.load('pictures/Body/Body2.png').convert()
body3 = pygame.image.load('pictures/Body/Body3.png').convert()
body4 = pygame.image.load('pictures/Body/Body4.png').convert()
body5 = pygame.image.load('pictures/Body/Body5.png').convert()
body6 = pygame.image.load('pictures/Body/Body6.png').convert()
body7 = pygame.image.load('pictures/Body/Body7.png').convert()
body8 = pygame.image.load('pictures/Body/Body8.png').convert()
body9 = pygame.image.load('pictures/Body/Body9.png').convert()
body10 = pygame.image.load('pictures/Body/Body10.png').convert()
body11 = pygame.image.load('pictures/Body/Body11.png').convert()
body12 = pygame.image.load('pictures/Body/Body12.png').convert()
body13 = pygame.image.load('pictures/Body/Body13.png').convert()
body14 = pygame.image.load('pictures/Body/Body14.png').convert()

i = random.randrange(0,14)
#if i == 1:
    #screen.blit(len(body[]))
#if i == 2:
#if i == 3:
#if i == 4:
#if i == 5:
#if i == 6:
#if i == 7:
#if i == 8:
#if i == 9:
#if i == 10:
#if i == 11:
#if i == 12:
#if i == 13:
#if i == 14:

# Creating Food
food0 = (random.randrange(0,20)*20)+20
food1 = (random.randrange(0,20)*20)+20
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # Control of snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and goes_side != "Left":
                goes_side = "Right"
            elif event.key == pygame.K_LEFT and goes_side != "Right":
                goes_side = "Left"
            elif event.key == pygame.K_UP and goes_side != "Down":
                goes_side = "Up"
            elif event.key == pygame.K_DOWN and goes_side != "Up":
                goes_side = "Down"
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    # --- Game logic should go here
    # Where snake looks, there snake goes
    if goes_side == "Right":
        snake[0] += 20
    if goes_side == "Left":
        snake[0] -= 20
    if goes_side == "Up":
        snake[1] -= 20
    if goes_side == "Down":
        snake[1] += 20
    # Here i created cell for snake
    if snake[0] > 402:
        snake[0] -= 20
    if snake[0] < 22:
        snake[0] += 20
    if snake[1] > 402:
        snake[1] -= 20
    if snake[1] < 22:
        snake[1] += 20

    # ---- logic of Clash head and body
    for k in body:
        if k[0] == snake[0] and k[1] == snake[1]:
            print("You lose!")
            sys.exit()
    for l in body:
        if l[0] == food0+2 and l[1] == food1+2:
            food0 = (random.randrange(0,20)*20)+20
            food1 = (random.randrange(0,20)*20)+20
    # --- Screen-clearing code goes here

    # Here, we clear the screen to Black. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Floop of field where snake goes
    # Actually i don't know how it's to explain but if you
    # interesting in this, look at the code down below =)(meme)
    row1 = [0,0]
    for row in range(20):
        row1[0] += 20
        row1[1] = 20
        h = row1[0]/2
        for column in range(20):
            pygame.draw.rect(screen, field2,(row1[0],row1[1],20,20))
            if math.fmod(row, 2) == 0:
                pygame.draw.rect(screen, field1,(row1[0],row1[1],20,20))
            if math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field1,(row1[0],row1[1],20,20))
            if math.fmod(row, 2) == 0 and math.fmod(column, 2) == 1:
                pygame.draw.rect(screen, field2,(row1[0],row1[1],20,20))
            row1[1] += 20
    # Body trucking head
    animation()
    # Drawing Head of snake

    pygame.draw.rect(screen, GREEN, (snake[0], snake[1], 16, 16))
    # Drawing body of snake
    for segment in body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1],16,16))
    # Drawing food
    pygame.draw.rect(screen, RED, (food0+2, food1+2, 16, 16))
    # Condition of eating food
    if food0 < snake[0] < food0+20 and food1 < snake[1] < food1+20:
        # Score + 1
        NewScore += 1
        print(NewScore)
        # Random food everytime when snake get food
        food0 = (random.randrange(0,20)*20)+20
        food1 = (random.randrange(0,20)*20)+20
        body.append(body[0])
        xNS += 1
        j = len(body)
        print(j)
        # Score line
    pygame.draw.rect(screen, BLUE, (20,425,xNS,15))
    # if xNS get 100 points write "You win!" and exit the game
    if xNS > 100:
        print("You win!")
        sys.exit()


    if goes_side == "Right":
        screen.blit(head_right, (snake[0], snake[1]))
    if goes_side == "Left":
        screen.blit(head_left, (snake[0], snake[1]))
    if goes_side == "Up":
        screen.blit(head_up, (snake[0], snake[1]))
    if goes_side == "Down":
        screen.blit(head_down, (snake[0], snake[1]))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()
