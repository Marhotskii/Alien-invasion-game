import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Ship class"""

	def __init__(self, settings, screen):
		"""Initialisation of the ship and it's start posiyion"""
		super().__init__()
		self.screen = screen

		#Init settings
		self.settings = settings

		#Load shoot sound
		self.shoot_sound = pygame.mixer.Sound('sounds/pew.wav')

		#Load death soun
		self.death_sound = pygame.mixer.Sound('sounds/expl6.wav')

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
		if (self.moving_right) and (self.rect.right < 
				self.screen_rect.right):
			self.center += self.settings.ship_speed_factor
		if (self.moving_left) and (self.rect.left > 0):
			self.center -= self.settings.ship_speed_factor

		#Update centerx
		self.rect.centerx = self.center


	def center_ship(self):
		"""Placing ship in the middle"""
		self.center = self.screen_rect.centerx