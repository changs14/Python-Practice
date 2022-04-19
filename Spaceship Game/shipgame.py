"""Star Ship"""
"""The player controls a UFO at the bottom of the screen. They may move left and right
    using the left and right arrow keys and shoot using the space bar. Players must shoot
    the falling stars before it hits the player. If all stars are cleared, a new fleet will
    spawn at faster speed. If a player gets hit three times by the stars, the game is over."""

import sys
import pygame
from ufo import UFO
from settings import Settings
from ammo import Ammo
from bubble import Bubble

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

        #Ammo object
        self.ammos = pygame.sprite.Group()

        #Bubble object
        self.bubbles = pygame.sprite.Group()
        self.lots_of_bubbles()

    def lots_of_bubbles(self):
        """Generate a lot of bubbles"""
        bubble = Bubble(self)
        bubble_width = bubble.rect.width
        space_x = self.settings.width - (2 * bubble_width)
        bubble_count = space_x // (2*bubble_width)

        #Create a row of bubbles
        for num_of_bubbles in range(bubble_count):
            #Create bubble imagine in current row
            bubble = Bubble(self)
            bubble.x = bubble_width + 2 * bubble_width * num_of_bubbles
            bubble.rect.x = bubble.x
            self.bubbles.add(bubble)

        
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
        elif event.key == pygame.K_SPACE:
            self.fire() #Fire a bullet
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup(self, event):
        """Check for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ufo.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ufo.moving_left = False         

    def fire(self):
        """Creates a bullet and adds to the group"""
        #Users may shoot 4 bullets in a fixed interval
        if len(self.ammos) < self.settings.ammo_limit:
            new_ammo = Ammo(self)
            self.ammos.add(new_ammo)
                    
    def bullet_update(self):
        """Function that will update all bullets on screen"""
        
        #Update positions
        self.ammos.update()

        #Clear bullets that have disappeared
        for ammo in self.ammos.copy():
            if ammo.rect.bottom <= 0:
                self.ammos.remove(ammo)

    def update(self):
        """Update and draw the current screen"""
        #Draw most current screen
        self.screen.fill(self.settings.bg_color) #Draw the background colour
        self.ufo.blitme()

        self.bubbles.draw(self.screen)

        #Draw bullet to screen
        for ammo in self.ammos.sprites():
            ammo.draw()

         #Display the current screen
        pygame.display.flip()
        
    def run_game(self):
        """Run the main game loop"""
        while True:
            self.events() #Check if the game is running
            self.ufo.update() #Update the position of the ufo based on key presses
            self.bullet_update()
            self.update() #Update the screen
            
if __name__ == '__main__':
    #Run the game
    ss = StarShip()
    ss.run_game()
    
    #000332060