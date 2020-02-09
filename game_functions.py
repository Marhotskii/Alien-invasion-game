import pygame

from bullet import Bullet
from alien import Alien
from time import sleep


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

	#Exit game
	elif event.key == pygame.K_ESCAPE:
		pygame.quit()


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


def check_events(settings, screen, stats, play_button,
		ship, aliens, bullets):
	"""Check keyboard and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		#Ckick button Play
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings, screen, stats, play_button,
				ship, aliens, bullets, mouse_x, mouse_y)

		#Start moving
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, 
				screen, ship, bullets)

		#Stop moving
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def check_play_button(settings, screen, stats, play_button,
		ship, aliens, bullets, mouse_x, mouse_y):
	"""Start game when click button Play"""

	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:

		#Cursor is hiding
		pygame.mouse.set_visible(False)

		#Reset game stats
		stats.reset_stats()
		stats.game_active = True

		#Clear list f aliens and bullets
		aliens.empty()
		bullets.empty()

		#Create a new aliens fleet
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()


def update_screen(settings, screen, stats, ship, aliens,
	bullets, play_button):
	"""Update screen"""
	screen.fill(settings.background_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	#Button visiable if game is not active
	if not stats.game_active:
		play_button.draw_button()

	#Display last drawn screen
	pygame.display.flip()


def update_bullets(settings, screen, ship, aliens, bullets):
	"""Update bullets positions and delete old bullets"""
	#Update bullets
	bullets.update()

	#Deleting old  bullets
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
	"""Check collisions"""
	#Check collision bullet with alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		#Create new fleet
		bullets.empty()
		create_fleet(settings, screen, ship, aliens)


def get_number_rows(settings, ship_height, alien_height):
	"""Calculate number of rows"""
	available_space_y = (settings.screen_height - 
						(2 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def get_number_aliens_x(settings, alien_width):
	"""Calculate number of aliens"""
	available_space_x = settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def create_alien(settings, screen, aliens, alien_number, row_number):
	"""Create alien and push it in the row"""
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = 1.5 * alien.rect.height * row_number
	aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
	"""Creating aliens fleet"""

	#Creat alien and searching number of aliens in the row
	#Distance between two aliens = aliens width
	alien = Alien(settings, screen)
	number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
	number_rows = get_number_rows(settings, ship.rect.height, 
		alien.rect.height)

	#Create first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(settings, screen, aliens, alien_number,
				row_number)


def check_fleet_edges(settings, aliens):
	"""Reacts to the aliens reaching the end of the screen"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break


def change_fleet_direction(settings, aliens):
	"""Drop fleet and change direction"""
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1


def update_aliens(settings, stats, screen, ship, aliens, bullets):
	"""Update all of aliens positions"""
	check_fleet_edges(settings, aliens)
	aliens.update()

	#Check collisions alien - ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, stats, screen, ship, aliens, bullets)

	#Check collisions alien - bottom 
	check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)


def ship_hit(settings, stats, screen, ship, aliens, bullets):
	"""Process collisions alien-ship"""
	#Derciment ships_left
	if stats.ships_left > 0:
		stats.ships_left -= 1

		#Clear list of aliens and bullets
		aliens.empty()
		bullets.empty()

		#Create new aliens fleet and placing ship in the middle
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()

		#Pause after death
		sleep(1.5)
	else:
		stats.game_active = False
		#Show cursor
		pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, stats, 
	screen, ship, aliens, bullets):
	"""Check aliens collisions with the bottom"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#The same thing happens, as in collision with the ship
			ship_hit(settings, stats, screen, ship, aliens, bullets)
			break