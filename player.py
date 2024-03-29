import pygame

from assets import * 

class Player(pygame.sprite.Sprite):

    COLOUR = (255, 255, 255)
    GRAVITY = 1 
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height, sprites):
        super().__init__()

        self.rect = pygame.Rect(x, y, width, height)
        self.PLAYER_VEL = 5
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None 
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0 
        self.SPRITES = sprites


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0


    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0


    def handle_movements(self):
        keys = pygame.key.get_pressed()

        self.x_vel = 0
        if keys[pygame.K_LEFT]:
            self.move_left(self.PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            self.move_right(self.PLAYER_VEL)

    
    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY) # simulating accel due to gravity
        self.move(self.x_vel, self.y_vel)
        
        self.fall_count += 1 
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_vel != 0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1 
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite) # Allows us to perform pixel perfect collision
        

    def draw(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))



