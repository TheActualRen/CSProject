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

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0

        self.jump_count += 1 
        if self.jump_count == 1:
            self.fall_count = 0
        
        
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
    
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def handle_vertical_collisions(self, objects, dy):
        for obj in objects:
            if pygame.sprite.collide_mask(self, obj):
                if dy > 0:
                    self.rect.bottom = obj.rect.top
                    self.landed()
                elif dy < 0:
                    self.rect.top = obj.rect.bottom
                    self.hit_head()



    def handle_movements(self, objects):
        keys = pygame.key.get_pressed()

        self.x_vel = 0
        if keys[pygame.K_LEFT]:
            self.move_left(self.PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            self.move_right(self.PLAYER_VEL)

        self.handle_vertical_collisions(objects, self.y_vel)
    
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



