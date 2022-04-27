class Stats:
    """Track game stats of shipgame"""

    def __init__(self,game):
        """"Initialize statistics"""
        self.settings = game.settings
        self.reset()
        self.active = False

        #Levels
        self.level = 1

        #High scores
        self.score = 0
        self.high_score = 0

    def reset(self):
        self.remaining_tries = self.settings.ship_lives