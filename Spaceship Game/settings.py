import ssl

class Settings:
    """Store settings for the game"""
    
    def __init__(self):
        self.width = 1200 #Screen width
        self.height = 800 #Screen height
        self.bg_color = (249, 255, 228) #Screen background colour
        self.bg_color = (249, 255, 228) #Screen background colour
        self.ship_speed = 1.2 #Movementspeed of the ufo

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
