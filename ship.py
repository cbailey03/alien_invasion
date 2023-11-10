import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.transform.scale(pygame.image.load('player_ship.bmp'), (25, 50))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        # Store a decimal value for the ships vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

    def update(self):
        """Update the ships position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_forward and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update the rect object from self.x.
        self.rect.x = round(self.x)
        # Update the rect object from self.y
        self.rect.y = round(self.y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)