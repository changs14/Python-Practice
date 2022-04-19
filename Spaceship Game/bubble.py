import pygame
from pygame.sprite import Sprite

class Bubble(Sprite):
    """Class representing bubble sprite that the ufo will shoot down"""

    def __init__(self, game):
        """Initialize position of bubble"""
        super().__init__()
        self.screen = game.screen

        #Load image and set rect
        self.image = pygame.image.load('bubble.bmp')
        self.rect = self.image.get_rect()

        #First image will always display at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store position of bubble
        self.x = float(self.rect.x)