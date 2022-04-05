"""Star Ship"""
"""The player controls a UFO at the bottom of the screen. They may move left and right
    using the left and right arrow keys and shoot using the space bar. Players must shoot
    the falling stars before it hits the player. If all stars are cleared, a new fleet will
    spawn at faster speed. If a player gets hit three times by the stars, the game is over."""

import sys
import pygame
from ufo import UFO
from settings import Settings

class StarShip:
    """General class containing game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        
        #Create game window and display game title in the top bar
        self.settings = Settings() #Get game settings
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height)) #Get game display
        pygame.display.set_caption("Star Ship") #Top bar title
        
        #UFO object
        self.ufo = UFO(self)
        
    def events(self):
        """Check if the game is running or not"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
                    
    def _check_keydown(self, event):
        """Check for keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ufo.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ufo.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup(self, event):
        """Check for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ufo.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ufo.moving_left = False            
                    
    def update(self):
        """Update and draw the current screen"""
        #Draw most current screen
        self.screen.fill(self.settings.bg_color) #Draw the background colour
        self.ufo.blitme()

         #Display the current screen
        pygame.display.flip()
        
    def run_game(self):
        """Run the main game loop"""
        while True:
            self.events() #Check if the game is running
            self.ufo.update() #Update the position of the ufo based on key presses
            self.update() #Update the screen
            
if __name__ == '__main__':
    #Run the game
    ss = StarShip()
    ss.run_game()
    
    #000332060