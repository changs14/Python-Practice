import pygame.font

class Scoreboard:
    """Class that stores the user score"""

    def __init__(self, game):
        """Init scorekeeping for the game"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = game.settings
        self.stats = game.stats

        #Font settings
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.Sysfont(None, 48)

        #Create score
        self.create_score()

    def create_score(self):
        """Create score image"""
        score_string = str(self.stats.score)
        self.score_image = self.font.render(score_string, True, self.text_colour, self.ettings.bg_colour)

        #Score image attributes
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def shop_score(self):   
        """Display the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)