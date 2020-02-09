import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	"""Init game and draw window"""
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, 
									settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Create play button
	play_button = Button(settings, screen, "Play")

	#Create stats object
	#Create Scoreboard
	stats = GameStats(settings)
	sb = Scoreboard(settings, screen, stats)

	#Create ship
	ship = Ship(settings, screen)

	#Creating bullets group and aliens group
	bullets = Group()
	aliens = Group()

	#Create aliens fleet
	gf.create_fleet(settings, screen, ship, aliens)

	#Start main game cycle
	while True:
		#Keyboard and mouse event tracking
		gf.check_events(settings, screen, stats, play_button,
				ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(settings, screen, stats, sb,
				ship, aliens, bullets)
			gf.update_aliens(settings, stats, screen, ship, 
				aliens, bullets)
		gf.update_screen(settings, screen, stats, sb, ship, aliens,
				bullets, play_button)

run_game()