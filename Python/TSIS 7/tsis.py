import pygame
import math

pygame.init()
# Разрешения окна
# ! Есть возможность изменения разрешения ! не прям точный, но +- работающий
RESx, RESy = 1200, 800
#RESx,RESy = 800,600
cnt = (1200 / RESx) / (780 / RESy)
# Окно
win = pygame.display.set_mode((RESx, RESy))
pygame.display.set_caption("Cos and Sin")
pi = math.pi
# colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
# fonts
font = pygame.font.SysFont('serif', int(RESx / 50))
text1 = font.render("sinx", False, black)
text2 = font.render("cosx", False, black)
text3 = font.render('X',    False, black)
# Переменная для запуска кода
run = True
# Коеффицент для отрисовки графиков не на весь экран
k = 2 / 3
# Коеф начала и конца в соотношений разрешения экрана
start = (1 - k) / 2
end = (k + (1 - k) / 2)
# Это рендж х = от -3pi до 3pi
xrange = (-3 * pi, 3 * pi)
# Шаг или же расстояние между точками х
step = 0.1
# Коеф для того чтобы получать нунжый размер графиков
kx = (k * RESx) / (6 * pi)
ky = (k * RESy) / 2
# Координаты центра чтобы позже просто подвинуть графики к центру
center = (RESx/2, RESy/2)
real_center = math.ceil((RESx * end - RESx * start) * 3 / 4)
real_center_y = math.ceil((RESy * end - RESy * start) * 3 / 4)
# Код для дэш лайна от Бейсенбек Агая


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
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.aaline(surf, color, start.get(), end.get(), width)

# Функция которая рисует маленькие линий в двух координатах которые получены кодом который скинул Агай
def draw_dashed_lines(win, color, points, width, dash_l):
    for i in range(len(points) - 1):
        draw_dashed_line(win, color, points[i], points[i+1], width, dash_l)

# Функция которая достает все точки любой функций и возвращает лист из тюплсов
def get_points(f, xrange, step, kx, ky, center):
    num = math.ceil((xrange[1] - xrange[0]) / step)  # количество точек х
    x_val = (x * step + xrange[0] for x in range(num))  # значения х
    # кх ку - коеф чтобы растянуть под нунжый размер
    func = ((kx * x, ky * f(x)) for x in x_val)
    points = tuple(map(lambda x: (x[0] + center[0], -x[1] + center[1]), func))
    return points

def draw_line(win, x, y, y1):
    k = math.ceil((RESy * end - RESy * start) / 8)
    for i in range(k, int(RESy * end - RESy * start), k):
        pygame.draw.line(win, black, (x[0], x[1] + i), (y[0], y[1] + i), 1)

    m = math.ceil((RESx * end - RESx * start) / 6)
    for i in range(m, int(RESx * end - RESx * start), m):
        if i == m * 4:
                pygame.draw.line(win, black, (x[0] + i, x[1] + m * cnt / 2), (y1[0] + i, y1[1]), 1)
        else:
            pygame.draw.line(win, black, (x[0] + i, x[1]), (y1[0] + i, y1[1]), 1)
    win.blit(text1, (x[0] + m * 4 - RESx / 60, x[1]))
    win.blit(text2, (x[0] + m * 4 - RESx / 60, x[1] + RESx / 40))
    pygame.draw.line(win, red, (x[0] + m * 4 + RESx / 30, x[1] + RESx / 66), (x[0] + m * 4 + RESx / 17, x[1] + RESx / 66))
    draw_dashed_line(win, blue, (x[0] + m * 4 + RESx / 30, x[1] + RESx / 24), (x[0] + m * 4 + RESx / 17, x[1] + RESx / 24), 2)
    win.blit(text3, (RESx/2 - RESx / 150, RESy * end + RESx / 20))

    x_val  = ['-3п', '-5п', '-2п', '-3п', '-п','-п', '0', 'п', 'п', '3п', '2п', '5п', '3п']
    x_val2 = ['', ' 2', '', ' 2', '', ' 2', '', '2', '', '2', '', '2', '']
    val    = ['', ' _', '', ' _', '', ' _', '', '_', '', '_', '', '_', '']
    y_val  = [' 1.00', ' 0.75', ' 0.50', ' 0.25',' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']

    j = 0
    for i in range(len(x_val)):
        text4 = font.render(x_val[i], False, black)
        text5 = font.render(x_val2[i], False, black)
        text6 = font.render(val[i], False, black)
        win.blit(text4, (RESx * start + j,  RESy * end + RESy * cnt / 39))
        win.blit(text5, (RESx * start + j,  RESy * end + RESy * cnt / 20))
        win.blit(text6, (RESx * start + j,  RESy * end + RESy * cnt / 39 - 2 ))
        j += (m/2) - 1
    j = 0
    for i in range(len(y_val)):
        text4 = font.render(y_val[i], False, black)
        win.blit(text4, (RESx * start - RESx / 12,
                 RESy * start + j - RESx / 80))
        j += k


