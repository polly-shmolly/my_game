import pygame
from support import import_folder


class ParticleEffect(pygame.sprite.Sprite):
	def __init__(self, pos, stat_type):
		"""
		:param pos: position of the player
		:param stat_type: player status
		"""
		super().__init__()
		self.frame_index = 0
		self.animation_speed = 0.5
		if stat_type == 'jump':
			self.frames = import_folder('graphics/character/dust_particles/jump')
		if stat_type == 'land':
			self.frames = import_folder('graphics/character/dust_particles/land')
		if stat_type == 'explosion':
			self.frames = import_folder('graphics/enemy/explosion')
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center=pos)

	def animate(self):
		self.frame_index += self.animation_speed
		if self.frame_index >= len(self.frames):
			self.kill()
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self, x_shift):
		self.animate()
		self.rect.x += x_shift
