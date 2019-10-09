import pygame
import sys
import random

pygame.init()

WIDTH = 880
HEIGHT = 660

CYAN = (100,100,255)
start_pos = [400, 300]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

num_x_tiles = 80
num_y_tiles = 60
tiles = [[0 for x in range(num_x_tiles)] for y in range(num_y_tiles)]

x = 0
y = 0

for i in range(0, num_y_tiles):
	for j in range(0, num_x_tiles):
		tiles[i][j] = pygame.draw.rect(screen, CYAN, (x, y, 10, 10))
		x += 11
	x = 0
	y += 11

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.update()

