import pygame 
import random

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0) 
WHITE = (255,255,255)
RESx = 700
RESy = 700

WIN = pygame.display.set_mode((RESx, RESy))
pygame.display.set_caption("Simple Paint")
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

font = pygame.font.SysFont('serif', 25)


def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x - w/2 , y - h / 2, w, h], 5)

def drawCircle(surface, color, x, y,rad):
    pygame.draw.circle(surface, color, (x, y), rad, 3)

def erase(surface, x, y,rad):
    pygame.draw.circle(surface, background_color, (x, y), rad)

def draw_line(surface, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(surface, color, (x, y), radius)

def screenshot(display,name,pos,size):
    image = pygame.Surface(size)  
    image.blit(display,(0,0),(pos,size))  
    pygame.image.save(image,name)  

draw_on = False

prevPoint = (0, 0)
curPoint = (0, 0)

# 0 - pencil, 1 - rectangle, 2 - circle, 3 - eraser
currentTool = 0
toolCount = 4

current_color = BLACK

background_color = WHITE

all_colors = [BLACK,WHITE,RED,GREEN,BLUE]

RAD = 20

run = True

WIN.fill(background_color)
pos_of_colors = []
s_cnt = int(open('Screenshots/number_of_screenshots.txt','r').readline())
file = open('Screenshots/number_of_screenshots.txt','w')
while  run:
    text_r = font.render(f"R = {RAD}",False,BLACK)
    pygame.draw.rect(WIN, background_color ,[0,0,RESx,100])
    WIN.blit(text_r, (30,40))

    for i in range(20):
        all_colors.append((random.randrange(256), random.randrange(256), random.randrange(256)))

    pygame.draw.rect(WIN, current_color ,[130,25,50,50])
    pygame.draw.rect(WIN, BLACK ,[130,25,50,50],4)
    cnt = 0

    for i in range(0,500,50):
        pygame.draw.rect(WIN, all_colors[cnt] ,[200 + i,10,35,35])
        pygame.draw.rect(WIN, BLACK ,[200 + i,10,35,35],2)
        pygame.draw.rect(WIN, all_colors[cnt + 10] ,[200 + i,55,35,35])
        pygame.draw.rect(WIN, BLACK ,[200 + i,55,35,35],2)
        cnt+=1
        pos_of_colors.append(((200 + i, 10),(235 + i , 35)))
        pos_of_colors.append(((200 + i, 55),(235 + i , 90)))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            file.write(str(s_cnt))
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if currentTool == 0:
                pygame.draw.circle(WIN, current_color, event.pos, RAD)
                draw_on = True
            elif currentTool == 1:
                drawRectangle(WIN, current_color, event.pos[0],event.pos[1], RAD * 2, RAD * 2)
                draw_on = True
            elif currentTool == 2:
                drawCircle(WIN, current_color, event.pos[0],event.pos[1],RAD)
                draw_on = True
            elif currentTool == 3:
                erase(WIN, event.pos[0],event.pos[1],RAD)
                draw_on = True    
            
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
            mouse_pos = pygame.mouse.get_pos()
            for pos1,pos2 in pos_of_colors:
                if pos1[0] < mouse_pos[0] < pos2[0] and pos1[1] < mouse_pos[1] < pos2[1]:
                    current_color = WIN.get_at(mouse_pos)
        if event.type == pygame.MOUSEMOTION:
            if draw_on and ( 0 <= event.pos[0] <= RESx and 100<=event.pos[1]<=RESy):
                if currentTool == 0: 
                    pygame.draw.circle(WIN, current_color, event.pos, RAD)
                    draw_line(WIN, current_color, event.pos, last_pos,  RAD)
                elif currentTool == 1:
                    drawRectangle(WIN, current_color, event.pos[0],event.pos[1], RAD * 2, RAD * 2)
                elif currentTool == 2:
                    drawCircle(WIN, current_color, event.pos[0],event.pos[1],RAD)
                elif currentTool == 3:
                    erase(WIN, event.pos[0],event.pos[1],RAD)
            last_pos = event.pos


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                currentTool += 1
                currentTool = currentTool % toolCount

            if event.key == pygame.K_d:
                WIN.fill(background_color)
            if event.key == pygame.K_UP:
                if RAD < 70:
                    RAD += 1
            if event.key == pygame.K_DOWN:
                if RAD > 1:
                    RAD -= 1
            if event.key == pygame.K_s:
                screenshot(WIN,f"Screenshots/screen{s_cnt}.png",(0,100),(600,600))
                s_cnt += 1

    pygame.display.flip()