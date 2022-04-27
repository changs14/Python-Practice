import pygame.font
from pygame.sprite import Group
from ufo import UFO

class Scoreboard:
    """Class that stores the user score"""

    def __init__(self, game):
        """Init scorekeeping for the game"""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = game.settings
        self.stats = game.stats

        #Font settings
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
    
        #Create level
        self.set_level()

        #Create ship limit
        self.set_ships()

        #Create score
        self.create_score()
        self.set_high_score()

    def create_score(self):
        """Create score image"""
        score_string = str(self.stats.score)
        self.score_image = self.font.render(score_string, True, self.text_colour, self.setting.bg_color)

        #Score image attributes
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def set_score(self):   
        """Display the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def set_high_score(self):
        """Display high score onto the screen"""
        high_score = self.stats.high_score
        high_score_str= "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_colour, self.setting.bg_color)

        #Center at the top and middle of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check for new high scores"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.set_high_score()

    def display_score(self):
        """Draw scoreboard to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_rect)

    def set_level(self):
        """"draw level to screen"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_colour, self.setting.bg_color)

        #Position to the top left of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = self.screen_rect.top

    def set_ships(self):
        """Display number of lives left"""
        lives_str = str(self.stats.remaining_tries)
        self.lives_image = self.font.render(lives_str, True, self.text_colour, self.setting.bg_color)

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left+ 100
        self.level_rect.top = self.screen_rect.top