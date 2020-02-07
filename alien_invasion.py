import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
	"""Init game and draw window"""
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, 
									settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(settings, screen)

	#Creating group to storage bullets
	bullets = Group()

	#Start main game cycle
	while True:
		#Keyboard and mouse event tracking
		gf.check_events(settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(settings, screen, ship, bullets)

run_game()







