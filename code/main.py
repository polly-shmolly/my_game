import pygame
import sys
from code.settings import *
from code.level import Level
from code.overworld import Overworld
from code.ui import UI
from code.registration import Registration, Button
from code.support import save_high_score


class Game:
	"""
	game logic
	"""
	def __init__(self):

		# game attributes
		self.max_level = 2
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0

		# audio
		self.level_bg_music = pygame.mixer.Sound('../audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld_music.wav')

		# registration creations
		self.registration = Registration(screen)
		self.button1 = Button('Start game', 300, 60, (700, 300), 6, screen, self.create_overworld)
		self.status = 'registration'
		self.level_bg_music.play(loops=-1)

		# user interface
		self.ui = UI(screen)

	def create_level(self, current_level):
		self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops=-1)

	def create_overworld(self, current_level, new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level, self.max_level, screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops=-1)
		self.level_bg_music.stop()

	def change_coins(self, amount):
		self.coins += amount

	def change_health(self, amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0, self.max_level, screen, self.create_level)
			self.status = 'overworld'
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops=-1)

	def run(self):
		if self.status == 'registration':
			self.registration.run()
			self.button1.draw()
		if self.status == 'overworld':
			self.overworld.run()
		if self.status == 'level':
			self.level.run()
			self.ui.show_health(self.cur_health, self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()
registration = Registration(screen)
pygame.display.set_caption("my_game")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_high_score(registration.user_text, game.coins)
			pygame.quit()
			sys.exit()
	
	screen.fill('grey')
	game.run()

	pygame.display.update()
	clock.tick(60)

