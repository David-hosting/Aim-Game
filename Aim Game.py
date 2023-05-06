#Main File
import pygame
import sys
from utils import menu

#Initialization
pygame.mixer.init()
pygame.init()

FONT = pygame.font.SysFont('Comic Sans MS', 30)

button1 = menu.Button('Play',200,40,(300,300),5)
button2 = menu.Button('Exit',200,40,(300,350),5)
screen = pygame.display.set_mode((800, 600))
screen.fill('#DCDDD8')

def buttons_draw() -> None:
    for b in menu.buttons:
        b.draw()

while True:
    text_surface_2 = FONT.render("Welcome To Aim Game - By David Ioffe", True, (0, 0, 0))
    screen.blit(text_surface_2, (120,120))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    buttons_draw()

    pygame.display.update()


