import pygame

from window import Window
from player import Player
from assets import *
from block import Block
from fire_trap import Fire
from melon import Melon


def main():
    pygame.init()
    game_window = Window()
    game_window_surface = game_window.generate_window()

    player_sprites = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    player = Player(100, 100, 50, 50, player_sprites)

    block_size = 96

    fire_traps = [Fire(block_size * 2,       game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 2 + 32,  game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 2 + 64,  game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 12,      game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 12 + 32, game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 12 + 64, game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 13,      game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 13 + 32, game_window.HEIGHT - block_size - 64, 16, 32),
                  Fire(block_size * 13 + 64, game_window.HEIGHT - block_size - 64, 16, 32),



                  
    ]
    
    for trap in fire_traps:
        trap.on()

    floor = [Block(i * block_size, game_window.HEIGHT - block_size, block_size)
             for i in range(-game_window.WIDTH // block_size, (game_window.WIDTH * 4) // block_size)]

    blocks = [*floor,
              Block(block_size * 4,  game_window.HEIGHT  -  block_size * 3.5, block_size),
              Block(block_size * 5,  game_window.HEIGHT  -  block_size * 3.5, block_size),
              Block(block_size * 6,  game_window.HEIGHT  -  block_size * 3.5, block_size), 
              Block(block_size * 9,  game_window.HEIGHT  -  block_size * 5  , block_size),
              Block(block_size * 10, game_window.HEIGHT  -  block_size * 5  , block_size),
              Block(block_size * 15, game_window.HEIGHT  -  block_size * 3.5, block_size),


    
    ]

    melon_positions = [
        (block_size,         game_window.HEIGHT  -  block_size * 1.5),
        (block_size * 3.35,         game_window.HEIGHT  -  block_size * 1.5),


        (block_size * 4.35,  game_window.HEIGHT  -  block_size * 4),
        (block_size * 5.35,  game_window.HEIGHT  -  block_size * 4),
        (block_size * 6.35,  game_window.HEIGHT  -  block_size * 4),
        (block_size * 9.35,  game_window.HEIGHT  -  block_size * 5.5),
        (block_size * 10.35, game_window.HEIGHT  -  block_size * 5.5),
        (block_size * 15.35, game_window.HEIGHT  -  block_size * 4)
                       
    ]  

    melons = [Melon(x, y) for x, y in melon_positions]

    objects = [*blocks] + fire_traps + melons  # Include blocks, fire_trap, and melons

    offset_x = 0
    scroll_area_width = 200

    game_window.event_loop(game_window_surface, player, objects, offset_x, scroll_area_width, fire_traps, melons)


if __name__ == "__main__":
    main()
