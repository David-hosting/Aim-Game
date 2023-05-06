import time
from webbrowser import BackgroundBrowser
import pygame, random
import os, sys
from utils import utils
from assets import assets

#Initialization
pygame.font.init()

#General settings
CIRCLE = pygame.image.load(os.path.join('assets', 'Circle.png'))
MINI_BG = pygame.image.load(os.path.join('assets', 'mini bg.png'))
FONT = pygame.font.SysFont('Comic Sans MS', 30)
BACKGROUND_MUSIC = os.path.join('assets', 'BackgroundMusic.wav')

clicks, all_clicks = 0, 0

class Screen:
    def __init__(self, screen_size : tuple, fill : tuple) -> None:
        """
        | Initializer,
        screen_size: tuple which takes two  arguements, widths and lenght of the main window,
        fill: tuple which takes three arguements, R, G, B. which fills the main window.
        Returns None.
        """
        self.screen_size = screen_size
        self.fill = fill

    @property
    def window(self) -> None:
        pygame.mixer.music.load(BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.1)
        start_time = time.time()
        """
        | Function which executes all the graphics. Takes no arguments & returns None.
        """
        global clicks, all_clicks
       
        screen = pygame.display.set_mode(self.screen_size)
        screen.fill(self.fill)

        circle_pos = (random.randint(0, 750), random.randint(100, 550))
        c = assets.Circle(CIRCLE, (50, 50))
        circle1 = c.circle()
        mask = pygame.mask.from_surface(circle1)
        screen.blit(circle1, circle_pos)

        text_surface = FONT.render("Clicks: {} out of {}".format(clicks, all_clicks), False, (0, 0, 0))
        screen.blit(text_surface, (0,0))

        pygame.display.update()

        while open:
            end_time = time.time()
            sec = end_time - start_time
            __time = utils.timer(sec)

            text_surface_2 = FONT.render("{}:{}:{}".format(int(__time[2]),int(__time[1]),int(__time[0])), False, (0, 0, 0))
            screen.blit(text_surface_2, (700,0))
            pygame.display.update()

            time.sleep(0.025)

            bg = assets.MiniBackground(MINI_BG, (200, 50))
            cover = bg.cover()
            screen.blit(cover, (700, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    try:
                        if mask.get_at((event.pos[0]-circle_pos[0], event.pos[1]-circle_pos[1])):
                            clicks += 1
                            all_clicks += 1

                            circle_pos = (random.randint(0, 750), random.randint(100, 550))
                            c = assets.Circle(CIRCLE, (50, 50))
                            circle1 = c.circle()
                            mask = pygame.mask.from_surface(circle1)

                            pygame.display.update()
                     
                    except IndexError:
                        all_clicks += 1
                    
                    screen = pygame.display.set_mode(self.screen_size)
                    screen.fill(self.fill)

                    screen.blit(circle1, circle_pos)

                    text_surface = FONT.render("Clicks: {} out of {}".format(clicks, all_clicks), False, (0, 0, 0))

                    screen.blit(text_surface, (0,0))

                    pygame.display.update()

