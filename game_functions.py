import pygame

def check_events(ship):
	"""Check keyboard and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		#Start moving
		elif event.type == pygame.KEYDOWN:
			#Move right
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			#Move left
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True

		#Stop moving
		elif event.type == pygame.KEYUP:
			#Move right
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			#Move left
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False


def update_screen(settings, screen, ship):
	"""Update screen"""
	screen.fill(settings.background_color)
	ship.blitme()

	"""Display last drawn screen"""
	pygame.display.flip()