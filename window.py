import pygame
from os.path import join

class Window:
    def __init__(self):
        self.FPS = 60
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.CAPTION = "My Game"
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()



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
    

    def draw(self, window, background, bg_image, player, objects, offset_x):
        for tile in background:
            window.blit(bg_image, tile)
        
        for obj in objects:
            obj.draw(window, offset_x)
        
        player.draw(window, offset_x)

        font = pygame.font.SysFont(None, 36)
        health_text = font.render(f"Health: {player.health}/20", True, (255, 255, 255))
        window.blit(health_text, (10, 10))

        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        window.blit(score_text, (10, 40))

        timer_text = font.render(f"Time: {(int(self.timer))}", True, (255, 255, 255))
        window.blit(timer_text, (10, 70))  
            
        pygame.display.update()


    def event_loop(self, window, player, objects, offset_x, scroll_area_width, fire_traps, melons):

        self.background, self.bg_image = self.get_background("Yellow.png")

        while True:
            self.clock.tick(self.FPS)
            elapsed_time = pygame.time.get_ticks() - self.start_time
            elapsed_time /= 1000
            self.timer = max(30 - elapsed_time, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()

            

            if self.timer <= 0 and player.score < 3:
                pygame.quit()
                exit()
                

            player.loop(self.FPS)
            for trap in fire_traps:
                trap.loop()
            
            for melon in melons:
                melon.loop()

            player.handle_movements(objects)
            self.draw(window, self.background, self.bg_image, player, objects, offset_x)

            if ((player.rect.right - offset_x >= self.WIDTH - scroll_area_width and player.x_vel > 0) or 
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel
