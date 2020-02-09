class GameStats():
	"""Tracking game stats"""

	def __init__(self, settings):
		"""Initialisation game stats"""
		self.settings = settings
		self.reset_stats()
		self.game_active = True

		self.game_active = False


	def reset_stats(self):
		"""Initialisation stats, that changes during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
