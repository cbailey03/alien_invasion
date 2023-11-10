class Settings:
    """Stores all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (50, 50, 50)

        # Ship settings
        self.ship_speed = 0.3

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 5