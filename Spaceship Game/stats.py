class Stats:
    """Track game stats of shipgame"""

    def __init__(self,game):
        """"Initialize statistics"""
        self.settings = game.settings
        self.reset()
        self.active = True

    def reset(self):
        self.remaining_tries = self.settings