import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Alien class"""

	def __init__(self, settings, screen):
		"""Initialisation class"""

		super().__init__()
		self.screen = screen
		self.settings = settings

		#Load image and make rectangle
		self.image = pygame.image.load('images/alien64.png')
		self.rect = self.image.get_rect()

		#Alien position in the left top corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Coordiate in float
		self.x = float(self.rect.x)


	def blitme(self):
		"""Draw alien in current position"""
		self.screen.blit(self.image, self.rect)