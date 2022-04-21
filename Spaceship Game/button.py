import pygame.font

class Button:
    
    def __init__(self, game, message):
        """Init button attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Dimensions of start button
        self.width, self.height = 200, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Create button object
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.create_message(message)
        
    def create_message(self, message):
        """Turn a message into an image and center it onto the button"""
        self.message_image = self.font.render(message, True, self.text_colour, self.button_colour)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center
        
    def create_button(self):
        """Create a button the screen"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)