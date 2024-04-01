import pygame

from object import Object
from assets import *

class Fire(Object):
    ANIMATION_DELAY = 3
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire_trap = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire_trap["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"
    
    def off(self):
        self.animation_name = "off"

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image) 
    
    def loop(self):
        sprites = self.fire_trap[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1 
        self.update()

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0  # Reset animation count


