import pygame
from pygame.sprite import Sprite

class Bubble(Sprite):
    """Class representing bubble sprite that the ufo will shoot down"""

    def __init__(self, game):
        """Initialize position of bubble"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        #Load image and set rect
        self.image = pygame.image.load('bubble.bmp')
        self.rect = self.image.get_rect()

        #First image will always display at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store position of bubble
        self.x = float(self.rect.x)

    def update(self):
        """Update movement of bubbles"""
        self.x += self.settings.bubble_speed * self.settings.direction
        self.rect.x = self.x

    def check_edges(self):
        """Check if a bubble is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

