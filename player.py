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
        self.jump_count = 0
        self.SPRITES = sprites
        self.hit = False
        self.hit_count = 0 
        self.health = 20
        self.score = 0 
    
    def decrease_health(self):
        self.health -= 1
        if self.health == 0:
            pygame.quit()
            exit()
    
    
    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0

        self.jump_count += 1 
        if self.jump_count == 1:
            self.fall_count = 0
        
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    

    def got_hit(self):
        self.hit = True
        self.hit_count = 0 
        self.decrease_health()

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
        collided_objects = []

        for obj in objects:
            if pygame.sprite.collide_mask(self, obj):
                if dy > 0:
                    self.rect.bottom = obj.rect.top
                    self.landed()
                elif dy < 0:
                    self.rect.top = obj.rect.bottom
                    self.hit_head()
                
                collided_objects.append(obj)
        
        return collided_objects


    def collide(self, objects, dx):
        self.move(dx, 0)
        self.update()
        collided_object = None

        for obj in objects:
            if pygame.sprite.collide_mask(self, obj):
                collided_object = obj
                break
        
        self.move(-dx, 0)
        self.update()
        
        return collided_object


    def handle_movements(self, objects):
        keys = pygame.key.get_pressed()

        self.x_vel = 0
        collide_left = self.collide(objects, -self.PLAYER_VEL * 2) # multiplied by 2 so animation count does not affect collision
        collide_right = self.collide(objects, self.PLAYER_VEL * 2)

        if keys[pygame.K_LEFT] and not collide_left:
            self.move_left(self.PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            self.move_right(self.PLAYER_VEL)

        vertical_collisions = self.handle_vertical_collisions(objects, self.y_vel)
        to_check = [collide_left, collide_right, *vertical_collisions] 

        for obj in to_check:
            if obj:
                if obj and obj.name == "fire":
                    self.got_hit()
                elif obj.name == "melon" and obj in objects:
                    objects.remove(obj)        
                    self.score += 1


    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY) # simulating accel due to gravity
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1 
        
        if self.hit_count > fps * 2:
            self.hit = False 
            self.hit_count = 0
        
        
        self.fall_count += 1 
        self.update_sprite()


    def update_sprite(self):
        sprite_sheet = "idle"

        if self.hit: 
            sprite_sheet = "hit"

        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"

        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"

        elif self.x_vel != 0:
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
        

    def draw(self, window, offset_x):
        window.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))



