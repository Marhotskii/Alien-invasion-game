import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Bullet class"""

	def __init__(self, settings, screen, ship):
		"""Create bullet object in current ship position"""
		super().__init__()
		self.screen = screen

		#Create bullet in (0,0) and assign right position"""
		self.rect = pygame.Rect(0, 0, settings.bullet_width, 
			settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#Position in float
		self.y = float(self.rect.y)

		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor


	def update(self):
		"""Moving bullet to the top of screen"""
		self.y -= self.speed_factor

		#Update rectangle position
		self.rect.y = self.y


	def draw_bullet(self):
		"""Drawing bullet"""
		pygame.draw.rect(self.screen, self.color, self.rect)
