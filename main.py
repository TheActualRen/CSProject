import pygame

from window import Window
from player import Player


if __name__ == "__main__":
    pygame.init()
    game_window = Window()
    game_window_surface = game_window.generate_window()

    player = Player(100, 100, 50, 50)

    game_running = game_window.event_loop(game_window_surface, player)


