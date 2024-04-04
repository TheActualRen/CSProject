import pygame

from window import Window
from player import Player
from assets import *
from block import Block
from fire_trap import Fire
from melon import Melon


if __name__ == "__main__":
    pygame.init()
    game_window = Window()
    game_window_surface = game_window.generate_window()

    player_sprites = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    player = Player(100, 100, 50, 50, player_sprites)

    block_size = 96

    fire_trap = Fire(100, game_window.HEIGHT - block_size - 64, 16, 32)
    fire_trap.on()

    floor = [Block(i * block_size, game_window.HEIGHT - block_size, block_size)
        for i in range(-game_window.WIDTH // block_size, (game_window.WIDTH * 2) // block_size)]
    
    blocks = [*floor, Block(0, game_window.HEIGHT - block_size, block_size)]

    melon_positions = [(200, 500), (400, 300), (600, 600)]  # Adjust positions as needed
    melons = [Melon(x, y) for x, y in melon_positions]

    objects = [*floor, Block(0, game_window.HEIGHT - block_size *2, block_size),
            Block(block_size * 3, game_window.HEIGHT - block_size * 4, block_size), 
            fire_trap] + melons

    offset_x = 0
    scroll_area_width = 200

    game_running = game_window.event_loop(game_window_surface, player, objects, offset_x, scroll_area_width, fire_trap, melons)


