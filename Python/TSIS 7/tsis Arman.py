import pygame
import math
pygame.init()
WIDTH = 700
HEIGHT = 500
#Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
#Screen configurations
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sine and cosine")
#Setting fps
clock = pygame.time.Clock()
FPS = 40
run = True
x = 0
xx = 0
point_sine = []
point_cosine = []
values = ["1.00","0.75","0.50","0.25","0.00","-0,25","-0.50","-0.75","-1.00"]
pi_values = ["-3П","-2.5П","-2П","-1.5П","-П","-0.5П","0","0.5П","П","1.5П","2П","2.5П","3П"]

#Code Bais
class Point:
    # constructed using a normal tupple
    def __init__(self, point_t=(0, 0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    if length == 0:
        length = 1
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.aaline(surf, color, start.get(), end.get(), width)

# Функция которая рисует маленькие линий в двух координатах которые получены кодом который скинул Агай

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Logic
    #Draw
    screen.fill(WHITE)
        #Draw axises
    pygame.draw.line(screen,BLACK,(30,HEIGHT/2),(WIDTH - 30, HEIGHT/2),3)
    pygame.draw.line(screen,BLACK,(WIDTH/2,30),(WIDTH/2,HEIGHT - 30),3)
        #Draw boundaries
            # First stage
    pygame.draw.line(screen,BLACK,(30,50),(WIDTH - 30,50),1)
    pygame.draw.line(screen,BLACK,(50,30),(50,HEIGHT - 30),1)
    pygame.draw.line(screen,BLACK,(30,HEIGHT - 50),(WIDTH - 30, HEIGHT - 50),1)
    pygame.draw.line(screen,BLACK,(WIDTH - 50,30),(WIDTH - 50,HEIGHT - 30),1)
            # Second stage
    pygame.draw.line(screen,BLACK,(30,30),(WIDTH - 30,30),2)
    pygame.draw.line(screen,BLACK,(30,30),(30,HEIGHT-30),2)
    pygame.draw.line(screen,BLACK,(30,HEIGHT-30),(WIDTH-30,HEIGHT-30),2)
    pygame.draw.line(screen,BLACK,(WIDTH-30,30),(WIDTH-30,HEIGHT-30),2)
        #Draw net
            #Draw horizontal lines
    for i in range(100,401,50):
        pygame.draw.line(screen,BLACK,(30,i),(WIDTH-30,i))
            #Draw vertical lines
    for i in range(50,601,100):
        if not i in range(400,451):
            pygame.draw.line(screen,BLACK,(i,30),(i,HEIGHT-30))
        else:
            pygame.draw.line(screen,BLACK,(450,100),(450,470))
        #Draw indicators
        font = pygame.font.Font(None,25)
        sine = font.render("sin x",True,BLACK)
        cosine = font.render("cos x",True,BLACK)
        screen.blit(sine,(450,55))
        screen.blit(cosine,(450,75))
        pygame.draw.line(screen,RED,(500,63),(525,63),2)
        pygame.draw.line(screen,BLUE,(500,83),(525,83),2)
        #Draw pointers for pi's
    for i in range(100,601,100):
        pygame.draw.line(screen,BLACK,(i,HEIGHT-30),(i,HEIGHT-45),1)
        pygame.draw.line(screen,BLACK,(i,30),(i,45),1)
        #Draw pointers for values
    for i in range(75,426,50):
        pygame.draw.line(screen,BLACK,(30,i),(45,i))
        pygame.draw.line(screen,BLACK,(WIDTH-45,i),(WIDTH-30,i))
        #Draw small lines
            #Draw lines for pi's
    for i in range(75,626,25):
        pygame.draw.line(screen,BLACK,(i,HEIGHT-30),(i,HEIGHT-40))
        pygame.draw.line(screen,BLACK,(i,40),(i,30))
            #Draw lines for values
    for  i in range(62,451,25):
        pygame.draw.line(screen,BLACK,(30,i),(40,i))
        pygame.draw.line(screen,BLACK,(WIDTH-40,i),(WIDTH-30,i))
            #Draw additional lines for pi's
    for i in range(62,651,25):
        pygame.draw.line(screen,BLACK,(i,HEIGHT-30),(i,HEIGHT-35))
        pygame.draw.line(screen,BLACK,(i,35),(i,30))
            #Draw y-values
    for i in range(50,451,50):
        font = pygame.font.Font(None,15)
        value = font.render(values[(i // 50)-1],True,BLACK)
        screen.blit(value,(5,i - 5))
            #Draw pi values
    for i in range(50,651,100):
        font = pygame.font.Font(None,15)
        pi = font.render(pi_values[(i // 50) - 1],True,BLACK)
        screen.blit(pi,(i - 3,HEIGHT - 25))
    #Draw animation for sine
    j = 50
    dxc = 10
    dx = 5
    pos_x = x - 50
    s_x = (math.pi/100) * (x % 100)
    s_y = int() 
    # s_y = math.sin(s_x)
    if pos_x in range(50,151) or pos_x in range(250,351) or pos_x in range(450,551):
        s_y = (math.sin(s_x) * 200) + 250
    else:
        s_y = 250 - (abs(math.sin(s_x)) * 200)
    if pos_x <= 650 and pos_x >= 50:
        point_sine.append((pos_x,s_y))
        # pygame.draw.line(screen,RED,(x,s_y),(x+1,s_y+1),2)
    '''if len(point_sine) > 2:   
        pygame.draw.lines(screen,RED,False,point_sine,2)
    '''

    for i in range(len(point_sine) - 1):
        draw_dashed_line(screen, RED, point_sine[i], point_sine[i+1])
    # Draw animation for cosine 
    pos_x_c = xx - 50
    c_x = (math.pi/100) * (xx % 100)
    c_y = int()
    if pos_x_c in range(50,150) or pos_x_c in range(250,350) or pos_x_c in range(450,550) or pos_x_c in range (650,750):
        c_y = (math.cos(c_x) * 200) + 250
    else:
        c_y = 250 - (math.cos(c_x)) * 200
    if pos_x_c <= 700 and pos_x_c + 50 >= 100:
        point_cosine.append((pos_x_c ,c_y))
        # pygame.draw.line(screen,RED,(x,s_y),(x+1,s_y+1),2)
    
    if len(point_cosine) > 2:
        pygame.draw.aalines(screen,BLUE,False,point_cosine,2)
    '''
    #Cosine dash line
    for i in range(len(point_cosine) - 1):
        draw_dashed_line(screen, BLUE, point_cosine[i], point_cosine[i+1])
    '''
    #Update
    if x < 700 and xx <= 750:
        x += dx
        xx += dx
    #
    
    # mouse = pygame.mouse.get_pos()
    # print(mouse)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()