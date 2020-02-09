class Settings():
	"""Class to store all of game settings"""

	def __init__(self):
		"""Initialisation static settings"""
		#Screen param
		self.screen_width = 1280
		self.screen_height = 720
		self.background_color = (230, 230, 230)

		#Ship settings
		self.ship_limit = 3

		#Bullet settings
		self.bullet_width = 1200
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Alien settings
		self.fleet_drop_speed = 10

		#Game acceleration
		self.speedup_scale = 1.1
		#Alien cost
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialisation dynamic settings"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		#fleet_direction = 1 means move to the Rigth, - 1 to the Left
		self.fleet_direction = 1

		self.alien_point = 50


	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_point = int(self.alien_point * self.score_scale)
