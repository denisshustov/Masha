import pygame
import sys
#https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie

#-------------colors--------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
#-------------colors--------------
WIN_WIDTH = 600
WIN_HEIGHT = 400

FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

r1 = pygame.Rect((150, 20, 100, 75))
# радиус и координаты круга
r = 30
x = 5   # скрываем за левой границей
y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали


running = True
while running:
    screen.fill(BLACK)

    clock.tick(FPS)
    # events содержит список событий
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    # --------
    # изменение объектов и многое др.
    # --------
    # pygame.draw.rect(screen, YELLOW, (20, 20, 100, 75),5)
    # pygame.draw.rect(screen, GREEN, r1,5)
    pygame.draw.circle(screen, YELLOW, (x, y), r)
    # если полностью скрылся за правой границей
    if x >= WIN_WIDTH + r:
        x = 0 - r
    else:  # во всех остальных случаях
        x += 2  # в следующем кадре круг сместится,
        # от значения зависит "скорость движения"


    
    # обновление экрана
    pygame.display.update()


pygame.quit()
