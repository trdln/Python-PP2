import pygame
import random
#pylint: disable=no-member
#pylint: disable=too-many-function-args

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')
background = pygame.image.load('res/grass.png')


##########################################    Snake    ##########################################

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx, self.dy = 2 * self.radius, 0  # right
        self.add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 200), element, self.radius)

    def move(self):
        self.elements.insert(
            0, [self.elements[0][0] + self.dx, self.elements[0][1] + self.dy])
        if not self.add:
            self.elements.pop()
        else:
            self.size += 1
            self.add = False

    def randomNotInSnake(self):
        x = random.randint(1, 37) * 20 + 10
        y = random.randint(1, 27) * 20 + 10
        if [x + 10, y + 10] in self.elements:
            return self.randomNotInSnake()
        else:
            return [x, y]

    def checkCollisions(self):
        global done
        global gameOver
        if self.elements[0] in self.elements[1:]:
            done = True
            gameOver = True

        if not (32 < self.elements[0][0] < screen.get_width() - 32 and 32 < self.elements[0][1] < screen.get_height() - 32):
            done = True
            gameOver = True


##########################################    Walls    ##########################################

class Walls:
    def __init__(self):
        self.image = pygame.image.load('res/wall.png')
        self.h = self.image.get_height()
        self.w = self.image.get_width()

    def draw(self):
        for i in range(screen.get_width() // self.w + 1):
            screen.blit(self.image, (i*self.w, 0))
            screen.blit(self.image, (i*self.w, screen.get_height() - self.h))

        for i in range(screen.get_height() // self.h + 1):
            screen.blit(self.image, (0, i*self.h))
            screen.blit(self.image, (screen.get_width() - self.w, i*self.h))


##########################################    Food    ##########################################


class Food:
    def __init__(self):
        self.image = pygame.image.load('res/apple.png')
        self.x, self.y = 210, 210

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def isEaten(snake, food):
    dist_x = snake.elements[0][0] - food.x - snake.radius
    dist_y = snake.elements[0][1] - food.y - snake.radius
    if -snake.radius * 2 < dist_x < food.image.get_width() and -snake.radius * 2 < dist_y < food.image.get_height():
        return True
    else:
        return False


def drawScore(score):
    font = pygame.font.SysFont('Courier', 24, bold=True)
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(text, (screen.get_width() - text.get_width() - 20, 10))

##########################################    Init    ##########################################


snake = Snake()
walls = Walls()
food = Food()

done = False
gameOver = False

d = 20
FPS = 10
clock = pygame.time.Clock()

##########################################    Main loop    ##########################################

font = pygame.font.SysFont('Courier', 48, bold=True)
start_text = font.render('Press space to start', True, (0, 0, 0))
screen.blit(background, (0, 0))
screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2,
                         screen.get_height() // 2 - start_text.get_height() // 2))
pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        break

while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d

    snake.move()
    snake.checkCollisions()
    if isEaten(snake, food):
        snake.add = True
        food.x, food.y = snake.randomNotInSnake()

    screen.blit(background, (0, 0))
    food.draw()
    snake.draw()
    walls.draw()
    drawScore(snake.size - 1)

    pygame.display.flip()


if gameOver:
    end_text = font.render(f'Game Over. Score: {snake.size - 1}', True, (0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(end_text, (screen.get_width() // 2 - end_text.get_width() // 2,
                           screen.get_height() // 2 - end_text.get_height() // 2))
    pygame.display.flip()

    sec = 0
    while sec < 3:
        sec += clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sec = 3

pygame.quit()
