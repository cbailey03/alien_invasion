import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game, create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set the screen size and title.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Alien Invasion")

        # Initialize the ship
        self.ship = Ship(self)
        # Initialize the bullets
        self.bullets = pygame.sprite.Group()
        # Initialize the aliens
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Update the ship.
            self.ship.update()
            # Update the bullets.
            self._update_bullets()
            # Update the screen.
            self._update_screen()   

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Check to see if the movement keys are being pressed.
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                # Check to see if the movement keys are not being pressed.
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Respond to keydown presses."""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_w:
            self.ship.moving_forward = True
        if event.key == pygame.K_s:
            self.ship.moving_backward = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keyup releases."""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_w:
            self.ship.moving_forward = False
        if event.key == pygame.K_s:
            self.ship.moving_backward = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 
    
    def _update_screen(self):
        """Update images on the screen and flip the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Redraw the ship.
        self.ship.blitme()
        # Redraaw the bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Redraw the aliens
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
