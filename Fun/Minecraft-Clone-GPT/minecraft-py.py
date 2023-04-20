# Code from ChatGPT Run at own risk!
import pygame
from pygame.locals import *
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
BACKGROUND_COLOR = (135, 206, 250)
BLOCK_COLOR = (139, 69, 19)
PLAYER_COLOR = (255, 255, 0)

class Block:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self, screen):
		pygame.draw.rect(screen, BLOCK_COLOR, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self, screen):
		pygame.draw.rect(screen, PLAYER_COLOR, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption('Minecraft Clone')
	clock = pygame.time.Clock()

	# Create blocks
	blocks = []
	for i in range(GRID_WIDTH):
		for j in range(GRID_HEIGHT):
			if random.random() < 0.2:
				blocks.append(Block(i, j))

	# Create player
	player = Player(0, 0)

	# Game loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		# Handle player movement
		keys = pygame.key.get_pressed()
		if keys[K_UP] and player.y > 0:
			player.y -= 1
		if keys[K_DOWN] and player.y < GRID_HEIGHT - 1:
			player.y += 1
		if keys[K_LEFT] and player.x > 0:
			player.x -= 1
		if keys[K_RIGHT] and player.x < GRID_WIDTH - 1:
			player.x += 1

		screen.fill(BACKGROUND_COLOR)

		# Draw blocks
		for block in blocks:
			block.draw(screen)

		# Draw player
		player.draw(screen)

		pygame.display.update()
		clock.tick(10)

if __name__ == '__main__':
	main()
