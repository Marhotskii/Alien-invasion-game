import pygame

class Ship():
	"""Ship class"""

	def __init__(self, settings, screen):
		"""Initialisation of the ship and it's start posiyion"""
		self.screen = screen

		#Init settings
		self.settings = settings

		"""Load ship image and get rectangle"""
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Float coordinate of the ship center
		self.center = float(self.rect.centerx)

		#Moving flags
		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		"""Draw the ship in the current position"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Update ship position"""
		if self.moving_right:
			self.center += self.settings.ship_speed_factor
		if self.moving_left:
			self.center -= self.settings.ship_speed_factor

		#Update centerx
		self.rect.centerx = self.center