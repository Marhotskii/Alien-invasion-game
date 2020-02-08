class Settings():
	"""Class to store all of game settings"""

	def __init__(self):
		"""Initialisation of game settings"""
		#Screen param
		self.screen_width = 1280
		self.screen_height = 720
		self.background_color = (230, 230, 230)
		self.game_speed = 500

		#Ship settings
		self.ship_speed_factor = 1.5

		#Bullet settings
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 5
		# 1 - moving right, -1 - moving left
		self.fleet_direction = 1