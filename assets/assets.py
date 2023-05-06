from asyncio import as_completed
import pygame
from dataclasses import dataclass

@dataclass
class Settings:
    asset : pygame.Surface
    scale : tuple

class Circle(Settings):
    def circle(self) -> pygame.Surface:
        """
        | Function which returns circle (scale). Returns the circle as 'pygame.Surface' 
        """
        self.asset = pygame.transform.scale(self.asset, self.scale)
        return self.asset

class MiniBackground(Settings):
    def cover(self) -> pygame.Surface:
        """
        | Function which returns mini bg (scale). Returns the circle as 'pygame.Surface' 
        """
        self.asset = pygame.transform.scale(self.asset, self.scale)
        return self.asset


