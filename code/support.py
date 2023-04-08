from csv import reader
from code.settings import tile_size
from os import walk
import pygame


def import_folder(path):
	"""list of images"""
	surface_list = []

	for _, __, image_files in walk(path):
		for image in image_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list


def import_csv_layout(path):
	"""information from csv files in list"""
	terrain_map = []
	with open(path) as my_map:
		level = reader(my_map, delimiter=',')
		for row in level:
			terrain_map.append(list(row))
		return terrain_map


def save_high_score(name, coin):
	"""
	:param name: user name
	:param coin: amount of coins
	:return: new high score
	"""
	with open('code/high_score.txt', 'r') as f:
		data = f.readline()
		coin_score = data.split(' ')[1]

	if coin >= int(coin_score):
		coin_score = coin
		name_score = name
		new_data = name_score + ' ' + str(coin_score)
		with open('high_score.txt', 'w') as f:
			f.write(new_data)
		return new_data
	return data


def import_cut_graphics(path):
	surface = pygame.image.load(path).convert_alpha()
	tile_num_x = int(surface.get_size()[0] / tile_size)
	tile_num_y = int(surface.get_size()[1] / tile_size)

	cut_tiles = []
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			x = col * tile_size
			y = row * tile_size
			new_surf = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
			new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
			cut_tiles.append(new_surf)

	return cut_tiles
