import pygame

from bullet import Bullet

def check_keydown_events(event, settings, screen, ship, bullets):
	"""Check keydown events"""
	#Move right
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True

	#Move left
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	#Create new bullet
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)


def fire_bullet(settings, screen, ship, bullets):
	"""Create new bullet"""
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):
	"""Check keyup events"""
	#Move right
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False

	#Move left
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(settings, screen, ship, bullets):
	"""Check keyboard and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		#Start moving
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, 
				screen, ship, bullets)

		#Stop moving
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
	"""Update screen"""
	screen.fill(settings.background_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	#Display last drawn screen
	pygame.display.flip()


def update_bullets(bullets):
	"""Update bullets positions and delete old bullets"""
	#Update bullets
	bullets.update()

	#Deleting old  bullets
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)