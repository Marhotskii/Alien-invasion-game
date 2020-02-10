import json

class GameStats():
	"""Tracking game stats"""

	def __init__(self, settings):
		"""Initialisation game stats"""
		self.settings = settings
		self.reset_stats()
		self.game_active = True

		self.game_active = False

		#High score
		with open('best_score.json') as score:
			self.high_score = json.load(score)


	def reset_stats(self):
		"""Initialisation stats, that changes during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
