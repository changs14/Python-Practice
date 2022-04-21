import ssl

class Settings:
    """Store settings for the game"""
    
    def __init__(self):
        self.width = 1200 #Screen width
        self.height = 800 #Screen height
        self.bg_color = (249, 255, 228) #Screen background colour
        self.bg_color = (249, 255, 228) #Screen background colour
        self.ship_speed = 1.2 #Movementspeed of the ufo
        self.ship_lives = 3

        #Ammo settings
        self.ammo_speed = 1.0 #Projectile speed
        self.ammo_width = 3
        self.ammo_height = 15
        self.ammo_colour = (60,60,60)
        self.ammo_limit = 4

        #Bubble settings
        self.bubble_speed = 1.0
        self.drop_speed = 10
        self.direction = 1

        #Game speed
        self.speedup = 1.1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Changes to the settings throughout the game"""
        self.ship_speed = 1.5
        self.ammo_speed = 3.0
        self.bubble_speed = 1.0

        self.direction = 1

    def speedup(self):
        """Increase speed of all objects"""
        self.ship_speed *= self.speedup
        self.ammo_speed *= self.speedup
        self.bubble_speed *= self.speedup
