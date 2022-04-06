import pygame
from pygame.sprite import Sprite

class Ammo(Sprite):
        """Class that manages all ammo features"""

        def __init__(self, game):
            """Create object at ship position"""
            super().__init__()
            self.screen = game.screen
            self.settings = game.settings
            self.colour = self.settings.ammo_colour

            #Create a bullet at 0,0 then adjust to the current position
            self.rect = pygame.Rect(0,0, self.settings.ammo_width, self.settings.ammo_height)
            self.rect.midtop =  game.ufo.rect.midtop

            #Keep the position of the ammo as a number
            self.y = float(self.rect.y)


        def update(self):
            """Ammo will always keep moving upwards"""
            #Update number position of ammo
            self.y -= self.settings.ammo_speed

            #Update rect position
            self.rect.y = self.y

        def draw(self):
            """Draw to screen"""
            pygame.draw.rect(self.screen, self.colour, self.rect)