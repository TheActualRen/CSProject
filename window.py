import pygame
from os.path import join

from player import Player

class Window:
    def __init__(self):
        self.FPS = 60
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.CAPTION = "My Game"
        self.clock = pygame.time.Clock()


    def generate_window(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.CAPTION)
        return self.window


    def get_background(self, name):
        image = pygame.image.load(join("assets", "Background", name))
        _, _, width, height = image.get_rect()
        
        tiles = []
        
        for i in range(self.WIDTH // width + 1):
            for j in range(self.HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)
        
        return tiles, image
    

    def draw(self, window, background, bg_image, player):
        for tile in background:
            window.blit(bg_image, tile)
        
        player.draw(window)
    
        pygame.display.update()


    def event_loop(self, window, player):

        self.background, self.bg_image = self.get_background("Yellow.png")

        while True:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    exit()

            player.loop(self.FPS)
            player.handle_movements()
            self.draw(window, self.background, self.bg_image, player)
      