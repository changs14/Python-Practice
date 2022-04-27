"""All attributes to the user-controlled UFO"""

import pygame
from pygame.sprite import Sprite

class UFO(Sprite):
    """Load ship image and management"""
    
    def __init__(self, game):
        #Initialize the UFO
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        #Load ship image
        self.image = pygame.image.load('ship1.bmp')
        self.rect = self.image.get_rect()
        
        #Set the position of the UFO to the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store decimal value of ufo horizontal position
        self.x = float(self.rect.x)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Updates the ship position based on whether the flag is true (moving) or false (not moving)"""
        #Update the x (horizontal position) of the ufo
        #Check if the ufo is moving and not beyond the screen
        if self.moving_right and (self.rect.right<self.screen_rect.right):
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #Rect object is now the new x value
        self.rect.x = self.x
        
    def blitme(self):
        #Draws the current position of the uFO
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen when hit"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)