def draw_little_hor(x, y, h, m, l):
    s = math.ceil((RESx * end - RESx * start) / 6) / 8
    for i in range(0, 48, 4):
        if h < 0:
            pygame.draw.line(win, black, (x + s * i, y ), (x + s * i, y - 20), 1)
        else:
            pygame.draw.line(win, black, (x + s * i, y ), (x + s * i, y + 20), 1)
    for i in range(0, 48, 2):
        pygame.draw.line(win, black, (x + s * i, y + h), (x + s * i, y + m), 1)
    for i in range(0, 48):
        pygame.draw.line(win, black, (x + s * i, y + h), (x + s * i, y + l + m), 1)


def draw_little_ver(x, y, h, m, l):
    s = math.ceil((RESy * end - RESy * start) / 8) / 4
    for i in range(0, 32, 4):
        if h < 0:
            pygame.draw.line(win, black, (x - 20, y + s * i), (x , y + s * i), 1)
        else:
            pygame.draw.line(win, black, (x + 20, y + s * i), (x, y + s * i), 1)
    for i in range(0, 32, 2):
        pygame.draw.line(win, black, (x + h, y + s * i), (x + m, y + s * i), 1)
    for i in range(0, 32):
        pygame.draw.line(win, black, (x + h, y + s * i), (x + l + m, y + s * i), 1)


# Получаем все точки синуса и косинуса
sin_points = get_points(math.sin, xrange, step, kx, ky, (real_center  + 2,real_center_y))
cos_points = get_points(math.cos, xrange, step, kx, ky, (real_center  + 2,real_center_y))
while run:
    # Заполняем экран
    win.fill(white)

    # Рисуем центральную линию координат
    pygame.draw.lines(win, black, False, ((RESx * start, RESy / 2),    (RESx * end, RESy / 2)),    2)
    pygame.draw.lines(win, black, False, ((real_center, RESy * start), (real_center, RESy * end)), 2)
    # Точки уголков нашей рамки
    '''
    bounding_points = (
        (start * RESx, start * RESy),
        (end * RESx, start * RESy),
        (end * RESx, end * RESy),
        (start * RESx, end * RESy)
    )
    '''
    bb = 20
    draw_little_hor(start * RESx, start * RESy, -20, -10, -5)
    draw_little_hor(start * RESx, end   * RESy, 20, 10, 5)
    draw_little_ver(start * RESx, start * RESy, -20, -10, -5)
    draw_little_ver(end   * RESx, start * RESy, 20, 10, 5)
    # Рисуем рамку
    # pygame.draw.aalines(win , black, True, bounding_points, 4) #alternative method
    #pygame.draw.rect(win, black, [RESx * start, RESy* start, RESx * k, RESy * k], 1)
    pygame.draw.line(win, black, (RESx * start, RESy * start - bb), (RESx * start, RESy * end + bb))
    pygame.draw.line(win, black, (RESx * end,   RESy * start - bb), (RESx * end, RESy * end + bb))
    pygame.draw.line(win, black, (RESx * start - bb, RESy * end),   (RESx * end + bb, RESy * end))
    pygame.draw.line(win, black, (RESx * start - bb, RESy * start), (RESx * end + bb, RESy * start))
    # Внешняя рамка
    pygame.draw.rect(win, black, [RESx * start - bb, RESy * start - bb, RESx * k + bb * 2, RESy * k + bb * 2], 2)
    # Рисуем синус готовой функцие pygame.draw.aalines
    pygame.draw.aalines(win, red, False, sin_points)
    # Рисуем косинус написанной функцией для дэш линий
    draw_dashed_lines(win, blue, cos_points, 2, 3)
    # pygame.draw.aalines(win , (255,0,0),False, cos_points) #функция для обычной отрисовки косинуса
    draw_line(win, (RESx * start, RESy * start), (RESx * end, RESy * start), (RESx * start, RESy * end))
    # Чтобы закрыть окно
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    # Обовнляем окно
    pygame.display.flip()
