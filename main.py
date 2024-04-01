import pygame

from window import Window
from player import Player
from assets import *
from block import Block


if __name__ == "__main__":
    pygame.init()
    game_window = Window()
    game_window_surface = game_window.generate_window()

    player_sprites = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    player = Player(100, 100, 50, 50, player_sprites)

    block_size = 96
    floor = [Block(i * block_size, game_window.HEIGHT - block_size, block_size)
for i in range(-game_window.WIDTH // block_size, (game_window.WIDTH * 2) // block_size)]
    blocks = [*floor, Block(0, game_window.HEIGHT - block_size, block_size)]

    offset_x = 0
    scroll_area_width = 200

    game_running = game_window.event_loop(game_window_surface, player, blocks, offset_x, scroll_area_width)


